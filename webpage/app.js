document.querySelector("#form").addEventListener("submit", async (event) => {
  event.preventDefault();

  const marks = event.target.marks.value;
  const easy = event.target.easy.value;
  const medium = event.target.medium.value;
  const hard = event.target.hard.value;

  const response = await fetch('http://localhost:5000/ques', { 
    method: 'POST',
    body: JSON.stringify({ 
      "marks": parseInt(marks), 
      "category": { 
        "Easy": parseInt(easy), 
        "Medium": parseInt(medium), 
        "Hard": parseInt(hard)
      } 
    }),
    headers: {
      'Content-Type': 'application/json'
    },
  });

  // Check if the server responded with a success code
  const data = await response.json();
  if (!response.ok) {
      const errDiv = document.createElement('div');
      errDiv.classList.add('err');
      errDiv.innerText = data.error;  // Get the server error message
      document.getElementById('allquestions').appendChild(errDiv);
      return;
  }

  document.getElementById('allquestions').innerHTML = '';
  data.forEach((question) => {
      const div = document.createElement('div');
      div.classList.add('question-card');

      const marksDiv = document.createElement('div');
      marksDiv.classList.add('marks');
      marksDiv.innerHTML = `Marks: ${question.marks}`;
      div.appendChild(marksDiv);

      const difficultyDiv = document.createElement('div');
      difficultyDiv.classList.add('difficulty');
      difficultyDiv.innerHTML = `Difficulty: ${question.difficulty}`;
      div.appendChild(difficultyDiv);

      div.innerHTML += `${question.question}, Subject: ${question.subject}, Topic: ${question.topic}`;
      document.getElementById('allquestions').appendChild(div);
    });
});