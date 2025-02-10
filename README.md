Fitness Chatbot 
Overview
The AI-Powered Fitness Chatbot is an interactive fitness assistant that provides personalized workout recommendations based on user preferences, goals, and available equipment. It leverages Google Generative AI for intelligent responses and uses Streamlit for a user-friendly interface.

Features
✅ AI-driven chatbot for fitness guidance
✅ Personalized workout recommendations
✅ Tracks user preferences & history
✅ Beginner-friendly & interactive UI
✅ Supports home & gym workouts
✅ Exercises categorized by muscle groups
✅ BMR Calculator for calorie needs

Tech Stack
Backend
Python
Google Generative AI
JSON (data storage)
Python-dotenv (environment management)
Frontend
Streamlit
Project Structure
bash
Copy
Edit
Project_Folder/
├── chatbot.py          # Main chatbot logic
├── chatbot_ui.py       # Streamlit User Interface
├── database.py         # Handles workout database interactions
├── user.py             # Manages user profiles
├── workouts.json       # Stores exercise data
├── user_data.json      # Stores user preferences & history
├── .env                # Environment variables
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
Installation & Setup
1️⃣ Clone the Repository
bash
Copy
Edit
git clone https://github.com/your-username/fitness-chatbot.git
cd fitness-chatbot
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Set Up Environment Variables
Create a .env file in the root directory
Add your Google API Key inside .env:
ini
Copy
Edit
GOOGLE_API_KEY=your_api_key_here
4️⃣ Run the Chatbot
bash
Copy
Edit
streamlit run chatbot_ui.py
Usage
1️⃣ Open the Streamlit UI
2️⃣ Enter your details (weight, height, goals, equipment)
3️⃣ Receive personalized workout plans
4️⃣ Modify your preferences anytime


Future Enhancements 🚀
✅ Voice-enabled chatbot interaction
✅ Workout tracking & analytics
✅ Integration with wearable fitness devices
✅ Mobile app version
Contributors
👤 SANJAYKUMAR S – Developer

License
📜 MIT License

