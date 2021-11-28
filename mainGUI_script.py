import os
import tkinter as tk
from tkinter import StringVar, messagebox
from Email.tools import send_email, find_file
from PIL import ImageTk, Image

filename, filepath = find_file.find_attachment()
office1 = "ZUS"
office2 = "URZĄD SKARBOWY"

class Start_window:
    def __init__(self, master, office1, office2, filename, filepath, zus_img, skarbowy_img):
        self.master = master
        self.master.title("MENU GŁÓWNE")

        self.office1 = office1
        self.office2 = office2
        self.filename = filename
        self.filepath = filepath
        self.zus_img = zus_img
        self.skarbowy_img = skarbowy_img

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.info_label = tk.Label(
            self.frame,
            text = "WYBIERZ URZĄD",
            bg = "grey",
            fg = "white",
            font = ('Helvetica', 10, 'bold')
        )

        self.info_label.pack(
            ipadx = 100,
            pady = 10
        )

        self.zus_button = tk.Button(
            self.frame,
            image = zus_img,
            command = self.new_window_zus
        )

        self.zus_button.pack(
            side = 'top',
            pady = 10
        )

        self.skarbowy_button = tk.Button(
            self.frame,
            image = skarbowy_img,
            pady = 100,
            command = self.new_window_skarbowy
        )
        self.skarbowy_button.pack(
            side = 'bottom',
            pady = 10
        )

    def hide(self):
        self.master.withdraw()

    def new_window_zus(self):
        self.hide()
        new_window = tk.Toplevel()
        new_window.title("HASŁO")
        new_window.geometry("380x280")
        new_window.resizable(0,0)
        self.app = Password(new_window, self.filename, self.filepath, self.office1)

    def new_window_skarbowy(self):
        self.hide()
        new_window = tk.Toplevel()
        new_window.title("HASŁO")
        new_window.geometry("380x280")
        new_window.resizable(0,0)
        self.app = Password(new_window, self.filename, self.filepath, self.office2)


class Password:
    def __init__(self, master, filename, filepath, office):
        self.master = master
        self.filename = filename
        self.filepath = filepath
        self.office = office

        self.frame = tk.Frame(self.master)
        self.frame.pack()

        self.general_info_label = tk.Label(
            self.frame,
            text = f"WYSYŁASZ POTWIERDZENIE Z {office}",
            bg = "grey",
            fg = "white",
            font = ('Helvetica', 10, 'bold'),
            width = 45
        )

        self.general_info_label.grid(
            row = 0,
            column = 0,
            sticky = tk.N,
            columnspan = 3,
            pady = 15
        )

        self.file_info_label = tk.Label(
            self.frame,
            text = 'WYBRANY PLIK',
            bg = 'grey',
            fg = 'white',
            font = ('Helvetica', 10, 'bold'),
            width = 13
        )

        self.file_info_label.grid(
            row = 1,
            column = 0,
            sticky = tk.W,
            pady = 10,
            padx = 5
        )

        self.chosen_file_label = tk.Label(
            self.frame,
            text = self.filename,
        )

        self.chosen_file_label.grid(
            row = 1,
            column = 1,
            sticky = tk.W,
            pady = 10,
            padx = 5
        )

        self.email_info_label = tk.Label(
            self.frame,
            text = 'ODBIORCA',
            bg = 'grey',
            fg = 'white',
            font = ('Helvetica', 10, 'bold'),
            width = 13
        )

        self.email_info_label.grid(
            row = 2,
            column = 0,
            sticky = tk.W,
            pady = 10,
            padx = 5
        )

        clicked = StringVar()
        clicked.set("adam.pruszynski95@gmail.com")

        self.chosen_email_label = tk.OptionMenu(
            self.frame,
            clicked,
            "adam.pruszynski95@gmail.com",
            "geopawel90@gmail.com",
            "baska9@vp.pl"
        )

        self.chosen_email_label.config(width = 30)

        self.chosen_email_label.grid(
            row = 2,
            column = 1,
            sticky = tk.E,
            pady = 10
        )

        self.password_info_label = tk.Label(
            self.frame,
            text = "WPISZ HASŁO",
            bg = 'grey',
            fg = 'white',
            font = ('Helvetica', 10, 'bold'),
            width = 13
        )
        self.password_info_label.grid(
            row = 3,
            column = 0,
            sticky = tk.W,
            pady = 10,
            padx = 5
        )

        self.input_password_entry = tk.Entry(
            self.frame,
            width = 35
        )

        entered = StringVar()
        entered = self.input_password_entry

        self.input_password_entry.grid(
            row = 3,
            column = 1,
            sticky = tk.E,
            pady = 10,
            padx = 5
        )

        self.send_button = tk.Button(
            self.frame,
            text = "WYŚLIJ",
            font = ('Helvetica', 10, 'bold'),
            fg = "white",
            bg = "grey",
            command = lambda: self.popup(send_email.send_email(office, entered.get(), self.filepath, clicked.get())),
            height = 3,
            width = 20
        )

        self.send_button.grid(
            row = 4,
            columnspan = 2,
            pady = 15
        )

    def popup(self, send_function):
        if send_function == "error":
            response = messagebox.showerror("STATUS", "Nieprawidłowe hasło")
        else:
            response = messagebox.showinfo("STATUS", "Gratulacje! Wysłałeś potwierdzenie do księgowej.")

        status_label = tk.Label(text = response)
        status_label.pack()

        self.master.destroy()

        return send_function


def main():
    root = tk.Tk()
    root.title("MENU GŁÓWNE")

    zus_image = ImageTk.PhotoImage(Image.open(os.getcwd() + r'\photos\zus.jpg'))
    skarbowy_image = ImageTk.PhotoImage(Image.open(os.getcwd() + r'\photos\urzad_skarbowy.jpg'))

    app = Start_window(root, office1, office2, filename, filepath, zus_image, skarbowy_image)

    root.mainloop()


if __name__ == '__main__':
    main()