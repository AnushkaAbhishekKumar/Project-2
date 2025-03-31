#Project_2(TDS Solver)
## Backround
You are a clever student who has joined IIT Madras’ Online Degree in Data Science. You have just enrolled in the Tools in Data Science course.

To make your life easier, you have decided to build an LLM-based application that can automatically answer any of the graded assignment questions.

Specifically, you are building and deploying an API that accepts any question from one of these 5 graded assignments:

Graded Assignment 1
Graded Assignment 2
Graded Assignment 3
Graded Assignment 4
Graded Assignment 5
… and responds with the answer to enter in the assignment.

##Create an API

Your application exposes an API endpoint. Let’s assume that it is at https://your-app.vercel.app/api/.

The endpoint must accept a POST request, e.g. POST https://your-app.vercel.app/api/ with the question as well as optional file attachments as multipart/form-data.

For example, here’s how anyone can make a request:

```bash
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Download and unzip file abcd.zip which has a single extract.csv file inside. What is the value in the "answer" column of the CSV file?" \
  -F "file=@abcd.zip"
```bash
