import os
from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
from Email.tools import send_mail as mail, find_file as file

def main():

    def popup(send_file):
        response = messagebox.showinfo("Potwierdzenie MEGAKAM", "Gratulacje! Wysłałeś potwierdzenie do księgowej.")
        label_popup = Label(root, text = response)
        label_popup.grid(row = 0, column = 0)
        return send_file

    def button_zus_click(file):
        # os.chdir(filepath)





        top = Toplevel()
        top.title("ZUS")
        top.geometry("270x200")
        label_first = Label(top, text = f"Czy chcesz wysłać potwierdzenie z ZUSu \n {file}?",
                            font=  ('Helvetica', 10, 'bold'), pady = 30)

        label_password = Label(top, text = "Wpisz hasło do poczty -->")
        entry_password = Entry(top, width = 20)
        zus = mail.ZUS(entry_password.get())

        button_send = Button(top, text = "WYŚLIJ", font = 'bold', command = lambda: popup(zus.send_email_zus(file)))
        label_first.grid(row = 0, column = 0, columnspan = 2)
        label_password.grid(row = 1, column = 0)
        entry_password.grid(row = 1, column = 1)
        button_send.grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 20)



    # def button_skarbowy_click(file):
    #     os.chdir(download_path)
    #     top = Toplevel()
    #     top.title("Urząd Skarbowy")
    #     top.geometry("270x200")
    #     label_first = Label(top, text = f"Czy chcesz wysłać potwierdzenie z Urzędu Skarbowego \n {file}?",
    #                         font=  ('Helvetica', 10, 'bold'), pady = 30)
    #
    #     label_password = Label(top, text = "Wpisz hasło do poczty -->")
    #     entry_password = Entry(top, width = 20)
    #     password = entry_password.get()
    #     skarbowy = send_mail.Skarbowy(password)
    #
    #     button_send = Button(top, text = "WYŚLIJ", font = 'bold', command = lambda: popup(skarbowy.send_email_skarbowy(filename)))
    #     label_first.grid(row = 0, column = 0, columnspan = 2)
    #     label_password.grid(row = 1, column = 0)
    #     entry_password.grid(row = 1, column = 1)
    #     button_send.grid(row = 2, column = 0, columnspan = 2, padx = 20, pady = 20)


    root = Tk()
    root.title("POTWIERDZENIE MEGA-KAM")
    root.geometry("340x220")

    zus_img = ImageTk.PhotoImage(Image.open(os.getcwd() + r'\photos\zus.jpg'))
    # skarbowy_img = ImageTk.PhotoImage(Image.open(os.getcwd() + r'\photos\urzad_skarbowy.jpg'))

    label_up = Label(root, text="Z JAKIEGO URZĘDU WYSYŁASZ POTWIERDZENIE?", pady=30, font=('Helvetica', 10, 'bold'))

    label_zus = Label(root, image=zus_img)
    # label_skarbowy = Label(root, image=skarbowy_img)
    button_zus = Button(root, text="Wybierz", height=3, width=15, padx=14, command = lambda: button_zus_click(file.find_attachment()))
    # button_skarbowy = Button(root, text="Wybierz", height=3, width=15, padx=14, command = lambda: button_skarbowy_click(filename))

    label_up.grid(row=0, column=0, columnspan=2)
    label_zus.grid(row=1, column=1)
    # label_skarbowy.grid(row=2, column=1)
    button_zus.grid(row=1, column=0)
    # button_skarbowy.grid(row=2, column=0)


    root.mainloop()


main()