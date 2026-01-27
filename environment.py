class Environment:
    def __init__(self):
        self.active_tools = ["Muscles", "Nail Gun", "Saw", "Tape"]

        self.progress = {
            "wood_moved": 0,
            "wood_cut": 0,
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

        self.time_remaining = 10   # ✅ FIXED
        self.history = []

    # -------------------------
    # CORE ACTION ENGINE
    # -------------------------
    def _perform_action(
        self,
        agent,
        action_name,
        progress_key,
        progress_increment,
        stamina_cost,
        xp_gain
    ):
        if agent.stamina <= 0:
            self.history.append(f"{agent.username} is too exhausted to work.")
            return False

        if self.time_remaining <= 0:
            self.history.append("No time remaining.")
            return False

        # apply progress
        self.progress[progress_key] += progress_increment
        if self.progress[progress_key] > 100:
            self.progress[progress_key] = 100

        # apply agent effects
        agent.stamina -= stamina_cost
        agent.experience += xp_gain

        # consume time
        self.time_remaining -= 1

        # log
        self.history.append(
            f"{agent.username} {action_name} "
            f"(+{progress_increment} {progress_key}, -{stamina_cost} stamina)"
        )

        return True

    # -------------------------
    # ACTIONS
    # -------------------------
    def move_wood(self, agent):
        progress = agent.strength + agent.tool_skills
        stamina = max(1, 3 - (agent.strength // 2))

        self._perform_action(
            agent,
            action_name="moved wood",
            progress_key="wood_moved",
            progress_increment=progress,
            stamina_cost=stamina,
            xp_gain=1
        )

    def cut_wood(self, agent):
        if self.progress["wood_moved"] <75: #this number might need to change
            self.history.append (
            "Not enough wood moved to cut!"
            f"({self.progress['wood_moved']}/75)." #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="cut wood",
            progress_key="wood_cut",
            progress_increment=agent.tool_skills,
            stamina_cost=2,
            xp_gain=1
        )

    def layout_floor(self, agent):
        #build order rule
        if self.progress["wood_moved"] < 75:
            self.history.append(
                "Not enough wood moved to start floor layout!"
                f"({self.progress['wood_moved']}/75)."
            )
            return False
        
        return  self._perform_action(
            agent,
            action_name="laid out floor",
            progress_key="floor",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=4,
            xp_gain=2
        )

    def frame_floor(self, agent):
        if self.progress["floor"] <75: ##this number might need to change
            self.history.append(
                "Not enough layout completed to build floor"
                f"({self.progress['floor']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="framed floor",
            progress_key="floor",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def layout_walls(self, agent):
        if self.progress["floor"] <75: ##this number might need to change
            self.history.append(
                "Not enough floor completed to layout walls"
                f"({self.progress['floor']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="laid out walls",
            progress_key="walls",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def frame_walls(self, agent):
        if self.progress["walls"] <75: ##this number might need to change
            self.history.append(
                "Not enough layout completed to build walls"
                f"({self.progress['walls']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="framed walls",
            progress_key="walls",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def layout_floor2(self, agent):
        if self.progress["walls"] <75: ##this number might need to change
            self.history.append(
                "Not enough walls built to layout 2nd floor"
                f"({self.progress['walls']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="laid out second floor",
            progress_key="floor2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=4,
            xp_gain=2
        )

    def frame_floor2(self, agent):
        if self.progress["floor2"] <75: ##this number might need to change
            self.history.append(
                "Not enough layout completed to build 2nd floor"
                f"({self.progress['floor2']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="framed second floor",
            progress_key="floor2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def layout_stairs(self, agent):
        if self.progress["floor2"] <75: ##this number might need to change
            self.history.append(
                "Not enough floor finished to build stairs"
                f"({self.progress['floor2']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="laid out stairs",
            progress_key="stairs",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def frame_stairs(self, agent):
        if self.progress["stairs"] <75: ##this number might need to change
            self.history.append(
                "Not enough layout completed to build stairs"
                f"({self.progress['stairs']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="framed stairs",
            progress_key="stairs",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )


    def layout_walls2(self, agent):
        if self.progress["floor2"] <75: ##this number might need to change
            self.history.append(
                "Not enough floor completed to layout walls"
                f"({self.progress['floor2']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="laid out walls",
            progress_key="walls2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def frame_walls2(self, agent):
        if self.progress["walls2"] <75: ##this number might need to change
            self.history.append(
                "Not enough layout completed to build walls"
                f"({self.progress['walls2']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="framed walls",
            progress_key="walls2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )


    def layout_roof(self, agent):
        if self.progress["walls2"] <75: ##this number might need to change
            self.history.append(
                "Not enough layout completed to build walls"####
                f"({self.progress['walls2']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="laid out roof",
            progress_key="roof",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def frame_roof(self, agent):
        if self.progress["roof"] <75: ##this number might need to change
            self.history.append(
                "Not enough layout completed to build roof"
                f"({self.progress['roof']}/75)."    #this number might need to change
            )
            return False
        return self._perform_action(
            agent,
            action_name="framed roof",
            progress_key="roof",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )
    def rest (self, agent):
        recovered = 4
        
        #night life and recovery
        if agent.night_life ==1:
            recovered +=3
        elif recovered==3:
            recovered-=2
        if recovered <1:
            recovered=1
        
        agent.stamina += recovered
        self.time_remaining -= 1
        self.history.append(
            f"{agent.username}rested and recovered{recovered} stamina."
        )
        return True
## action area

    def get_available_actions(self, agent):
        actions = []

        if agent.stamina <=3:
            actions.append("rest")  #just added in step 1 

        if agent.stamina > 0 and self.time_remaining>0:
            actions.append("move_wood")

        if self.progress["wood_moved"]>=75:
            actions.append("cut_wood")
            actions.append("layout_floor")

        if self.progress["floor"]>=75:
            actions.append("frame_floor")
            actions.append("layout_walls")

        if self.progress["walls"] >= 75:
            actions.append("frame_walls")
            actions.append("layout_floor2")

        if self.progress["floor2"] >= 75:
            actions.append("frame_floor2")
            actions.append("layout_stairs")
            actions.append("layout_walls2")

        if self.progress["stairs"] >= 75:
            actions.append("frame_stairs")

        if self.progress["walls2"] >= 75:
            actions.append("layout_roof")

        if self.progress["roof"] >= 75:
            actions.append("frame_roof")

        return actions
        # -------------------------
    # ACTION EXECUTION
    # -------------------------
    def execute_action(self, agent, action_name):

        available = self.get_available_actions(agent)

        if action_name not in available:
            self.history.append(
                f"INVALID ACTION: {action_name}"
            )
            return False

        action_fn = getattr(self, action_name, None)

        if not action_fn:
            self.history.append(
                f"UNKNOWN ACTION: {action_name}"
            )
            return False
        #is this where I add the code from step 2
        return action_fn(agent)
    
    