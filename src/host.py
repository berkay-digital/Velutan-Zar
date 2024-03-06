import requests
import random
from tkinter import Tk, Button
import json

auth = json.load(open("./server.json")).get("auth")
host = json.load(open("./server.json")).get("host")

def send_roll():
    roll = random.randint(1, 20)
    headers = {"Authorization": auth}
    requests.post(
        f"http://{host}/set_roll", json={"roll": roll}, headers=headers
    )
    requests.post(f"http://{host}/set_roll", json={"roll": roll})
    button.config(state="disabled")
    root.after(4000, lambda: button.config(state="normal"))


root = Tk()
root.title("Velutan Zar | Host")
button = Button(root, text="Bas Bana Dayı", command=send_roll, width=20, height=5)
button.pack()

root.mainloop()
