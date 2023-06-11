class Record:
    def __init__(self, tab, notifications):
        self.tab = tab
        self.notifications = notifications

    def start_recording(self, mission_name: str):
        if mission_name.startswith("mission_"):
            self.notifications.set("Mission name is valid")
        elif mission_name.startswith("map_"):
            self.notifications.set("Map name is valid")
        else:
            self.notifications.set("Invalid mission or map name")

    def cancel_recording(self):
        self.notifications.set("cancelling recording...")

    def create_waypoint(self, name: str, description: str, time: int, pose: bool):
        self.notifications.set(
            f"Creating waypoint {name} with description {description} at time {time} with pose {pose}"
        )

    def save_recording(self):
        self.notifications.set("Saving recording...")
