from tkinter import *

f = open("Vocab/vocab_new.txt", "r")
wordlist = []
for line in f:
    wordlist.append(line.split('\n')[0])

print(wordlist[-1])
root = Tk()
text = Text(root)
text.insert(INSERT, wordlist[-1])
text.pack()
root.mainloop()
