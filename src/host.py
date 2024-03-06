import requests
import random
from tkinter import Tk, Button

hard_coded_auth = "123123123x"


def send_roll():
    roll = random.randint(1, 20)
    headers = {"Authorization": hard_coded_auth}
    requests.post(
        "http://localhost:5000/set_roll", json={"roll": roll}, headers=headers
    )
    requests.post("http://localhost:5000/set_roll", json={"roll": roll})
    button.config(state="disabled")
    root.after(4000, lambda: button.config(state="normal"))


root = Tk()
root.title("Velutan Zar | Host")
button = Button(root, text="Bas Bana Dayı", command=send_roll, width=20, height=5)
button.pack()

root.mainloop()
