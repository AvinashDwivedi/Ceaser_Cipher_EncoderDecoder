import tkinter as tk
from tkinter.constants import SUNKEN
from encode_decode import *

window=tk.Tk()
window.title('Caeser Cipherd')
frame=tk.Frame(master=window,bg="skyblue",padx=10)
frame.pack()
label1=tk.Label(frame,text="Enter Text: ", bg="skyblue").grid(row=1,column=1)
entry1=tk.Entry(master=frame,relief=SUNKEN,borderwidth=6,width=48)
entry1.grid(row=1,column=0,columnspan=6,ipady=4,pady=4)

label2=tk.Label(frame,text="Enter Key: ", bg="skyblue").grid(row=2,column=1)
entry2=tk.Entry(master=frame,relief=SUNKEN,borderwidth=6,width=48)
entry2.grid(row=2,column=0,columnspan=6,ipady=4,pady=4)

entry3=tk.Entry(master=frame,relief=SUNKEN,borderwidth=12,width=95)
entry3.grid(row=4,column=0,columnspan=6,ipady=4,pady=4)

def cipher():
    entry3.delete(0, tk.END)
    entry3.insert(tk.END, "The Caeser Cipher text after encoding: " + encode(str(entry1.get()), int(entry2.get())))

def real():
    entry3.delete(0, tk.END)
    entry3.insert(tk.END, "The Plain text after decoding: " + decode(str(entry1.get()), int(entry2.get())))
    
button_1=tk.Button(master=frame,text='Encode',padx=35,pady=10,width=6,command=cipher)
button_1.grid(row=3,column=2,pady=3)
button_2=tk.Button(master=frame,text='Decode',padx=35,pady=10,width=6,command=real)
button_2.grid(row=3,column=3,pady=3)

window.mainloop()