# Do zmiennej quote przypisz zdanie:

quote = "Honesty is the first chapter in the book of wisdom."

#policz wzystkie znaki w napisie
number_of_signs = len(quote) #50

#Nie modyfikując zmiennej wyświetl słowo wisdom
print(quote[-7:-1])

#Wyswietl tylko pierwszą połowę tekstu
half_of_quote = int(number_of_signs/2)
print(quote[:half_of_quote])

#Wyswietl tylko kropkę
print(quote[-1])

#Wyswietl od połowy tylko co trzecią listerę cytatu
print(quote[half_of_quote::3])

#Wyświetl "Hnsyi h is hpe ntebo fwso"
print(quote[::2].replace(".", ""))
print(quote[:-1:2])

#Wyswietl cały cytat odwrtonie
print(quote[::-1])

#zamien wisdom na słowo friendship
print(quote.replace("wisdom", "friendship"))