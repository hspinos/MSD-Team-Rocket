from tkinter import *

class Gui:
    def __init__(self):
       #define our window
        self.window = Tk()
        self.window.title("Hello world")
        self.window.geometry("1280x640")

        self.inputSent = False
        self.userInput = ""

        #define text box
        self.textBox = Text()


        #Start text from eliza
        self.elizaSays = "Fuck you"
        self.textBox.insert("1.0", "Eliza: " + str(self.elizaSays) + "\n")

        #User typing
        self.textBox.insert("2.0", "You: ")

        self.textBox.pack()
        # create send button
        Button(self.window, text="Send", width=20, command=self.getInput).pack(pady=20)

    def getInput(self):
        pos = self.textBox.index("end-1l+5c")
        self.userInput = self.textBox.get(pos, END)
        print(str(self.userInput))
        self.textBox.insert(END, "\n")
        self.inputSent = True



    def sendEliza(self):
        self.textBox.insert(END, "Eliza: " + self.elizaSays + "\n")
        self.textBox.insert(END, "You: ")
        self.inputSent = False

# if __name__ == '__main__':
#     gui = Gui()
#     gui.window.mainloop()


