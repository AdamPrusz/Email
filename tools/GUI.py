import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from Email.tools import send_mail, find_file
filename, filepath = find_file.find_attachment()
send_mail.send_email("ZUS", 'jjtzifggelvlfbwq', filepath)

# class Office:
#     def __init__(self, name, file, path):
#         self.name = name
#         self.file = file
#         self.path = path
#
#     def click(self, popup_function):
#         top = Toplevel()
#         top.title("HASŁO")
#         top.geometry("270x200")
#
#         confirmation_label = Label(top, text=f"Czy chcesz wysłać potwierdzenie z {self.name}\n {self.file}?",
#                                    font=('Helvetica', 10, 'bold'), pady=30)
#         password_label = Label(top, text="Wpisz hasło do poczty -->")
#         password_entry = Entry(top, width=20)
#
#         confirmation_label.grid(row=0, column=0, columnspan=2)
#
#         password_label.grid(row=1, column=0)
#         password_entry.grid(row=1, column=1)
#         password = password_entry.get()
#
#         send_button = Button(top, text="WYŚLIJ", font='bold', command = lambda: popup_function(send_mail.send_email(self.name, password, self.path)))
#         send_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)
#
#
#
# def main():
#     root = Tk()
#     root.title("POTWIERDZENIE")
#     root.geometry("320x220")
#
#     zus_image = ImageTk.PhotoImage(Image.open(os.getcwd() + r'\photos\zus.jpg'))
#     skarbowy_image = ImageTk.PhotoImage(Image.open(os.getcwd() + r'\photos\urzad_skarbowy.jpg'))
#
#     def popup(send_function):
#         response = messagebox.showinfo("STATUS", "Gratulacje! Wysłałeś potwierdzenie do księgowej.")
#         popup_label = Label(root, text = response)
#         popup_label.grid(row=0, column=0)
#
#         return send_function
#
#
#     file_name, file_path = find_file.find_attachment()
#
#     zus = Office("ZUS", file_name, file_path)
#     zus_button = Button(root, image = zus_image, command= lambda: zus.click(popup))
#
#     skarbowy = Office("Urząd Skarbowy", file_name, file_path)
#     skarbowy_button = Button(root, image = skarbowy_image, command= lambda: skarbowy.click(popup))
#
#
#     choose_label = Label(root, text="Z JAKIEGO URZĘDU WYSYŁASZ POTWIERDZENIE?", pady = 30, font = ('Helvetica', 10, 'bold'))
#     choose_label.grid(row=0, column=0)
#     zus_button.grid(row=1, column=0)
#     skarbowy_button.grid(row=2, column=0)
#
#
#     root.mainloop()
#
# if __name__ == "__main__":
#     main()