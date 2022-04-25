from tkinter import *

#define our window
window = Tk()
window.title("Hello world")
window.geometry("1280x640")

#define text box
textBox = Text()


#Start text from eliza
elizaSays = "Fuck you"
textBox.insert("1.0", "Eliza: " + str(elizaSays) + "\n")

#User typing
textBox.insert("2.0", "You: ")

def getInput():
    pos = textBox.index("end-1l+5c")
    userInput = textBox.get(pos, END)
    print(str(userInput))
    textBox.insert(END, "\n")
    textBox.insert("end", "Eliza: " + elizaSays + "\n")
    textBox.insert("end", "You: ")

textBox.pack()

#create send button
Button(window, text="Send", width=20, command=getInput).pack(pady=20)
window.mainloop()