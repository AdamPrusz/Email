# Utwórz skrypt, który zapyta uzytkownika o tytuł książki, nazwisko autora, liczbę stron, a następnie:
# - Sprawdź, czy tytuł i naziwsko składają się tylko z liter, natomiast liczba strona jest wartością liczbową
# - Uzytkownicy bywają leniwi. Nie zawsze zapisują tytuły i nazwisko z dużej litery - popraw ich
# - Połącz dane w jeden ciag  book za pomocą spacji
# - Policz lizbę wszystkich znaków w napisie book

user = input("Please gimme the book name, author and number of pages: ").split()
name, author, pages = user

if not name.isalpha():
    print("The name of the book should includes only letters, try again")
if not author.isalpha():
    print("The name of the author should includes only letters, try again")
if not pages.isdigit():
    print("The number of pages should includes only digits,try again")
else:
    print("Everything correct")

name = name.capitalize()
author = author.capitalize()

book = " ".join(user)
print(f"The number of signs in '{book}' is {len(book)}")
