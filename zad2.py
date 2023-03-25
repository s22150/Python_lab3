import random

miasta = ["Warszawa", "Kraków", "Łódź", "Wrocław", "Poznań", "Gdańsk", "Szczecin", "Bydgoszcz", "Lublin", "Katowice"]
plan_wycieczki = random.sample(miasta, 10)

for i in range(len(plan_wycieczki)):
    print(i+1,".", plan_wycieczki[i])