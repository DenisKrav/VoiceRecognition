import customtkinter
import voiceBot
from PIL import Image

def button_callback():
    textBox.delete("0.0", "end")
    textBox.insert("0.0", voiceBot.main())

app = customtkinter.CTk()
app.geometry("500x500")

textBox = customtkinter.CTkTextbox(app)
textBox.insert("0.0", "")
textBox.pack(padx=20, pady=20)

button_image = customtkinter.CTkImage(Image.open("microphone.png"), size=(26, 26))

button = customtkinter.CTkButton(app, text="", command=button_callback, image=button_image)
button.pack(padx=20, pady=20)

app.mainloop()