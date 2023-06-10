from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import StringVar, IntVar, BooleanVar


# * Show missions list: initial fiducial, description
def start_recording(mission_name: str):
    if mission_name.startswith("mission_"):
        notifications["style"] = "success.TLabel"
        notification_msg.set("Mission name is valid")
    elif mission_name.startswith("map_"):
        notification_msg.set("Map name is valid")
        notifications["style"] = "success.TLabel"
    else:
        notification_msg.set("Invalid mission or map name")
        notifications["style"] = "danger.TLabel"


def cancel_recording():
    notification_msg.set("cancelling recording...")


def create_waypoint(name: str, description: str, time: int, pose: bool):
    notification_msg.set(
        f"Creating waypoint {name} with description {description} at time {time} with pose {pose}"
    )


def save_recording():
    notification_msg.set("Saving recording...")


root = ttk.Window(themename="darkly")
root.title("Missions UI")
root.geometry("800x600")

notification_msg = StringVar()

t1 = ttk.Label(root, text="RECORD", font="Montserrat 15", bootstyle="white")
t1.pack()

ttk.Separator(root).pack(fill="x", padx=5, pady=5)


mission = StringVar()
entry = ttk.Entry(master=root, textvariable=mission, width=30)
entry.pack(pady=10)

start_recording_button = ttk.Button(
    root,
    text="Start recording",
    bootstyle=SUCCESS,
    command=lambda: start_recording(mission.get()),
)
start_recording_button.pack(pady=10)

# * waypoints variables
waypoint_name = StringVar()
waypoint_description = StringVar()
waypoint_time = IntVar()
waypoint_pose = BooleanVar(value=False)

waypoint_name_entry = ttk.Entry(master=root, textvariable=waypoint_name, width=30)
waypoint_name_entry.pack(pady=10)
waypoint_description_entry = ttk.Entry(
    master=root, textvariable=waypoint_description, width=50
)
waypoint_description_entry.pack(pady=10)
waypoint_time_entry = ttk.Entry(master=root, textvariable=waypoint_time, width=10)
waypoint_time_entry.pack(pady=10)
waypoint_pose_check = ttk.Checkbutton(
    root,
    text="Save pose",
    variable=waypoint_pose,
)
waypoint_pose_check.pack()

create_waypoint_button = ttk.Button(
    root,
    text="Create waypoint",
    bootstyle=INFO,
    command=lambda: create_waypoint(
        waypoint_name.get(),
        waypoint_description.get(),
        waypoint_time.get(),
        waypoint_pose.get(),
    ),
)
create_waypoint_button.pack(pady=10)

save_recording_button = ttk.Button(
    root, text="Save recording", bootstyle=INFO, command=save_recording
)
save_recording_button.pack(pady=10)

# pb1 = ttk.Progressbar(bootstyle="success")
# pb1.pack(side=LEFT, padx=5, pady=10)


cancel_recording_button = ttk.Button(
    root, text="Cancel recording", bootstyle=DANGER, command=cancel_recording
)
cancel_recording_button.pack(pady=10)


notifications = ttk.Label(
    root,
    text="Notifications",
    font="Montserrat 10",
    textvariable=notification_msg,
)
notifications.pack(side=BOTTOM)

root.mainloop()
