import json
import os
from Database import database  # Import database module


class User:
    def __init__(self, filename="data/user_data.json"):
        self.filename = filename
        self.user_data = self.load_user_data()
        self.db = database.Database("data/megaGymDataset.csv")  # Ensure correct path

    def load_user_data(self):
        """Load user data from a JSON file."""
        if os.path.exists(self.filename):
            try:
                with open(self.filename, "r", encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, IOError) as e:
                print(f"Error loading user data: {e}")
                return {}
        return {}

    def save_user_data(self):
        """Save user data to a JSON file."""
        try:
            with open(self.filename, "w", encoding="utf-8") as file:
                json.dump(self.user_data, file, indent=4)
        except IOError as e:
            print(f"Error saving user data: {e}")

    def set_preference(self, user, preference, value):
        """Set user preference and save it."""
        if not isinstance(user, str) or not isinstance(preference, str):
            print("Invalid input: User and preference must be strings.")
            return
        
        if user not in self.user_data:
            self.user_data[user] = {}

        self.user_data[user][preference] = value
        self.save_user_data()

    def get_preference(self, user, preference):
        """Retrieve user preference."""
        return self.user_data.get(user, {}).get(preference)

    def log_workout(self, user, workout, duration):
        """Log a workout for the user in the database."""
        if not isinstance(duration, (int, float)) or duration <= 0:
            print("Invalid duration: Must be a positive number.")
            return
        
        try:
            self.db.save_workout(user, workout, duration)
        except Exception as e:
            print(f"Error logging workout: {e}")

    def get_user_workouts(self, user):
        """Retrieve workout history for a specific user."""
        try:
            return self.db.get_user_workouts(user)
        except Exception as e:
            print(f"Error retrieving user workouts: {e}")
            return []
