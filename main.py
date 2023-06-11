from ttkbootstrap.constants import *
import ttkbootstrap as ttk
from tkinter import StringVar, IntVar, BooleanVar

from record import Record
from replay import Replay

# * Window
root = ttk.Window(themename="darkly")
root.title("Missions UI")
root.geometry("800x600")

notification_msg = StringVar()

notebook = ttk.Notebook(root)
# * Recording
recording_tab = ttk.Frame(notebook, relief="flat")

recording_tab.columnconfigure(0, weight=1)
recording_tab.columnconfigure(1, weight=2)


record = Record(recording_tab, notification_msg)

recording_title = ttk.Label(
    recording_tab, text="RECORD", font="Montserrat 15", bootstyle="white"
)
recording_title.grid(row=0, column=0, padx=10, pady=10)
# recording_title.pack()

separator = ttk.Separator(recording_tab)
separator.grid(row=1, column=0, sticky="ew")
# separator.pack(fill="x", padx=5, pady=5)


mission = StringVar()


entry = ttk.Entry(master=recording_tab, textvariable=mission, width=30)
# entry.pack(pady=10)
entry.grid(row=2, column=1, padx=10, pady=10)

mission_name_label = ttk.Label(recording_tab, text="Mission name", font="Montserrat 10")
mission_name_label.grid(row=1, column=1, padx=10)

start_recording_button = ttk.Button(
    recording_tab,
    text="Start recording",
    bootstyle=SUCCESS,
    command=lambda: record.start_recording(mission.get()),
)
start_recording_button.grid(row=2, column=0, padx=10, pady=10)
# start_recording_button.pack(pady=10)

separator = ttk.Separator(recording_tab)
separator.grid(row=3, column=0, sticky="ew")

# * waypoints variables
waypoint_name = StringVar()
waypoint_description = StringVar()
waypoint_time = IntVar()
waypoint_pose = BooleanVar(value=False)

waypoint_name_label = ttk.Label(
    recording_tab, text="Waypoint name", font="Montserrat 10"
)
waypoint_name_label.grid(row=3, column=1, padx=10)
waypoint_name_entry = ttk.Entry(
    master=recording_tab, textvariable=waypoint_name, width=30
)
waypoint_name_entry.grid(row=4, column=1, padx=10, pady=10)

waypoint_description_label = ttk.Label(
    recording_tab, text="Waypoint description", font="Montserrat 10"
)
waypoint_description_label.grid(row=5, column=1, padx=10)
waypoint_description_entry = ttk.Entry(
    master=recording_tab, textvariable=waypoint_description, width=30
)
waypoint_description_entry.grid(row=6, column=1, padx=10, pady=10)


waypoint_time_label = ttk.Label(
    recording_tab, text="Waypoint wait time", font="Montserrat 10"
)
waypoint_time_label.grid(row=3, column=2, padx=10)
waypoint_time_entry = ttk.Entry(
    master=recording_tab, textvariable=waypoint_time, width=10
)
waypoint_time_entry.grid(row=4, column=2, padx=10, pady=10)

waypoint_pose_label = ttk.Label(recording_tab, text="Save pose", font="Montserrat 10")
waypoint_pose_label.grid(row=5, column=2, padx=10)
waypoint_pose_check = ttk.Checkbutton(
    recording_tab,
    text="Pose",
    variable=waypoint_pose,
)
waypoint_pose_check.grid(row=6, column=2, padx=10, pady=10)


create_waypoint_button = ttk.Button(
    recording_tab,
    text="Create waypoint",
    bootstyle=INFO,
    command=lambda: record.create_waypoint(
        waypoint_name.get(),
        waypoint_description.get(),
        waypoint_time.get(),
        waypoint_pose.get(),
    ),
)
create_waypoint_button.grid(row=4, column=0, padx=10, pady=10)

separator = ttk.Separator(recording_tab)
separator.grid(row=7, column=0, sticky="ew")


save_recording_button = ttk.Button(
    recording_tab, text="Save recording", bootstyle=INFO, command=record.save_recording
)


cancel_recording_button = ttk.Button(
    recording_tab,
    text="Cancel recording",
    bootstyle=DANGER,
    command=record.cancel_recording,
)
cancel_recording_button.grid(row=8, column=0, padx=10, pady=10)


notifications = ttk.Label(
    root,
    text="Notifications",
    font="Montserrat 10",
    textvariable=notification_msg,
)
notifications.place(relx=1.0, rely=1.0, anchor="se")

# * Replaying
replaying_tab = ttk.Frame(notebook)

replay = Replay(replaying_tab, notification_msg)

replaying_title = ttk.Label(
    replaying_tab, text="REPLAY", font="Montserrat 15", bootstyle="white"
)
# replaying_title.pack()

# ttk.Separator(replaying_tab).pack(fill="x", padx=5, pady=5)

mission = StringVar()

start_replaying_button = ttk.Button(
    replaying_tab,
    text="Start replaying",
    bootstyle=SUCCESS,
    command=lambda: replay.start_replaying(mission.get()),
)
# start_replaying_button.pack(pady=10)

pause_replaying_button = ttk.Button(
    replaying_tab,
    text="Pause replaying",
    bootstyle=INFO,
    command=replay.pause_replaying,
)
# pause_replaying_button.pack(pady=10)

resume_replaying_button = ttk.Button(
    replaying_tab,
    text="Resume replaying",
    bootstyle=INFO,
    command=replay.resume_replaying,
)
# resume_replaying_button.pack(pady=10)

cancel_replaying_button = ttk.Button(
    replaying_tab,
    text="Cancel recording",
    bootstyle=DANGER,
    command=replay.cancel_replaying,
)
# cancel_replaying_button.pack(pady=10)

# pb1 = ttk.Progressbar(bootstyle="success")
# pb1.pack(side=LEFT, padx=5, pady=10)


# notifications = ttk.Label(
#     recording_tab,
#     text="Notifications",
#     font="Montserrat 10",
#     textvariable=notification_msg,
# )
# notifications.pack(side=BOTTOM)

notebook.add(recording_tab, text="Recording")
notebook.add(replaying_tab, text="Replaying")
# notebook.pack()
notebook.grid(row=0, column=0, sticky="nsew")

root.mainloop()
