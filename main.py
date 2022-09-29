from quiz_logo import *
from multi_quiz import *

# En while loop som gör att man kan köra det flera gånger om man vill
running = True 
while running == True:
    print(logo)
    questions = int(input("Hur många frågor vill du svara på? "))
    print("Svara på frågorna med [1], [2] eller [3]")
    # Kallar på funktionen, med argumentet quiz (dvs vår dictionary)
    
    quizinator(quiz,questions)
    spela = input("\nVill du Quiza igen?! [J] / [N]?\n: ")
    if spela.lower() == "j":
        print(f"\nEn gång till!{stars}\n")  
        score = 0 # Nollställer score för nästa spelande
    else:
        print("Tack för att du spelade!")
        running = False # Ändrar condition för while-loopen, programmet avslutas