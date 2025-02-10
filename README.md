#Fitness Chatbot

Introduction
The AI-Powered Fitness Chatbot is a personalized AI fitness companion that provides:

• Exercise descriptions with clear instructions and form tips
• Tailored workout recommendations based on user goals (muscle gain, weight loss, endurance)
• Fitness Q&A covering training principles, nutrition, and general fitness guidance

Whether you're a beginner or a fitness enthusiast, this chatbot adapts to your needs, offering customized workouts for both gym & home training using barbells, cables, and bodyweight exercises.

#Key Features

• Exercise Library – Detailed descriptions of exercises categorized by muscle groups
• Personalized Workout Plans – Tailored routines based on user input
• AI-Powered Responses – Answers to fitness-related questions using Google Generative AI
• Beginner-Friendly UI – Simple interface powered by Streamlit
• BMR Calculator – Estimates daily calorie needs for goal-based planning

#Technologies Used

Technology	Purpose
Python	Core programming language
Google Generative AI	AI-driven workout recommendations
Streamlit	Web framework for building the user interface
Pandas	Data manipulation and exercise database management
JSON	Stores user preferences & workout history
Python-dotenv	Manages API keys and environment variables

#Project Structure

fitness_chatbot/
├── chatbot.py          # Main chatbot logic
├── chatbot_ui.py       # Streamlit User Interface
├── database.py         # Handles workout database interactions
├── user.py             # Manages user profiles
├── workouts.json       # Stores exercise data
├── user_data.json      # Stores user preferences & history
├── .env                # Environment variables
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation

#How to Run Locally

1. Clone the Repository
git clone https://github.com/your-username/fitness-chatbot.git
cd fitness-chatbot
2. Install Dependencies
pip install -r requirements.txt
3.Set Up Environment Variables
• Create a .env file in the root directory
• Add your Google API Key inside .env:
GOOGLE_API_KEY=your_api_key_here
4.Run the Chatbot
streamlit run chatbot_ui.py

#Screenshot of UI


![image alt](https://github.com/SANJAYKUMAR21062003/Fitness-Chaatbot/blob/48ad963b53e79da542317beead8d0b174641012b/Screenshot%20(3).png)



#License
MIT License

#Get Involved
Contributions, suggestions, and feedback are welcome! Feel free to open issues or submit pull requests.
