from flask import Flask, request, jsonify
import json
import random
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/ques": {"origins": "http://127.0.0.1:5500"}})

# Loading our question data from local
with open('updated_questions.json', 'r') as file:
    data = json.load(file)

def generateQuestions(data, quesReq):

    total = quesReq['marks']
    diff_distribution = quesReq['category']

    mark_distribution = {}
    
    # Marks allocation
    for difficulty_percentage in diff_distribution:
        mark_allocation = int((diff_distribution[difficulty_percentage] / 100) * total)
        mark_distribution[difficulty_percentage] = mark_allocation

  
    # Separate questions by difficulty
    question_difficulties = {'Easy': [], 'Medium': [], 'Hard': []}
    for question in data['questions']:
        question_difficulties[question['difficulty']].append(question)

    generated_questions = []
    seen = set()

    for difficulty in mark_distribution:
        # difficulty_lower = difficulty.lower()
        marks_allocated = 0
        while marks_allocated < mark_distribution[difficulty]:
            if not question_difficulties[difficulty]:
                return {'error': f"Not enough questions in the category {difficulty}. You can lower the total marks"}, False

            randomques = random.choice(question_difficulties[difficulty])
            queshash = hash(json.dumps(randomques))
            # print("Question hash", queshash)
            if randomques['marks'] <= (mark_distribution[difficulty] - marks_allocated) and queshash not in seen:
                generated_questions.append(randomques)
                seen.add(queshash)
                marks_allocated += randomques['marks']
                # here we are removing the question from the question_difficulties array
                question_difficulties[difficulty].remove(randomques)

    return generated_questions, True

@app.route('/ques', methods=['POST'])
def todo():
    user = request.get_json()

    res, success = generateQuestions(data, user)

    # Check if error happened
    if not success:
        return jsonify(res), 400
    return jsonify(res), 200

if __name__ == '__main__':
    app.run(port=5000, debug=True)