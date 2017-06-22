import tkinter as tk
from genedb import cleanerfunc


class Application(tk.Frame):
    """Helps create panel and button with string cleaner function.

    creates button and text panel, with a string cleaning function connected to the button"""
    def __init__(self, master=None):
        tk.Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
    def createWidgets(self):
        self.clean=tk.Button(self, text="Clean Input",fg="green",command=(self.runStringCleaner))  
        self.inputText=tk.Text(self,height=20,width=100)
        self.clean.pack()
        self.inputText.pack()
    def runStringCleaner(self):
        String=cleanerfunc.removespecchar(self.inputText.get(1.0,tk.END))
        self.inputText.delete(1.0,tk.END)
        self.inputText.insert(tk.END,String)

root=tk.Tk()
app=Application(master=root)
app.mainloop()
