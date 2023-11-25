# Question Generator Web App

This is a web app that generates a wide range of questions based on the user's chosen difficulty and scoring preferences.

## How to Use:

1. **Clone the Repository:**
   - Run `git clone git@github.com:rajshukla1102/quesgen.git` in your terminal.
   - Alternatively, download and extract the zip file.

2. **Install Libraries:**
   - Go to the project directory.
   - Run `pip install -r requirements.txt` to install required Python libraries.

3. **Start the App:**
   - Run `python app.py` to launch the Flask app.

4. **Launch the Web Interface:**
   - Open `index.html` in your browser.

5. **Generate Questions:**
   - Enter your difficulty levels and total marks.
   - Click "Generate Questions" to see a list of relevant questions.

**API Usage:**

If you want to run only the API, you can use tools like Postman or cURL. Here's an example cURL command:

```bash
curl -X POST -H "Content-Type: application/json" -d '{ "marks": 100, "category": { "Easy": 30, "Medium": 50, "Hard": 20 } }' http://localhost:5000/ques
```

Enjoy effortless question generation, whether through the web interface or the API!
