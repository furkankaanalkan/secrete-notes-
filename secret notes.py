import tkinter
from cryptography.fernet import Fernet
import hashlib
import base64


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


def encrypt_and_save_to_file():
    message = text_1.get("1.0", "end")

    password = entry_2.get().encode()
    digest = hashlib.sha256(password).digest()
    my_key = base64.urlsafe_b64encode(digest)

    fernet = Fernet(my_key)
    encrypted_message =fernet.encrypt(message.encode())
    decrypted_message = fernet.decrypt(encrypted_message).decode()
    title = '\n' + entry_1.get() + '\n'
    with open("secret notes.txt",mode="a") as file:
        file.write(title)

    with open("secret notes.txt",mode="a") as file:
        file.write(str(encrypted_message))
    label_5.config(text="Secret Notes saved to file")

def decrypt_system():
    try :
        saved_message = bytes(text_1.get("1.1", "end"), "utf-8")

        password = entry_2.get().encode()
        digest = hashlib.sha256(password).digest()
        last_key = base64.urlsafe_b64encode(digest)

        saved_message_key = Fernet(last_key)
        decrypted_message = saved_message_key.decrypt(saved_message).decode()

        text_1.delete("1.0", "end")
        text_1.insert("1.0", decrypted_message)
    except :
        label_5.config(text="your password is incorrect")


button_1 = tkinter.Button(window, text="Save and Encrypt", command=encrypt_and_save_to_file )
button_1.pack()

button_2 = tkinter.Button(window, text="Decrypt", command=decrypt_system)
button_2.pack()

label_5 = tkinter.Label(window)
label_5.pack()


window.mainloop()