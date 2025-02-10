import streamlit as st
import os
from dotenv import load_dotenv
import json
import google.generativeai as genai
from Database import database
from Database import user

# Load environment variables
load_dotenv()

# Initialize components
db = database.Database("data/megaGymDataset.csv")
user_profile = user.User()

def load_workout_data():
    with open("data/workouts.json", "r") as file:
        return json.load(file)

def load_user_data():
    if os.path.exists("data/user_data.json"):
        with open("data/user_data.json", "r") as file:
            return json.load(file)
    else:
        return {}

def save_user_data(user_data):
    if os.path.exists("data/user_data.json"):
        with open("data/user_data.json", "r") as file:
            data = json.load(file)
    else:
        data = {}
    
    user_id = len(data) + 1  # Assign a new user ID
    data[user_id] = user_data
    
    with open("data/user_data.json", "w") as file:
        json.dump(data, file, indent=4)

workouts = load_workout_data()

# Streamlit UI
st.set_page_config(page_title="Fitness Chatbot", layout="wide")
st.title("Fitness Chatbot")
st.write("Get personalized workout and fitness advice!")

# User input section
user_input = st.text_input("You:", placeholder="Ask me anything about fitness...")

# Function to get Gemini response
def get_gemini_response(user_input):
    genai.configure(api_key=os.getenv("GOOGLE_GEMINI_API_KEY"))  # Load API key from .env
    model = genai.GenerativeModel("gemini-pro")  # Use Gemini-Pro model
    response = model.generate_content(user_input)
    return response.text if response else "Sorry, I couldn't process that."

if user_input:
    if user_input.lower() in ["exit", "quit"]:
        st.write("Goodbye! Have a great workout! 💪")
    else:
        response = get_gemini_response(user_input)
        st.write("**Bot:**", response)

# User Profile Section
st.subheader("User Profile")
name = st.text_input("Name", placeholder="Enter your name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
goal = st.selectbox("Your fitness goal", ["Muscle Gain", "Fat Loss"])

# Workout Suggestions
st.subheader("🏋️ Workout Suggestions")
workout_type = st.selectbox("Choose workout type", ["Gym", "Home"])
body_part = st.selectbox("Which body part would you like to work on?", ["Chest", "Back", "Legs", "Shoulders", "Full Body"])

if st.button(f"Get {body_part} Workouts", key=f"get_{body_part}_workouts"):
    selected_workouts = workouts.get(workout_type.lower(), {}).get(goal.lower().replace(" ", "_"), {}).get(body_part.lower(), [])
    
    if selected_workouts:
        for workout in selected_workouts:
            if "reps" in workout:
                st.write(f"**{workout['exercise']}** - {workout['target']} ({workout['reps']})")
            else:
                st.write(f"**{workout['exercise']}** - {workout['target']} ({workout['duration']})")
        
        user_data = {
            "name": name,
            "age": age,
            "weight": weight,
            "goal": goal,
            "workout_type": workout_type,
            "body_part": body_part,
            "workouts": selected_workouts
        }
        save_user_data(user_data)
        st.write("Your workout data has been saved!")
    else:
        st.write(f"No workouts available for {body_part} and {goal}. Please try another selection.")
