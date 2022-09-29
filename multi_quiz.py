from questionnaire import quiz
import random


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


def quizinator(arg,cap=0):
    global score
    if cap != 0: 
        for _ in range(0,cap):
            random_question = random.choice(arg)
            print(random_question['fråga'])
            svaret = input("\nSvar : ")
            if svaret == random_question["svar"]:
                print(f"Rätt Svar!\n{stars}")
                score +=1
            else:
                print(f"FEL!\n{stars}")
        print(f"{stripes}\nDu fick {score}/{cap} rätt!{stripes}") # Printar score
        
    else:
            
        
        for frågor in arg:
            random_fråga = random.randint(1,len(arg))
            print(quiz[random_fråga]['fråga']+f"{stars}")
            svaret = input("\nSvar : ")
            if svaret == quiz[random_fråga]['svar']:
                print(f"Rätt Svar!\n{stars}")
                score +=1 # Varje rätt svar ger +1 till score variabeln
            else:
                print(f"FEL!\n{stars}")
        print(f"{stripes}\nDu fick {score}/{len(arg)} rätt!{stripes}") # Printar score



# En while loop som gör att man kan köra det flera gånger om man vill
running = True # Condition för loopen, kan nog vara vad som helst
while running == True:
    # Lite intro bara
    print("\t-----QUIZTIME!-----")
    antal = int(input("Hur många frågor vill du ha? (1-30)\n: ")) # välj antal frågor
    print("Svara på frågorna med [1], [2] eller [3]\n")
    # Kallar på funktionen, med argumentet quiz (dvs vår dictionary)
    
    quizinator(quiz,antal)
    spela = input("\nVill du Quiza igen?! [J] / [N]?\n: ")
    if spela.lower() == "j":
        print(f"\nEn gång till!{stars}\n")  
        score = 0 # Nollställer score för nästa spelande
    else:
        print("Tack för du spelade!")
        running = False # Ändrar condition för while-loopen, programmet avslutas
       

