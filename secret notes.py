import tkinter

window = tkinter.Tk()
window.title("Secret Notes")
window.geometry("350x570")

original_image = tkinter.PhotoImage(file="output.png")
resized_image = original_image.subsample(5, 5)
label_1 = tkinter.Label(window, image=resized_image, compound="top" )
label_1.pack()


label_2 = tkinter.Label(window, text='Enter Your Title', compound="top")
label_2.config(pady=10)
label_2.pack()

entry_1 = tkinter.Entry(window)
entry_1.pack()

label_3 = tkinter.Label(window, text='Enter Your Secret', compound="top")
label_3.config(pady=10)
label_3.pack()

text_1 = tkinter.Text(window, height=10, width=35)
text_1.pack()

label_4 = tkinter.Label(window, text='Enter Master Key', compound="top")
label_4.config(pady=10)
label_4.pack()

entry_2 = tkinter.Entry(window)
entry_2.pack()


button_1 = tkinter.Button(window, text="Save and Encrypt", command=window.destroy)
button_1.pack()

button_2 = tkinter.Button(window, text="Decrypt", command=window.destroy)
button_2.pack()



















window.mainloop()