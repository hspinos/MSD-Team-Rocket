#MSD-Team-Rocket_psg.py
import tkinter as tk
from turtle import color
root = tk.Tk()
root.title("Eliza")
root.geometry("700x650")
frame = tk.Frame(root, bg='lightblue')
frame.pack(fill='both', expand='yes')

def answer1():
    """ What to do with the answer in the entry box"""
    # This is the second question
    if e1.get () == str ("im sad"):
        T2.replace (1.0, tk.END, "I am sorry to hear that you are sad.\n" 
                                 "Can I provide some material to help you with your sadness?\n")
    elif e1.get () == str ("im happy"):
        T2.replace (1.0, tk.END, "I am glad to hear that you are happy.\n"
                                 "Can I provide some material to help you with your happiness?\n")

def answer2():
    """ What to do with the answer in the entry box"""
    #This is the response to the second entry box
    if e2.get()==str("yes"):
        T3.replace (1.0, tk.END, "Great!!! Would you prefer Movies, Videos, or Books?")
    elif e2.get()==str("no"):
        T3.replace (1.0, tk.END, "Okay then. Have a great day!")

def answer3():
    """ What to do with the answer in the entry box"""
    #This is the response to the third entry box
    if e3.get() == str ("movies"): 
        T4.replace (1.0, tk.END, "Here are some movies: ")
    elif e3.get() == str ("videos"):
        T4.replace (1.0, tk.END, "Here are some videos: ")
    elif e3.get() == str ("books"):
        T4.replace (1.0, tk.END, "Here are some books: ")


 
#This is the first Question
T1= tk.Text(frame, height=6, width=45)
T1.pack(pady=5)
T1.insert(tk.END, "How do you do. Please tell me your problem.\n")
T1.configure(fg='black', bg='white')

#Make an entry box to answer the question in
e1 = tk.Entry(master=frame, fg='black', bg='lightgray', width=37)
e1.pack(pady=5)

#Make a Send button to send the answer from the entry box to the definition of answer1
send = tk.Button(frame, text="Send", command=answer1)
send.pack()

T2 = tk.Text(frame, height=6, width=45)
T2.pack(pady=5)
T2.insert(tk.END, "")
T2.configure(fg='black', bg='white')

#Make an entry box to answer the question in
e2 = tk.Entry(master=frame, fg='black', bg='lightgray', width=37)
e2.pack(pady=5)

send2 = tk.Button(frame, text="Send", command=answer2)
send2.pack()

T3 = tk.Text(frame, height=6, width=45)
T3.pack(pady=5)
T3.insert(tk.END, "")
T3.configure(fg='black', bg='white')

e3 = tk.Entry(master=frame, fg='black', bg='lightgray', width=37)
e3.pack(pady=5)

send3 = tk.Button(frame, text="Send", command=answer3)
send3.pack()

T4 = tk.Text(frame, height=12, width=45)
T4.pack(pady=5)
T4.insert(tk.END, "")
T4.configure(fg='black', bg='white')


root.mainloop()
