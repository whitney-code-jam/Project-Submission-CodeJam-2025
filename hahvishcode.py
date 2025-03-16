
import tkinter as tk
from PIL import Image, ImageTk
import datetime as dt


statue=False
#root window
root=tk.Tk()
ButtonsRemaining=4
TimeforExercise="5-20"
root.title("What Exercise Should You Do")
root.geometry('1000x300')

image_path = "/Users/aarav/Downloads/healthbg copy.jpeg"
image = Image.open(image_path)
image=image.resize((root.winfo_screenwidth(),root.winfo_screenheight()),Image.LANCZOS) 
photo_image=ImageTk.PhotoImage(image)
background_label=tk.Label(root, image=photo_image)
background_label.place(x=0,y=0, relwidth=1,relheight=1)
background_label.image=photo_image

Running=0
Cycling=0
Swimming=0
Push=0
Squats=0
Deadlifts=0
Jump=0
Yoga=0
Bench=0
Rowing=0
Burpees=0
Pull=0
Walking=0
Plank=0
Box=0
Kettlebell=0
Elliptical=0
Zumba=0
Rock=0
Pilates=0
HIIT=0
Lunges=0
Treadmill=0
Bench=0
Dancing=0
Mountain=0
Stretching=0
Hiking=0

exercises = ["Running",
    "Cycling",
    "Swimming",
    "Push",
    "Squats",
    "Deadlifts",
    "Jump",
    "Yoga",
    "Bench",
    "Rowing",
    "Burpees",
    "Pull",
    "Walking",
    "Plank",
    "Box",
    "Kettlebell",
    "Elliptical",
    "Zumba",
    "Rock",
    "Pilates",
    "HIIT",
    "Lunges",
    "Treadmill",
    "Bench",
    "Dancing",
    "Rowing",
    "Mountain",
    "Stretching",
    "Hiking"
]





ask = tk.Label(root,text = "How much time do you have to exercise?")
ask.grid()
ask2=tk.Label(root,text= "What muscle groups do you want to work out?")
ask2.grid()
ask3=tk.Label(root,text="Do you have gym equipment at your house?")
ask3.grid()
ask4=tk.Label(root,text="What intensity?")
ask4.grid()



def c1():
    ask.configure(text="Thank you!")
    b1.destroy()
    b2.destroy()
    b3.destroy()
    

b1 = tk.Button(root,text="5-20 min",fg="black", command=c1)
b2 = tk.Button(root,text="30 min",fg="black", command=c1)
b3 = tk.Button(root,text="60 min",fg="black", command=c1)

b1.grid(column=2,row=0)
b2.grid(column=3,row=0)
b3.grid(column=4,row=0)
ButtonsRemaining-=1


def c2():
    ask2.configure(text="Thank you!")
    
    b77.destroy()
    b88.destroy()
    b99.destroy()
    


b77 = tk.Button(root,text="Strength",fg="black", command=c2)
b88 = tk.Button(root,text="Cardio",fg="black", command=c2)
b99 = tk.Button(root,text="Flexibility",fg="black", command=c2)



b77.grid(column=2,row=1)
b88.grid(column=3,row=1)
b99.grid(column=4,row=1)
ButtonsRemaining-=1

def c3():
    ask3.configure(text="That's Great!")
    b4.destroy()
    b5.destroy()
    

b4 = tk.Button(root,text="Yes",fg="black", command=c3)
b5 = tk.Button(root,text="No",fg="black", command=c3)
ButtonsRemaining-=1


b4.grid(column=2,row=2)
b5.grid(column=3,row=2)

def c4():
    ask4.configure(text="We will use your answers and calculate the exercise best for you!")
    b111.destroy()
    b222.destroy()
    b333.destroy()
    
    
b111 = tk.Button(root,text="Low",fg="black", command=c4)
b222 = tk.Button(root,text="Medium",fg="black", command=c4)
b333 = tk.Button(root,text="High",fg="black", command=c4)

b111.grid(column=2,row=3)
b222.grid(column=3,row=3)
b333.grid(column=4,row=3)
ButtonsRemaining-=1


x="5-20 min"
y="legs"
z="no"
u="Low"
step_two = True
step_three = True

if c1 == b1:
    Push=1
    Squats=1
    Deadlifts=1
    Jump=1
    Bench=1
    Plank=1
    Box=1
    Kettlebell=1
    HIIT=1
    Lunges=1
    Bench=1
    Mountain=1
    Stretching=1
    Pull=1
elif c1 == b2:
    Running=1
    Cycling=1
    Swimming=1
    Rowing=1
    Walking=1
    Elliptical=1
    Rock=1
    Burpees=1
    Dancing =1
elif c1 == b3:
    Yoga=1
    Zumba=1
    Pilates=1
    Treadmill=1
    Hiking=1

if step_two == True:
    if c2 == b77:
        Push+=1
        Squats+=1
        Bench+=1
        Deadlifts+=1
        Pull+=1
        Plank+=1
        Box+=1
        Kettlebell+=1
        Rock+=1
        Lunges+=1
        Bench+=1
    elif c2 == b88:
        Yoga+=1
        Stretching+=1
        Pilates+=1
    elif y == b99:
        Jump+=1
        Treadmill+=1
        Hiking+=1
        Dancing+=1
        Mountain+=1
        HIIT+=1
        Elliptical+=1
        Zumba+=1
        Walking+=1
        Running+=1
        Cycling+=1
        Swimming+=1
        Burpees+=1
        Rowing+=1

if step_three == True:
    if c3 == b5:
        Running+=3
        Swimming+=3
        Push+=3
        Squats+=3
        Yoga+=3
        Burpees+=3
        Walking+=3
        Plank+=3
        Box+=3
        Zumba+=3
        Rock+=3
        Pilates+=3
        HIIT+=3
        Lunges+=3
        Dancing+=3
        Mountain+=3
        Stretching+=3
        Hiking+=3
        step_three=True

    elif c3==b4:
        Cycling+=3
        Deadlifts+=3
        Jump+=3
        Bench+=3
        Rowing+=3
        Pull+=3
        Kettlebell+=3
        Elliptical+=3
        Treadmill+=3
        Bench+=3

if step_three == True:
    if c4==b111:
        Running+=2
        Cycling+=2
        Jump+=2
        Walking +=2
        Elliptical+=2
        Pilates+=2
        Zumba+=2
        Lunges+=2
        Treadmill+=2
        Dancing+=2
        Stretching+=2
    elif c4==b222:
        Swimming+=2
        Squats+=2
        Hiking+=2
        Yoga+=2
        Bench+=2
        HIIT+=2
        Bench+=2
        Rowing+=2
        Burpees+=2
        Plank+=2
        Box+=2
        Kettlebell+=2
    elif c4==b333:
        Push+=2
        Mountain+=2
        Deadlifts+=2
        Pull+=2
        Rock+=2

h=0
ff=True
t= exercises[h]
if ff==True:
    h+=1

    dd= "Cycling"

    ee = tk.Label(root,text=dd)
    ee.grid()

root.mainloop()