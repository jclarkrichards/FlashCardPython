from tkinter import *

f = open("Vocab/vocab_new.txt", "r")
wordlist = []
for line in f:
    wordlist.append(line.split('\n')[0])

print(wordlist[0])
root = Tk()
text = Text(root)
text.insert(INSERT, wordlist[0])
text.pack()
root.mainloop()
