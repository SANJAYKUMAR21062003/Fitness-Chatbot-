# Genfit AI

A web-based fitness chatbot application built with Flask and Google's Gemini AI. The application provides workout suggestions based on user preferences and allows users to interact with a chatbot for fitness-related advice.

## Features

- **User Authentication**: Register, login, and reset password functionality.
- **Workout Suggestions**: Get personalized workout suggestions based on fitness goals, target muscles, and location (gym or home).
- **Chatbot**: Interact with a chatbot powered by Google's Gemini AI for fitness-related queries.
- **Database**: SQLite database to store user data and workout preferences.

## Prerequisites

- Python 3.8 or higher
- Google Gemini API key (replace `API_KEY` in `chatbot.py` with your actual API key)
- Gmail account for sending password reset emails (replace `MAIL_USERNAME` and `MAIL_PASSWORD` in `auth.py` with your Gmail credentials)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/fitness-chatbot-project.git
   cd fitness-chatbot-project
Create a virtual environment (optional but recommended):

bash
Copy
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the required dependencies:

bash
Copy
pip install -r requirements.txt
Set up the database:

The database will be automatically initialized when you run the application for the first time.

Replace placeholders in the code:

Replace API_KEY in chatbot.py with your Google Gemini API key.

Replace MAIL_USERNAME and MAIL_PASSWORD in auth.py with your Gmail credentials.

Running the Application
Start the Flask development server:

bash
Copy
python app.py
Open your browser and navigate to:

Copy
http://localhost:5000
Use the application:

Register a new account or log in with existing credentials.

Get workout suggestions based on your preferences.

Interact with the chatbot for fitness advice.

Project Structure
Here’s an overview of the project structure:

Copy
fitness-chatbot-project/
│── 📂 static/
│   │── style.css  # CSS for frontend styling
│── 📂 templates/
│   │── index.html  # Login page
│   │── signup.html # Signup page
│   │── forgot_password.html # Forgot password page
│   │── chatbot.html # Chatbot interface
│   │── workout_suggestion.html # Workout suggestion page
│── app.py  # Main Flask application
│── chatbot.py  # Google Gemini AI chatbot integration
│── auth.py  # User authentication and password reset functionality
│── database.py  # SQLite database setup and operations
│── workouts.json  # Workout suggestions based on user preferences
│── requirements.txt  # Python dependencies
│── README.md  # Project documentation
Explanation of Key Files and Folders
static/: Contains static files like CSS for styling the frontend.

templates/: Contains HTML templates for the web pages (login, signup, chatbot, etc.).

app.py: The main Flask application that handles routing and logic.

chatbot.py: Integrates Google's Gemini AI for chatbot functionality.

auth.py: Handles user authentication, registration, and password reset.

database.py: Manages SQLite database operations (user data, workout preferences).

workouts.json: Contains workout suggestions categorized by location, goal, and target muscle.

requirements.txt: Lists all Python dependencies required to run the project.

Contributing
Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.
