import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GListBox_913=tk.Listbox(root)
        GListBox_913["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GListBox_913["font"] = ft
        GListBox_913["fg"] = "#333333"
        GListBox_913["justify"] = "center"
        GListBox_913.place(x=60,y=170,width=385,height=320)

        GButton_312=tk.Button(root)
        GButton_312["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        GButton_312["font"] = ft
        GButton_312["fg"] = "#000000"
        GButton_312["justify"] = "center"
        GButton_312["text"] = "🔎"
        GButton_312.place(x=420,y=100,width=30,height=30)
        GButton_312["command"] = self.GButton_312_command

        GLineEdit_287=tk.Entry(root)
        GLineEdit_287["anchor"] = "center"
        GLineEdit_287["borderwidth"] = "3px"
        GLineEdit_287["cursor"] = "arrow"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_287["font"] = ft
        GLineEdit_287["fg"] = "#999999"
        GLineEdit_287["justify"] = "left"
        GLineEdit_287["text"] = "Czego szukasz?"
        GLineEdit_287.place(x=60,y=100,width=350,height=30)

        GMessage_469=tk.Message(root)
        ft = tkFont.Font(family='Times',size=10)
        GMessage_469["font"] = ft
        GMessage_469["fg"] = "#333333"
        GMessage_469["justify"] = "left"
        GMessage_469["text"] = "Kategorie:"
        GMessage_469.place(x=60,y=140,width=80,height=25)

        GMessage_899=tk.Message(root)
        ft = tkFont.Font(family='Times',size=28)
        GMessage_899["font"] = ft
        GMessage_899["fg"] = "#333333"
        GMessage_899["justify"] = "center"
        GMessage_899["text"] = "OLX Searcher"
        GMessage_899.place(x=160,y=30,width=200,height=30)

    def GButton_312_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
