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
   
height = input("Bitte geben Sie ihre Körpergröße (in cm) an: ")
weight = input("Bitte geben Sie ihr Körpergewicht (in Kg) an: ")
age = input("Bitte geben Sie ihr Alter an: ")
height = locale.atof(height)
weight = locale.atof(weight)
age = locale.atof(age)

# vereinfachte Formel Gewicht*24*1(Mann) oder Gewicht*24*0,9(Frau)

def bmr_simple(sex, weight):
    if sex == "mann":
        simpleCalc = float(weight*24*1)
        print("Ihr Grundumsatz ist bei: "+ str(simpleCalc) + "kcal")
    elif sex == "frau":
        simpleCalc = float(weight*24*0.9)
        print("Ihr Grundumsatz ist bei: " + str(simpleCalc) + "kcal")

bmr_simple(sex, weight)

# Berechnung nach Harris-Benedikt-Formel

def bmr_harris_benedict(sex, weight, height, age):
    bhCalc = 88.362 + (13.397*float(weight))+(4.799*float(height))-(5.677*float(age))
    print("Ihr Grundumsatz ist bei: " + str(bhCalc) + "kcal")
    
bmr_harris_benedict(sex, weight, height, age)