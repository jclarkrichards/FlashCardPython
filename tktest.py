from tkinter import *

class Example(Frame):
    def __init__(self, wordlist):
        super().__init__()
        self.wordindex = 0
        self.text = None
        self.wordlist = wordlist
        self.createUI()
        self.language = 0  #0 for english and 1 for polish
        
    def createUI(self):
        #print(wordlist[0])
        self.master.title('Flash Card App')
        self.pack(fill=BOTH, expand=True)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        
        label = Label(self, text="English", bg="white").grid(padx=10, pady=5, row=0, column=0, columnspan=3, sticky=W)
        self.text = Label(self, text=self.wordlist[self.wordindex], height=2, bg="yellow", font=("Helvetica", "20", "bold"))
        self.text.grid(padx=10, pady=5, row=1, column=0, columnspan=3, sticky=E+W+N+S)
        #self.text = Text(self, width=30, height=5, fg="red", font=('Helvetica', '20', 'bold'))
        #self.text.tag_configure("center", justify='center')
        #self.text.insert("1.0", "\n\n"+self.wordlist[self.wordindex])
        #self.text.tag_add("center", "1.0", "end")
        #self.text.grid(padx=10, pady=5, row=1, column=0, columnspan=3, sticky=(N, S, E, W))
        #print(type(self.text))
        
        button = Button(self, text="Flip", command=self.flip).grid(row=2, column=1, sticky=E+W, padx=5, pady=5)
        button2 = Button(self, text="NO", command=self.nextcard).grid(row=3, column=0, sticky=E+W, padx=5, pady=5)
        button3 = Button(self, text="YES", command=self.nextcard).grid(row=3, column=2, sticky=E+W, padx=5, pady=5)
    
    def flip(self):
        print("FLIP the card")


    def nextcard(self):
        print("Next card")
        self.wordindex += 1
        #print(dir(self.text))
        self.text.configure(text=self.wordlist[self.wordindex])
        #print(type(self.text))
        #self.text.replace("blahlsdfj")
        #print(self.text.get("1.0", END))
        #self.text.replace("1.0", END, self.text.get("1.0", END).replace("poop"))


def main():
    root = Tk()
    #root.geometry("350x300+300+300")
    f = open("Vocab/vocab_new.txt", "r", encoding='utf-8')
    wordlist = []
    for line in f:
        wordlist.append(line.split('\n')[0])
    
    app = Example(wordlist)
    root.mainloop()


if __name__ == '__main__':
    main()
