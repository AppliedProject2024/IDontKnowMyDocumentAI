# StudyBuddy-AI Streamlit Frontend
This repository contains the codebase for the Frontend of the StudyBuddy-AI web-application. This frontend interface is developed using Streamlit, utilising its UI components for a sleek and appealing user interface. The frontend also provides means of connecting to the Flask based Backend API developed for this application located in the Backend repository.

A video has been uploaded to youtube demonstrating StudyBuddy-AI in order to allow users to understand how to operate the application this video can be found [here](https://www.youtube.com/watch?v=vXqaH4HBn64)

## AI powered tools
The frontend supports the following AI powered tools that make up StudyBuddy-AI: 
🤖Q&A:
The Q&A feature is as simple as it sounds, just input a question, hit send, and watch as the AI responds with information directly e related to your documents. Need to know when your projects are due? Just ask, and the answer will appear infront of you in no time!

📚Summary:
The Summary feature allows users to create a summary based on a query and your stored documents. Sick and tierd of specfying the lenght and complexity of your summary to AI? simply just select the word count and complexity level from the provided drop downs and hit send.

✔️MCQ:
Multiple-choice questions are a grate way to learn for many students, and StudyBuddy-AI aims to provide the best MCQ experience possible. Simply enter your query, and select the number of questions and complexity of the questions, and watch as a interactive MCQ is generated based on your documents. See your scores at the end of the quiz to see whether you need to improve, or marvel at your own intellegence, its up to you!

## Cloning and running locally
To run StudyBuddy-AI locally the following considerations must be taken.
- Python version: 3.12.10
- Packages: Outlined in 'requirements.txt and can be installed using: 'pip install -r requirements.txt'
- Backend: The backend API must be running in order to run the frontend this can be done by following the steps in the backend repository. Once the Backend is up and running set check the 'Example.env' file here you will find a variable called API_URL you will need to add the backends url in here.
- Run: Run the development server using : streamlit run Main.py

## Deployed application:
Rather then going to the hastle of cloning this application simply visit the deployed version [here](https://studybuddyai-frontend.onrender.com)
