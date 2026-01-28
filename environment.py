import random


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
            "stairs": 0,
        }

        self.hazards = ["Rain", "Cold", "Hot", "Snow", "Hail", "Wind"]

        self.challenges = [
            "material_distance",
            "material_elevation",
            "material_weight",
            "material_amount",
        ]

        self.time_remaining = 10
        self.history = []

        self.current_hazard = None
        self.hazard_duration = 0

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
        xp_gain,
    ):

        if agent.stamina <= 0:
            self.history.append(f"{agent.username} is too exhausted to work.")
            return False

        if self.time_remaining <= 0:
            self.history.append("No time remaining.")
            return False

        # -------------------------
        # WEATHER MODIFIERS
        # -------------------------

        progress_multiplier = 1.0
        extra_stamina = 0

        if self.current_hazard == "Rain":
            progress_multiplier = 0.8
        elif self.current_hazard == "Hot":
            extra_stamina = 1
        elif self.current_hazard == "Cold":
            extra_stamina = 1
        elif self.current_hazard == "Wind":
            progress_multiplier = 0.9
        elif self.current_hazard == "Snow":
            progress_multiplier = 0.7
        elif self.current_hazard == "Hail":
            progress_multiplier = 0.6

        # -------------------------
        # APPLY RESULTS
        # -------------------------

        adjusted_progress = int(progress_increment * progress_multiplier)

        self.progress[progress_key] += adjusted_progress
        self.progress[progress_key] = min(self.progress[progress_key], 100)

        agent.stamina -= stamina_cost + extra_stamina
        agent.experience += xp_gain

        self.time_remaining -= 1

        log = (
            f"{agent.username} {action_name} "
            f"(+{adjusted_progress} {progress_key}, "
            f"-{stamina_cost + extra_stamina} stamina)"
        )

        if self.current_hazard:
            log += f" [{self.current_hazard}]"

        self.history.append(log)

        return True

    # -------------------------
    # ACTIONS
    # -------------------------

    def move_wood(self, agent):
        progress = agent.strength + agent.tool_skills
        stamina = max(1, 3 - (agent.strength // 2))

        return self._perform_action(
            agent,
            action_name="moved wood",
            progress_key="wood_moved",
            progress_increment=progress,
            stamina_cost=stamina,
            xp_gain=1,
        )

    def cut_wood(self, agent):
        if self.progress["wood_moved"] < 75:
            self.history.append(
                "Not enough wood moved to cut! "
                f"({self.progress['wood_moved']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="cut wood",
            progress_key="wood_cut",
            progress_increment=agent.tool_skills,
            stamina_cost=2,
            xp_gain=1,
        )

    def layout_floor(self, agent):
        if self.progress["wood_moved"] < 75:
            self.history.append(
                "Not enough wood moved to start floor layout! "
                f"({self.progress['wood_moved']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="laid out floor",
            progress_key="floor",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=4,
            xp_gain=2,
        )

    def frame_floor(self, agent):
        if self.progress["floor"] < 75:
            self.history.append(
                "Not enough layout completed to build floor "
                f"({self.progress['floor']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="framed floor",
            progress_key="floor",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def layout_walls(self, agent):
        if self.progress["floor"] < 75:
            self.history.append(
                "Not enough floor completed to layout walls "
                f"({self.progress['floor']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="laid out walls",
            progress_key="walls",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def frame_walls(self, agent):
        if self.progress["walls"] < 75:
            self.history.append(
                "Not enough layout completed to build walls "
                f"({self.progress['walls']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="framed walls",
            progress_key="walls",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def layout_floor2(self, agent):
        if self.progress["walls"] < 75:
            self.history.append(
                "Not enough walls built to layout 2nd floor "
                f"({self.progress['walls']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="laid out second floor",
            progress_key="floor2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=4,
            xp_gain=2,
        )

    def frame_floor2(self, agent):
        if self.progress["floor2"] < 75:
            self.history.append(
                "Not enough layout completed to build 2nd floor "
                f"({self.progress['floor2']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="framed second floor",
            progress_key="floor2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def layout_stairs(self, agent):
        if self.progress["floor2"] < 75:
            self.history.append(
                "Not enough floor finished to build stairs "
                f"({self.progress['floor2']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="laid out stairs",
            progress_key="stairs",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def frame_stairs(self, agent):
        if self.progress["stairs"] < 75:
            self.history.append(
                "Not enough layout completed to build stairs "
                f"({self.progress['stairs']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="framed stairs",
            progress_key="stairs",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def layout_walls2(self, agent):
        if self.progress["floor2"] < 75:
            self.history.append(
                "Not enough floor completed to layout walls "
                f"({self.progress['floor2']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="laid out walls",
            progress_key="walls2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def frame_walls2(self, agent):
        if self.progress["walls2"] < 75:
            self.history.append(
                "Not enough layout completed to build walls "
                f"({self.progress['walls2']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="framed walls",
            progress_key="walls2",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def layout_roof(self, agent):
        if self.progress["walls2"] < 75:
            self.history.append(
                "Not enough layout completed to build roof "
                f"({self.progress['walls2']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="laid out roof",
            progress_key="roof",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def frame_roof(self, agent):
        if self.progress["roof"] < 75:
            self.history.append(
                "Not enough layout completed to build roof "
                f"({self.progress['roof']}/75)."
            )
            return False

        return self._perform_action(
            agent,
            action_name="framed roof",
            progress_key="roof",
            progress_increment=agent.strength + agent.tool_skills,
            stamina_cost=5,
            xp_gain=3,
        )

    def rest(self, agent):
        recovered = 4

        if agent.night_life == 1:
            recovered += 3

        if recovered < 1:
            recovered = 1

        agent.stamina += recovered
        self.time_remaining -= 1

        self.history.append(
            f"{agent.username} rested and recovered {recovered} stamina."
        )

        return True

    # -------------------------
    # WEATHER SYSTEM
    # -------------------------

    def roll_hazard(self):

        if self.hazard_duration > 0:
            self.hazard_duration -= 1

            if self.hazard_duration == 0:
                self.history.append(f"Weather cleared: {self.current_hazard}")
                self.current_hazard = None

            return

        if random.random() < 0.35:
            self.current_hazard = random.choice(self.hazards)
            self.hazard_duration = random.randint(1, 3)

            self.history.append(
                f"Weather hazard started: {self.current_hazard}"
            )

    # -------------------------
    # ACTION SELECTION
    # -------------------------

    def get_available_actions(self, agent):

        actions = []

        if agent.stamina <= 3:
            actions.append("rest")

        if agent.stamina > 0 and self.time_remaining > 0:
            actions.append("move_wood")

        if self.progress["wood_moved"] >= 75:
            actions += ["cut_wood", "layout_floor"]

        if self.progress["floor"] >= 75:
            actions += ["frame_floor", "layout_walls"]

        if self.progress["walls"] >= 75:
            actions += ["frame_walls", "layout_floor2"]

        if self.progress["floor2"] >= 75:
            actions += ["frame_floor2", "layout_stairs", "layout_walls2"]

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

        self.roll_hazard()

        if action_name not in available:
            self.history.append(f"INVALID ACTION: {action_name}")
            return False

        action_fn = getattr(self, action_name, None)

        if not action_fn:
            self.history.append(f"UNKNOWN ACTION: {action_name}")
            return False

        return action_fn(agent)
