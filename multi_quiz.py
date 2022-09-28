# Själva quizet, en dict med index. Index = siffrorna innan, tror jag..
# Nu med MULTI-Q!

quiz = {
    1 :{
        "fråga" : "Vilket lag är bäst i Stockholm?\n1: Hammarby \n2: Djurgården \n3: AIK",
        "svar" : "1"
    },
    2 :{
        "fråga" : "Vad heter portugals huvudstad?\n1: Paris \n2: Lissabon  \n3: Göran",
        "svar" : "2"
    },
    3 :{
        "fråga" : "Vad kallas en sälunge?\n1: Bob \n2: Valp \n3: Kut",
        "svar" : "3"
    }
}

# Poäng räkning. måste kanske ligga i loop?
score = 0
# score += 1 , efter ett rätt svar

# Bara utsmyckning, för lite lättare text i funktionen
stars = "\n"+"*"*20 
stripes = "\n"+"=*"*10

# Det här printar nr 1 och nr 1s fråga, från dictionary
# print(quiz[1]['fråga'])

# Går igenom 1-3 index i dict, "frågor" är bara nummerna i dicten
# for frågor in quiz:
       # print(quiz[frågor]['fråga'])

# En funktion som går igenom vår dictionary med frågor
# Det printar frågor och alternativ, sen kollar mot svar.
# Stars/Stripes är bara utsmyckning
def quizinator(arg):
    global score 
    for frågor in arg:
        print(quiz[frågor]['fråga']+f"{stars}")
        svaret = input("\nSvar : ")
        if svaret == quiz[frågor]['svar']:
            print(f"Rätt Svar!\n{stars}")
            score +=1 # Varje rätt svar ger +1 till score variabeln
        else:
            print(f"FEL!\n{stars}")
    print(f"{stripes}\nDu fick {score}/3 rätt!{stripes}") # Printar score

# En while loop som gör att man kan köra det flera gånger om man vill
running = True # Condition för loopen, kan nog vara vad som helst
while running == True:
    # Lite intro bara
    print("\t-----QUIZTIME!-----")
    print("Svara på frågorna med [1], [2] eller [3]")
    # Kallar på funktionen, med argumentet quiz (dvs vår dictionary)
    quizinator(quiz)
    spela = input("\nVill du Quiza igen?! [J] / [N]?\n: ")
    if spela.lower() == "j":
        print(f"\nEn gång till!{stars}\n")  
        score = 0 # Nollställer score för nästa spelande
    else:
        print("Tack för du spelade!")
        running = False # Ändrar condition för while-loopen, programmet avslutas
       

