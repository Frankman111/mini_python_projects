import locale
locale.setlocale(locale.LC_ALL, 'de_DE')




while True:
    
    sex = input("Bitte geben Sie ihr biologisches Geschlecht an: ")
    sex = sex.lower()
    
    if sex == "mann":
        print("Mann")
        break
    elif sex == "frau":
        print("Frau")
        break
    else:
        print("falsche Eingabe")
   
height = input("Bitte geben Sie ihre Körpergröße (in m) an: ")
weight = input("Bitte geben Sie ihr Körpergewicht (in Kg) an: ")
height = locale.atof(height)
weight = locale.atof(weight)

# vereinfachte Formel Gewicht*24*1(Mann) oder Gewicht*24*0,9(Frau)

def bmrMale_simple(sex, weight):
    if sex == "mann":
        simpleCalc = float(weight*24*1)
        print("Ihr Grundumsatz ist bei: "+ str(simpleCalc) + "kcal")
    elif sex == "frau":
        simpleCalc = float(weight*24*0.9)
        print("Ihr Grundumsatz ist bei: " + str(simpleCalc) + "kcal")

bmrMale_simple(sex, weight)