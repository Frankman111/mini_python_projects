import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

height = input("Bitte geben Sie ihre Körpergröße (in m) an: ")
weight = input("Bitte geben Sie ihr Körpergewicht (in Kg) an: ")
height = locale.atof(height)
weight = locale.atof(weight)
def bmi(height, weight):
    bmi = float(weight) / (float(height)**2)
    bmi = "Ihr BMI beträgt: " + str(round(bmi, 1))
    print(bmi)
    
    
bmi(height, weight)