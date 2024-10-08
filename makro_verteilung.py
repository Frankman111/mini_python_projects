import locale
locale.setlocale(locale.LC_ALL, 'de_DE')

weight = input("Bitte Gewicht angeben: ")
target_calories = input("Bitte gewünschte Zielkalorien angeben: ")
protein_intake = input("Wieviel Protein g/kg Körpergewicht?")
fat_intake =  input("Wieviel Fett g/kg Körpergewicht?" )


def calculations(weight, target_calories, protein_intake, fat_intake):
    protein = locale.atof(weight)*locale.atof(protein_intake)
    protein = round(protein, 1)
    fat = locale.atof(weight)*locale.atof(fat_intake)
    fat = round(fat, 1)
    carbs = (locale.atof(target_calories) - ((protein*4.2) + (fat*9))) // 4.2
    carbs = round(carbs, 1)
    carbs_calories = carbs*4.2
    msg = "Protein: " +  str(protein) +  "g " + "Fett: " + str(fat)  +"g " "Kohlenhydrate: "  + str(carbs) + "g " + "entspricht " + str(carbs_calories) + " kcal"
    print(msg)
   
    

calculations(weight, target_calories, protein_intake, fat_intake)



111