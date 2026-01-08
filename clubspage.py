from pyscript import document, display

club_list = ["robots", "science", "arts", "sports"]

info_list = [
    "Robotics Club: Programming and robots in the Computer Lab. Led by Mr. Santiago from 7:00 AM to 9:00 AM.",
    "Science Club: Experiments and discoveries in the Science Lab. Led by Ms. Del Rosario from 9:30 PM to 10:00 PM",
    "Arts Club: Painting, drawing, and creativity in the Art Room. Led by Mr. Smith from 10:00 AM to 10:30 AM",
    "Sports Club: Training and games in the Gym. Led by Mr. Layug from 3:00 PM to 5:00 PM"
]

def show_info(event):
    choice = document.querySelector("#club").value

    if choice in club_list:
        i = club_list.index(choice)
        result = info_list[i]   

        display(result, target="info")
