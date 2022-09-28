
from quiz import quiz
# POÄNG räkning. måste kanske ligga i loop?
score = 0
# score += 1 , efter rätt svar

# Det här printar nr 1 och nr 1s fråga
# print(quiz[1]['fråga'])

# Går igenom 1-3 index i dict, "frågor" är bara nummerna i dicten
# for frågor in quiz:
       # print(quiz[frågor]['fråga'])

def quizinator(arg):
    global score # Hade bara kunnat skriva score = 0 här, men ville testa global
    for frågor in arg:
        print(quiz[frågor]['fråga'])
        print(f"{quiz[frågor]['alternativ']}...?")
        svaret = input("\nSvar : ")
        if svaret == quiz[frågor]['svar']:
            print("Rätt Svar!\n\n"+"*"*20)
            score +=1 # Varje rätt svar ger +1 till score variabeln
        else:
            print("FEL!\n\n"+"*"*20)
    print("\n"+"=*"*10+f"\nDu fick {score}/3 rätt!\n"+"=*"*10) # Printar score, och krimskrams

# Kallar på funktionen, med argumentet quiz (dvs vår dictionary)
quizinator(quiz)