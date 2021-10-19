from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from Email.working_area import attachment_module as attachment, find_file_module as find_file

root = Tk()
root.title("POTWIERDZENIE MEGA KAM")
root.geometry("340x220")

def popup(send_email):
    response = messagebox.showinfo("Potwierdzenie MEGAKAM", "Gratulacje! Wysłałeś potwierdzenie do księgowej.")
    label_popup = Label(root, text = response)
    label_popup.grid(row = 0, column = 0)
    return send_email

def button_zus_click():
    top = Toplevel()
    top.title("ZUS")
    top.geometry("270x200")

    label_first = Label(top, text = f"Czy chcesz wysłać ZUS \n {find_file.filename}?", \
                        font=  ('Helvetica', 10, 'bold'), pady = 30)
    label_password = Label(top, text = "Wpisz hasło do poczty -->")
    entry_password = Entry(top, width = 20)
    button_send = Button(top, text = "WYŚLIJ", font = 'bold', command = lambda: popup(attachment.send_email_zus \
                        (entry_password.get(), find_file.file_path)))
    label_first.grid(row = 0, column = 0, columnspan = 2)
    label_password.grid(row = 1, column = 0)
    entry_password.grid(row = 1, column = 1)
    button_send.grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 20)

def button_skarbowy_click():
    top = Toplevel()
    top.title("Urząd Skarbowy")
    top.geometry("270x200")

    label_first = Label(top, text="Czy chcesz wysłać Urząd Skarbowy \n pko_trans_details_20210822_094155 ?", \
                        font=('Helvetica', 10, 'bold'), pady=30)
    label_password = Label(top, text="Wpisz hasło do poczty -->")
    entry_password = Entry(top, width=20)
    try:
        button_send = Button(top, text="WYŚLIJ", font='bold', command=lambda: popup(attachment.send_email_skarbowy \
                        (entry_password.get(), find_file.file_path)))
    raise SMTPAuthenticationError(code, resp):
        print("złe haslo")
    label_first.grid(row=0, column=0, columnspan=2)
    label_password.grid(row=1, column=0)
    entry_password.grid(row=1, column=1)
    button_send.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

    zus_img = ImageTk.PhotoImage(Image.open(r'C:\Users\adamp\Downloads\zus.jpg'))
    skarbowy_img = ImageTk.PhotoImage(Image.open(r'C:\Users\adamp\Downloads\urzad_skarbowy.jpg'))

    label_up = Label(root, text = "Z JAKIEGO URZĘDU WYSYŁASZ POTWIERDZENIE?", pady = 30, font = ('Helvetica', 10, 'bold'))
    label_zus = Label(root, image = zus_img)
    label_skarbowy = Label(root, image = skarbowy_img)
    button_zus = Button(root, text = "Wybierz", height = 3, width = 15, padx = 14, command = button_zus_click)
    button_skarbowy = Button(root, text = "Wybierz", height = 3, width = 15, padx = 14, command = button_skarbowy_click)

    label_up.grid(row = 0, column = 0, columnspan = 2)
    label_zus.grid(row = 1, column = 1)
    label_skarbowy.grid(row = 2, column = 1)
    button_zus.grid(row = 1, column = 0)
    button_skarbowy.grid(row = 2, column = 0)

#działanie programu

root.mainloop()