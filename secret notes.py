import tkinter
from cryptography.fernet import Fernet

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




#print("original string: ", message)
#print("encrypted string: ", encrypted_message)
#my_key = Fernet.generate_key(str(entry_2.get()))
#fernet = Fernet(my_key)
#decrypted_message = fernet.decrypt(encrypted_message)
#print("decrypted string: ", decrypted_message)
my_key = Fernet.generate_key()
fernet = Fernet(my_key)

#furkan = keyword.iskeyword(entry_2.get())
userkey =



def encrypt_and_save_to_file():
    message = text_1.get("1.0", "end")
    my_key = Fernet.generate_key()
    fernet = Fernet(my_key)
    encrypted_message =fernet.encrypt(message.encode())
    print(encrypted_message)

    title = '\n' + entry_1.get()
    with open("secret notes.txt",mode="a") as file:
        file.write(title)

    with open("secret notes.txt",mode="a") as file:
        file.write('\n' + str(encrypted_message) + '\n' + str(my_key))
    label_5.config(text=f"Secret Notes saved to file")


def decrypt_system():
    saved_message = text_1.get("1.0", "end")
    last_key = bytes(entry_2.get()[1:], "utf-8")
    saved_message_key = Fernet(last_key)
    decrypted_message = saved_message_key.decrypt(saved_message.decode())
    print(decrypted_message)



button_1 = tkinter.Button(window, text="Save and Encrypt", command=encrypt_and_save_to_file )
button_1.pack()

button_2 = tkinter.Button(window, text="Decrypt", command=decrypt_system)
button_2.pack()

label_5 = tkinter.Label(window)
label_5.pack()
















window.mainloop()