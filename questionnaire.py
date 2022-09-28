#   Formuläret med frågorna i en dictionary med index
quiz = { 
    1:{ 
        "fråga" : "Vad är korrekt syntax for \"Hello World\" i Python?\n1. echo(\"Hello World\")\n2. syntax \"Hello World\"\n3. print(\"Hello world\")*",
        "svar": "3"
    },

    2:{ "fråga" : "Hur skriver du kommentarer i python?\n1. //Det här är en kommentar. \n2. # Det här är en kommentar.\n3. /*Det här är en kommentar.*/",
        "svar" : "3"
    },
    
    3:{
        "fråga" : "Vilken är INTE ett korrekt variabelnamn?\n1. min-var \n2. min_var\n3. minvar",
        "svar" : "1"
    },
    
    4: {
        "fråga" :  "Hur skriver man en varaibel med numeriskt värde 5?\n1. x = 5\n2. x = int(5)\n3. Båda är korrekt",
        "svar" : "3"
    },
    
    5:{ 
        "fråga" : "Vilket är korrekt filtillägg för python?\n1. .python3\n2. .py\3. .pyth", 
        "svar" : "2"
    },

    6:{ 
        "fråga" : "Hur skapar du en variabel med flyttal 2.8?\n1. x = float(2.8)\n2. x = 2.8\n3. Båda är korrekt",
        "svar" : "3"
    },

    7:{ 
        "fråga" : "Korrekt syntax för att få ut typen av en var eller obj i python?\n1. print(typeOf(x))\n2. print(type x)\3. print(type(x))",
        "svar" : "3"
    },
    8:{ 
        "fråga" : "Hur anger du korrekt en funktion i python?\n1. function minFunktion():\n2. def minfunktion():\n3. create minfunktion()",
        "svar" : "2"
    },
    9:{ 
        "fråga" : "I python fungerar \"Hello\" lika bra som 'Hello'?\n1. Sant\n2. Falskt",
        "svar" : "1"
    },
    10: { 
        "fråga" : "Korrekt syntax för att skriva ut första bokstaven i en sträng?\n1. x = sub(\"Hello\", 0, 1)\n2. x = \"Hello.sub\"(0, 1)\n3. x = \"Hello\"[0]",
        "svar" : "3"
        },
    11: { 
        "fråga" : "Vilken metod kan användas för att ta bort \"whitespace\" i början/slutet av en sträng?\n1. strip()\n2. trim()\n3. len()",
        "svar" : "1"
        },
    12: { 
        "fråga" : "Vilken metod kan göra en sträng till versaler?\n1. upperCase()\n2. toUpperCase\n3. upper",
        "svar" : "3"
        },
    13: { 
        "fråga" : "Vilken metod kan byta ut delar av en sträng?\n1. replace()\n2. switch()\n3.repl",
        "svar" : "1"
        },
    14: { 
        "fråga" : "Vilken operator används för multiplikation?\n1. \# \n2. * \n3. x",
        "svar" : "2"
        },
    15: { 
        "fråga" : "Vilken operator jämför två värden?\n1. = \n2. == \n3. <>",
        "svar" : "2"
        },
    16: { 
        "fråga" : "Hur definieras en lista?\n1. {\"namn\":\"äpple\", \"färg\":\"grön\"} \n2. (\"äpple\", \"banan\",\"körsbär\") \n3. [\"äpple\", \"banan\":\"körsbär\"]",
        "svar" : "3"
        },

    17: { 
        "fråga" : "Hur definieras en \"tuple\"?\n1. {\"namn\":\"äpple\": \"färg\":\"grön\"} \n2. (\"äpple\", \"banan\",\"körsbär\") \n3. [\"äpple\", \"banan\",\"körsbär\"]",
        "svar" : "2"
        },

    18: { 
        "fråga" : "Hur definieras ett \"set\"?\n1. {\"namn\":\"äpple\", \"färg\":\"grön\"} \n2. {\"äpple\", \"banan\",\"körsbär\"} \n3. [\"äpple\", \"banan\",\"körsbär\"]",
        "svar" : "2"
        },

    19: { 
        "fråga" : "Hur definieras en \"dictionary\"?\n1. {\"namn\":\"äpple\", \"färg\":\"grön\"} \n2. (\"äpple\", \"banan\",\"körsbär\") \n3. [\"äpple\", \"banan\",\"körsbär\"]",
        "svar" : "1"
        },

    20: { 
        "fråga" : "vilken samling är ordnad, ändringsbar och accepterar dubletter?\n1. tuple \n2. dictionary \n3. list",
        "svar" : "3"
        },
    21: { 
        "fråga" : "vilken samling accepterar INTE dubletter?\n1. list \n2. set \n3. dictionary",
        "svar" : "2"
        },
    22: { 
        "fråga" : "hur skriver du ett \"if statment\"?\n1. if x > y then: \n2. if x > y: \n3. if (x > y)",
        "svar" : "2"
        },
    23: { 
        "fråga" : "Hur börjar du en \"while loop\" i python?\n1. while x > y{ \n2. while x > y: \n3. while (x > y)",
        "svar" : "2"
        },
    24: { 
        "fråga" : "Hur börjar du en \"for loop\" i python?\n1. for x > y: \n2. for each x in y: \n3. for x in y:",
        "svar" : "1"
        },
    25: { 
        "fråga" : "Hur stoppar du en loop i python?\n1. return \n2. stop \n3. break",
        "svar" : "3"
        },
    26: { 
        "fråga" : "Vem skapade Python?\n1. Linus Torvalds \n2. Bill Gates \n3. Guido van Rossum",
        "svar" : "3"
        },
    27: { 
        "fråga" : "Vilket år lanserades python?\n1. 1987 \n2. 1991 \n3. 2001",
        "svar" : "2"
        },
    28: { 
        "fråga" : "Det finns en filosofi som summerar python, vad heter den?\n1. Python philosophy \n2. The Rules of python \n3. The Zen of Python",
        "svar" : "3"
        },
    29: { 
        "fråga" : "Python är även en art ormar, vilket är dess korrekta latinska namn?\n1. Pythontus \n2. Pythonidae \n3. Pythus reptilus",
        "svar" : "3"
        },
    30: { 
        "fråga" : "Python är även en art ormar, på en kontinent är den invasiv, vilken?\n1. Asien \n2. Australien \n3. Amerika",
        "svar" : "3"
        },
}