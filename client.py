from tkinter import Tk, Label, StringVar, PhotoImage
import requests

frameCnt = 24
frames = []
animation_id = None

def load_frames():
    global frames
    frames = [PhotoImage(file='dice.gif', format='gif -index %i' %(i)) for i in range(frameCnt)]

def update(ind):
    global animation_id
    frame = frames[ind]
    ind += 1
    if ind == frameCnt:
        ind = 0
    dice_label.configure(image=frame)
    animation_id = root.after(100, update, ind)

last_roll = 0
animating = False

def check_roll():
    global last_roll, animating
    response = requests.get('http://localhost:5000/get_roll')
    data = response.json()

    if response.status_code == 200:
        if last_roll != data['roll']:
            animating = True
            roll_number.set('Zar Atılıyor...\n ')
            root.after(0, update, 0)
            root.after(3000, stop_gif, data['roll']) 
            animating = False
    
    else:
        roll_number.set('Atılan Zar: \n0') 


    last_roll = data.get('roll')
    root.after(1000, check_roll)  

def stop_gif(roll):
    global animation_id
    if animation_id is not None:
        root.after_cancel(animation_id)
        animation_id = None
    dice_label.configure(image=frames[0]) 
    roll_number.set('Atılan Zar: \n' + str(roll))

root = Tk()
root.title("Velutan Zar")
load_frames() 
roll_number = StringVar()
roll_number.set('Atılan Zar: \n0')  
label = Label(root, textvariable=roll_number, font=("Helvetica", 24)) 
label.pack()

dice_label = Label(root, image=frames[0]) 
dice_label.pack()

check_roll()  
root.mainloop()