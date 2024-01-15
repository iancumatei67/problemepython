
def days_to_units(days):
    print(f"{days} zile in {unit} sunt {result}")


while True:
    unit = input(" Introdu o unitate de timp, pentru a opri programul introdu 'stop' ")
    if unit.lower() =='stop':
        print(f"Programul a fost oprit")
        break
    for days in range(1,10):
        if unit == 'ore':
            result = int(days) * 24
            days_to_units(days)
        elif unit == 'minute':
            result = int(days) * 24 * 60
            days_to_units(days)
        elif unit == 'secunde':
            result = int(days) * 24 * 60 * 60
            days_to_units(days)
        elif unit.isdigit():
            print(f"Trebuie introdusa o unitate de masura, nu un numar")
        else:
            print(f"{unit} nu este o unitate de masura a timpului")

