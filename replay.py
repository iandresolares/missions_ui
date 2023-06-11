class Replay:
    def __init__(self, tab, notifications):
        self.tab = tab
        self.notifications = notifications

    def start_replaying(self, mission_name: str):
        self.notifications.set("Starting replaying...")

    def cancel_replaying(self):
        self.notifications.set("Cancelling replaying...")

    def pause_replaying(self):
        self.notifications.set("pause replaying...")

    def resume_replaying(self):
        self.notifications.set("Resuming replaying...")
