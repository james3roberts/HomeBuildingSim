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
            progress_key="floor",
            progress_increment=progress,
            stamina_cost=stamina,
            xp_gain=1
        )

    def cut_wood(self, agent):
        self._perform_action(
            agent,
            action_name="cut wood",
            progress_key="floor",
            progress_increment=agent.tool_skills,
            stamina_cost=2,
            xp_gain=1
        )

    def layout_floor(self, agent):
        self._perform_action(
            agent,
            action_name="laid out floor",
            progress_key="floor",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=4,
            xp_gain=2
        )

    def frame_floor(self, agent):
        self._perform_action(
            agent,
            action_name="framed floor",
            progress_key="floor",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def layout_walls(self, agent):
        self._perform_action(
            agent,
            action_name="laid out walls",
            progress_key="walls",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def frame_walls(self, agent):
        self._perform_action(
            agent,
            action_name="framed walls",
            progress_key="walls",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def layout_floor2(self, agent):
        self._perform_action(
            agent,
            action_name="laid out second floor",
            progress_key="floor2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=4,
            xp_gain=2
        )

    def frame_floor2(self, agent):
        self._perform_action(
            agent,
            action_name="framed second floor",
            progress_key="floor2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def layout_stairs(self, agent):
        self._perform_action(
            agent,
            action_name="laid out stairs",
            progress_key="stairs",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def frame_stairs(self, agent):
        self._perform_action(
            agent,
            action_name="framed stairs",
            progress_key="stairs",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def layout_roof(self, agent):
        self._perform_action(
            agent,
            action_name="laid out roof",
            progress_key="roof",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )

    def frame_roof(self, agent):
        self._perform_action(
            agent,
            action_name="framed roof",
            progress_key="roof",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3
        )
