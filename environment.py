class Environment:
    def __init__(self):
        self.active_tools = ["Muscles", "Nail Gun", "Saw", "Tape"]

        self.progress = {
            "floor": 0,
            "walls": 0,
            "floor2": 0,
            "walls2": 0,
            "roof": 0,
            "stairs": 0
        }

        self.hazards = ["Rain", "Cold", "Hot", "Snow", "Hail", "Wind"]
        self.challenges = [
            "material_distance",
            "material_elevation",
            "material_weight",
            "material_amount"
        ]

        self.time_remaining = 10 #days to build the house i mean this must be a tract and should only be 5 or less
        self.history = []

    def move_wood(self, agent):
        # progress depends on agent ability (template-driven via stats)
        progress_increment = agent.strength + agent.tool_skills

        # stamina cost scales with strength
        stamina_cost = 3 - (agent.strength // 2)
        if stamina_cost < 1:
            stamina_cost = 1

        # apply progress (for now we attach this to floor prep)
        self.progress["floor"] += progress_increment
        if self.progress["floor"] > 100:
            self.progress["floor"] = 100

        # apply agent effects
        agent.stamina -= stamina_cost
        agent.experience += 1

        # log action
        self.history.append(
            f"{agent.username} moved wood "
            f"(+{progress_increment} floor, -{stamina_cost} stamina)"
        )
    
    def cut_wood(self,agent):
        progress_increment = agent.tool_skills
        stamina_cost = 2

        self.progress["floor"] += progress_increment
        if self.progress["floor"] > 100:
            self.progress["floor"]=100

        agent.stamina -= stamina_cost
        agent.experience += 1

        self.history.append(
            f"{agent.username} cut wood"
            f"(+{progress_increment} floor, -{stamina_cost} stamina)"
        )

    def layout_floor(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 4

        self.progress["floor"] += progress_increment
        if self.progress["floor"] > 100:
            self.progress["floor"]=100

        agent.stamina -= stamina_cost
        agent.experience += 2

        self.history.append(
            f"{agent.username} layout floor"
            f"(+{progress_increment} floor, -{stamina_cost} stamina)"
        )

    def frame_floor(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["floor"] += progress_increment
        if self.progress["floor"] > 100:
            self.progress["floor"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} frame floor"
            f"(+{progress_increment} floor, -{stamina_cost} stamina)"
        )
            
    def layout_walls(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["walls"] += progress_increment
        if self.progress["walls"] > 100:
            self.progress["walls"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} layout walls"
            f"(+{progress_increment} walls, -{stamina_cost} stamina)"
        )

    def frame_walls(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["walls"] += progress_increment
        if self.progress["walls"] > 100:
            self.progress["walls"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} frame walls"
            f"(+{progress_increment} walls, -{stamina_cost} stamina)"
        )

    def layout_floor2(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 4

        self.progress["floor2"] += progress_increment
        if self.progress["floor2"] > 100:
            self.progress["floor2"]=100

        agent.stamina -= stamina_cost
        agent.experience += 2

        self.history.append(
            f"{agent.username} layout floor 2"
            f"(+{progress_increment} floor2, -{stamina_cost} stamina)"
        )
    

    def frame_floor2(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["floor2"] += progress_increment
        if self.progress["floor2"] > 100:
            self.progress["floor2"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} frame floor2"
            f"(+{progress_increment} floor2, -{stamina_cost} stamina)"
        )
    


    def layout_stairs(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["stairs"] += progress_increment
        if self.progress["stairs"] > 100:
            self.progress["stairs"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} layout stairs"
            f"(+{progress_increment} stairs, -{stamina_cost} stamina)"
        )


    def frame_stairs(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["stairs"] += progress_increment
        if self.progress["stairs"] > 100:
            self.progress["stairs"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} frame stairs"
            f"(+{progress_increment} stairs, -{stamina_cost} stamina)"
        )

    def layout_roof(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["roof"] += progress_increment
        if self.progress["roof"] > 100:
            self.progress["roof"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} layout roof"
            f"(+{progress_increment} roof, -{stamina_cost} stamina)"
        )

    def frame_roof(self,agent):
        progress_increment = agent.strength + agent.tool_skills
        stamina_cost = 5

        self.progress["roof"] += progress_increment
        if self.progress["roof"] > 100:
            self.progress["roof"]=100

        agent.stamina -= stamina_cost
        agent.experience += 3

        self.history.append(
            f"{agent.username} frame roof"
            f"(+{progress_increment} roof, -{stamina_cost} stamina)"
        )