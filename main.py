import os
import random
import tkinter

import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.geometry("500x300")
        self.resizable(0, 0)
        self.title("Password Generator")
        self.iconphoto(False, tkinter.PhotoImage(file=os.path.join("icon", "icon.png")))

        self.password_length = tkinter.StringVar(self, f"Password Length (16)")
        self.lowercase_var = tkinter.StringVar(self, "on")
        self.uppercase_var = tkinter.StringVar(self, "on")
        self.numbers_var = tkinter.StringVar(self, "on")
        self.symbols_var = tkinter.StringVar(self, "off")
        self.ambiguous_characters_var = tkinter.StringVar(self, "off")
        self.exclude_similar_characters = tkinter.StringVar(self, "off")
        self.password = tkinter.StringVar(self, "")

        self.top_frame = customtkinter.CTkFrame(master=self)
        self.top_frame.place(anchor="n", x=250, y=10, w=480, h=70)

        self.password_length_label = customtkinter.CTkLabel(master=self.top_frame, textvariable=self.password_length)
        self.password_length_label.place(anchor="n", x=240, y=10)

        self.password_slider = customtkinter.CTkSlider(master=self.top_frame, from_=8, to=24,
                                                       command=lambda length: self.password_length.set(f"Password length ({round(length)})"))
        self.password_slider.place(anchor="n", x=240, y=40, w=460, h=20)
        self.password_slider.set(16)

        self.middle_frame = customtkinter.CTkFrame(master=self)
        self.middle_frame.place(anchor="center", x=250, y=150, w=480, h=120)

        self.lowercase_checkbox = customtkinter.CTkCheckBox(master=self.middle_frame, text="Lowercase (abcde)",
                                                            variable=self.lowercase_var, onvalue="on", offvalue="off")
        self.lowercase_checkbox.place(anchor="nw", x=10, y=10)

        self.uppercase_checkbox = customtkinter.CTkCheckBox(master=self.middle_frame, text="Uppercase (ABCDE)",
                                                            variable=self.uppercase_var, onvalue="on", offvalue="off")
        self.uppercase_checkbox.place(anchor="w", x=10, y=60)

        self.uppercase_checkbox = customtkinter.CTkCheckBox(master=self.middle_frame, text="Numbers (12345)",
                                                           variable=self.numbers_var, onvalue="on", offvalue="off")
        self.uppercase_checkbox.place(anchor="sw", x=10, y=110)

        self.lowercase_checkbox = customtkinter.CTkCheckBox(master=self.middle_frame, text="Symbols (!@#$%&*?+=)",
                                                           variable=self.symbols_var, onvalue="on", offvalue="off")
        self.lowercase_checkbox.place(anchor="nw", x=200, y=10)

        self.uppercase_checkbox = customtkinter.CTkCheckBox(master=self.middle_frame,
                                                           text="Ambiguous Characters (^`'\":;/\\<>(){}[]~.,)",
                                                           variable=self.ambiguous_characters_var, onvalue="on",
                                                           offvalue="off")
        self.uppercase_checkbox.place(anchor="w", x=200, y=60)

        self.uppercase_checkbox = customtkinter.CTkCheckBox(master=self.middle_frame,
                                                           text="Exclude Similar Characters (0,o,1,l,L,i,I)",
                                                           variable=self.exclude_similar_characters, onvalue="on",
                                                           offvalue="off")
        self.uppercase_checkbox.place(anchor="sw", x=200, y=110)

        self.bottom_frame = customtkinter.CTkFrame(master=self)
        self.bottom_frame.place(anchor="s", x=250, y=290, w=480, h=70)

        self.generate_button = customtkinter.CTkButton(master=self.bottom_frame, text="Generate",
                                                       command=self.generate_password)
        self.generate_button.place(anchor="w", x=10, y=35, w=225, h=50)

        self.password_frame = customtkinter.CTkFrame(master=self.bottom_frame)
        self.password_frame.place(anchor="e", x=470, y=35, w=225, h=50)

        def set_clipboard(password):
            self.clipboard_clear()
            self.clipboard_append(password)
            self.password.set("Copied")

        self.password_box = customtkinter.CTkButton(master=self.password_frame, textvariable=self.password, command=lambda: set_clipboard(self.password.get()))
        self.password_box.place(anchor="center", x=112.5, y=25)

    def generate_password(self):
        password = ""
        password_characters = ""

        if self.lowercase_var.get() == "on":
            password_characters += "abcdefghijklmnopqrstuvwxyz"

        if self.uppercase_var.get() == "on":
            password_characters += "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        if self.numbers_var.get() == "on":
            password_characters += "1234567890"

        if self.symbols_var.get() == "on":
            password_characters += "!@#$%&*?+="

        if self.ambiguous_characters_var.get() == "on":
            password_characters += "^`'\":;/\\<>(){}[]~.,"

        similar_character_list = ["0", "1", "l", "L", "i", "I","o", "O"]
        if self.exclude_similar_characters.get() == "on":
            for similar_character in similar_character_list:
                password_characters = password_characters.replace(similar_character, "")

        for _ in range(int(self.password_length.get()[17:-1])):
            try:
                password += random.choice(password_characters)
            except:
                password = "error: invalid selection"

        self.password.set(password)


def main():
    app = App()
    app.mainloop()


if __name__ == "__main__":
    main()
