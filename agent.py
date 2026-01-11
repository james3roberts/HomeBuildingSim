import random
from config import templates

class Agent:
    def __init__(self, username, user_template, night_life):
        self.username = username          # use 'username' consistently
        self.night_life = night_life
        self.current_role = None

        # Map numeric input to template string
        template_map = {1: "Rookie", 2: "Skilled_Worker", 3: "Foreman"}
        selected_template = template_map.get(user_template, "Rookie")  # Default to Rookie

        # Load the actual template dictionary
        template = templates[selected_template]

        # Sample random starting stats
        self.experience = random.randint(*template["experience_range"])
        self.strength = random.randint(*template["strength_range"])
        self.stamina = random.randint(*template["stamina_range"])
        self.recovery_rate = random.randint(*template["recovery_rate_range"])
        self.follow_directions = random.randint(*template["follow_directions_range"])
        self.tool_skills = random.randint(*template["tool_skills_range"])

    def print_stats(self):
        print("\n--- Agent Stats ---")
        print(f"Username: {self.username}")
        print(f"Night Life: {self.night_life}")
        print(f"Experience: {self.experience}")
        print(f"Strength: {self.strength}")
        print(f"Stamina: {self.stamina}")
        print(f"Recovery Rate: {self.recovery_rate}")
        print(f"Follow Directions: {self.follow_directions}")
        print(f"Tool Skills: {self.tool_skills}")
        print(f"Current Role: {self.current_role}")
