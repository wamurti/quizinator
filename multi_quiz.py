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
    
    key_list = list(arg.keys()) # skapar lista av key och values från dict
    val_list = list(arg.values())

    #Nedan if-block låter en ange hur många frågor man vill svara på + att frågorna är slumpade & kommer bara en gång förutsatt att man svarat rätt.
    if cap != 0: 
        for _ in range(0,cap): #Cap = hur många frågor vill du besvara
            random_question_index = random.randint(0,len(key_list)-1)
            print(val_list[random_question_index]['fråga'])
            svaret = input("\nSvar : ")
            if svaret == val_list[random_question_index]["svar"]:
                print(f"Rätt Svar!\n{stars}")
                score +=1
                val_list.pop(random_question_index) #Tar bort random_question_index från listor för att undvika att få samma fråga igen.
                key_list.pop(random_question_index)
                
            else:
                print(f"FEL!\n{stars}")
            print(f"{stripes}\nDu fick {score}/{len(arg)} rätt!{stripes}") # Printar score
        
    else: 
    #Nedan else-block kör igenom alla frågor utan randomisering
            
        for frågor in arg:
            print(arg[frågor]['fråga']+f"{stars}")
            svaret = input("\nSvar : ")
            if svaret == arg[frågor]['svar']:
                print(f"Rätt Svar!\n{stars}")
                score +=1 # Varje rätt svar ger +1 till score variabeln
            else:
                print(f"FEL!\n{stars}")
        print(f"{stripes}\nDu fick {score}/{len(arg)} rätt!{stripes}") # Printar score

