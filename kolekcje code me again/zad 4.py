#pobierz od usera paczysta liczbe elementów, sprawdź czy sordkowe elemnety sa takie same

user = input("Podaj parzyst liczbę elementów, odzielonych przecinkiem: ")
user_list = user.split(",")
half_length = int(len(user_list) / 2)


if user_list[half_length -1] == user_list[half_length]:
    print("środkowe elementy są takie same")
else:
    print("środkowe elementy są różne")