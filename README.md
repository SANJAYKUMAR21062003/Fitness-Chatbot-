# Fitness Chatbot Project

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
