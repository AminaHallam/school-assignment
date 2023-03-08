# coding: utf-8

import os
os.system('clear') # function system to issue command cls 


kpi_10 = [['År', 'Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'], ['2019', '328.56', '331.02', '331.79', '334.11', '334.95', '334.47', '335.8', '334.39', '335.95', '336.04', '336.36', '337.68'], ['2018', '322.51', '324.87', '325.76', '327.1', '327.86', '328.62', '330.33', '329.63', '331.14', '330.72', '330.4', '331.87'], ['2017', '317.5', '319.73', '319.68', '321.54', '321.74', '321.97', '323.69', '323.18', '323.62', '323.38', '324.04', '325.23'], ['2016', '313.13', '314.14', '315.7', '315.64', '316.21', '316.54', '316.73', '316.38', '316.91', '318', '318.1', '319.68'], ['2015', '310.75', '312.93', '313.19', '313.16', '314.24', '313.33', '313.43', '312.81', '314.06', '314.29', '313.75', '314.21'], ['2014', '311.39', '312.7', '312.68', '313.89', '314.05', '314.7', '313.67', '313.35', '313.85', '314.02', '313.56', '314.05'], ['2013', '312', '313.39', '314.65', '314.03', '314.54', '313.99', '313.55', '313.84', '315.05', '314.4', '314.2', '315.04'], ['2012', '311.85', '313.92', '314.8', '315.49', '315.23', '314.45', '313.23', '313.55', '314.81', '314.59', '313.82', '314.61'], ['2011', '306.15', '308.02', '310.11', '311.44', '312.02', '311.28', '311.13', '311.23', '313.41', '313.42', '314.16', '314.78'], ['2010', '299.79', '301.59', '302.32', '302.36', '302.92', '302.97', '302.04', '302.06', '304.6', '305.57', '306.58', '308.73']]

def print_kpi_10(): #Skriver ut listan kpi_10

    print('\nHela Listan:\n') 
    print(kpi_10) # Skriver ut hela listan i en utskrift utan radbrytning för varje rad

    print('\nListan radvis\n')
    for row in kpi_10: # Skriver ut hela listan med radbrytning för varje rad
        print(row)


# Skriv din kod här:

# Import av olika moduler för att underlätta kodning. 
import matplotlib.pyplot as plt
import csv 


#Funktion för att läsa csv-filer.  
def read_file(csv_files):
    with open(csv_files, "r", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        csv_files = list(reader)
        data = [row for row in csv_files]
    return data




# funktion som beräknar medelvärdet av värdena för varje rad för en 2D-lista. Först Lägger till strängen på slutet av myList med index 0. 
# Skapar en ny lista. for-loopen startar från index 1 och renderar listan. Konverterar val till Float.  
# Tot_price beräknar total prisutveckling genom att ta sista index minus första index.  
# Beräknar medelvärdet från år 1981 - 2021. 
# En if-sats som jämför om det är livsmedelData eller tjansteData, 
# sedan skriver den ut en tabell med hjälp av F-sträng och for-loopen varje rad för sig. 
def med_value(myList):
                     
    newList = []                                    

    for row in myList[1:]:                           
        tot_price = 0 
        values = [float(val) for val in row[1:]] 

        tot_price += values[-1] - values[0]  
        
        average = sum(values[1:]) / (len(values[1:]))        
        
        row.append(round(average, 2))
        
        newList.append(row[0])    
        newList.append(row[-1])                     
        newList.append(round(tot_price, 2))

    # If-satser som kontrollerar om det är livsmedelsData eller tjänsteData och returnerar resp. titel annars returneras 0 som är False.
    header1 = "livsmedel" if myList == livsmedelData else False
    header2 = "varor och tjänster" if myList == tjansteData else False

    print("+","-"*70,"+")
    print(f'{"|"} {"Kategorier av"} {header1 or header2:<26} {"|"} {"Medelvärde":>12} {"|"} {"Totalt":>12} {"|"}')
    print("+","="*40,"+", "="*12, "+", "="*12, "+")

    # For-loopen för att rendera varje 3 element på rad och därefter använda F-sträng för att underlätta utskrivning av tabellen
    for i in range(0, len(newList), 3):
        print(f'{"|"} {newList[i+0]:<40} {"|"} {newList[i+1]:>12} {"|"} {newList[i+2]:>12} {"|"}')
        print("+","-"*40,"+", "-"*12, "+", "-"*12, "+")




# Funktion som skapar ett diagram beroende på vilket argument som skickas med i funktionen. 
# funktionen tar in två argument, data som är listan från antingen LivsmedelData eller TjansteData, header är rubriken ovanför diagrammet. 
# for-loopen renderar listan från index 1.
# x_axis och y_axis variabler tar in en one-line for-loop som konverterar elementen till float. 
# plot() tar in (x_axis, y_axis), och label som börjar från lista 1 och alla index 0 som hamnar på legend().    
def plotta_data(data, header):

    for i in range(1, len(data)):
        x_axis = [float(rows) for rows in data[0][1:]]
        y_axis = [float(row) for row in data[i][1:]]
        plt.plot(x_axis, y_axis, label=data[i][0])

    plt.title(f'Prisutvecklingen för olika kategorier av {header} År 1980-2021', fontsize= 'x-small')
    plt.xlabel('År', fontsize='x-small')
    plt.ylabel('Prisutvecklingen', fontsize='x-small')
    plt.legend(fontsize= 'xx-small', loc='upper left')
    plt.grid()
    plt.show()



# funktion som beräknar medelvärdet av värdena för varje rad för en 2D-lista.  
# Skapar en ny lista. for-loopen startar från index 1 och renderar listan. Konverterar val till Float.  
# Appenda först average till row och sedan row till min nya lista. insert på index 0 i newList -> myList.
# Returparameter: En kopia av ursprungslistan med en extra kolumn med medelvärden sist i listan. 
def med_value_kpi(myList):
                    
    newList = []                                    

    for row in myList[1:]:                          
        values = [float(val) for val in row[1:]]    
        average = sum(values) / (len(values))        
        row.append(round(average, 2))
        newList.append(row)                         

    newList.insert(0, myList[0])               

    return newList



# Funktion som skapar graf. och stapeldiagram för kpi-data. Skapar ett input som frågar efter en månad och sedan konverterar input till int. 
# Anropa funktionen ovan som beräknar medelvärdet och ta in data som parameter. 
# one-lines for-loopar som renderar listan beroende på om man vill plocka åren, värden eller månader. 
def plot_kpi_data(data): 

    index = int(input("Ange vilken månad som ska presenteras (1 - 12) heltal: "))

    value = med_value_kpi(data)

    years = [int(rows[0]) for rows in value[1:]]

    values = [float(rows[-1]) for rows in value[1:]]

    # one-line for-loop som tar både element och index med hjälp av enumerate() och exkluderar rad med index 1 som är för år 2022 om i inte är 1 eller index är mindre eller = 7. 
    month = [row for i, row in enumerate(value) if i != 1 or index <= 7]

    # if-sats som ser om index som skickas av användaren är mindre än eller lika med 7 då börjar åren från index 0: annars börjar åren från 1: 
    yearsOfInput = years[0:] if index <= 7 else years[1:]
    
    # Loopen itererar över listan month, och month_list ska representera en viss månad med index som kommer ifrån input.
    # Nästa for-loopen konverterar samtliga element från index 1: till float = months. 
    result = [month_list[index] for month_list in month]
    months = [float(col) for col in result[1:]]


    # Plottar den röda linjen med label= result som är månaden som användaren har valt. 
    plt.plot(yearsOfInput, months, c="red", label=f'Linjediagram för {result[0]}')
    plt.plot(years, values, c="black", label="Linjediagram för medelkpi")
    plt.bar(years, values, color="lightblue", label="kpiMedel")

    plt.title("Konsumentprisindex År 1980 - 2022", fontsize= 'x-small')
    plt.xlabel('År', fontsize='x-small')
    plt.xlim(left=1980)
    plt.xticks(rotation=90)
    plt.ylabel('Konsumentprisindex', fontsize='x-small')
    plt.ylim(bottom=100)
    plt.legend(fontsize= 'xx-small', loc='upper left')
    plt.grid()
    plt.show()
    


# Funktion som returnerar det största värdet på varje rad och dess index för en 2D-lista. Först skapas en ny lista, 
# For-loopen börjar från index 1 och renderar listorna. Max() funktionen tar fram största värdet från index 1: och index() tar fram indexet till values.
# Returparameter: En kopia av ursprungslistan med största värde och indexet till det. 
def great_value(myList):
    max_value = []                                     

    for row in myList[1:]:                             
        values = [float(val) for val in row[0:]]      
        max_val = max(values[1:])                      
        max_index = values.index(max_val)             
        max_value.append([max_val, max_index])

    return max_value



# Funktion som returnerar minsta värdet på varje rad och dess index. Funktionen tar in som argument listan. 
# For-loopen börjar från index 1 och renderar listorna. Min() funktionen tar fram största värdet från index 1: och index() tar fram indexet till values.
# Returparameter: En kopia av ursprungslistan med största värde och indexet till det. 
def minimum_value(myList):
    min_value = []                                    

    for row in myList[1:]:                            
        values = [float(val) for val in row[0:]]      
        min_val = min(values[1:])                     
        min_index = values.index(min_val)             
        min_value.append([min_val, min_index])

    return min_value




# if-sats som utgår från användarens val och skriver ut resp. funktion:
# While-loop som kör if-satsen varje gång efter att användaren har gjort sitt val
while True:                                      
    
    # Skriver ut första menyn med 6 val: 
    print('\n- Program för att läsa in och analysera resultatet i uppgift 1 - 5 \n')
    print('1. Läser in csv-filerna.')
    print('2. Konsumentprisindex under åren 1980 - 2022.')
    print('3. Prisutvecklingen för de olika kategorierna 1980 - 2021.')
    print('4. Prisutvecklingen i procentform för de olika kategorierna 1980 - 2021.')
    print('5. Jämförelse mellan olika katergorier under åren 1980 - 2021.')
    print('6. Avsluta programmet.\n')

    choice = int(input('Välj ett menyalternativ (1-6): ')) 

    if choice == 6:

        print('Tack för denna gång. Programmet avslutas.')
        break                      # Programmet avslutas och while-loopen avbruts. 
    
    elif choice == 1: 

        kpi_file = input('Ange filnamn eller tryck bara Enter för kpi.csv: ') or 'kpi.csv'
        print(read_file(kpi_file))

        tjanster_file = input('Ange filnamn eller tryck bara Enter för tjanster.csv: ') or 'tjanster.csv'
        print(read_file(tjanster_file))

        livsmedel_file = input('Ange filnamn eller tryck bara Enter för livsmedel.csv: ') or 'livsmedel.csv'
        print(read_file(livsmedel_file))

    elif choice == 2:
        # Funktionen read_file läser csv filer som vi skickar in som en parameter in i funktionen. Variabeln används sedan in i en annan funktion. 
        kpiData = read_file('kpi.csv')
        plot_kpi_data(kpiData)

    elif choice == 3:
        # Skriver ut undermenyn med 3 val och ett input:
        print('\n- Undermeny - ')
        print('1. Skriv ut diagram för Tjänster.')
        print('2. Skriv ut diagram för Livsmedel.')
        print('3. Skriv ut båda diagrammen.\n')

        secondChoice = int(input('Välj ett av menyalternativ ovan (1-3): '))

        # If-satsen kollar vilket val användaren har gjort och sedan läser in varje fil med hjälp av funktionen read_file.
        # Därefter skickar en ny header till funktionen och sedan körs den. 
        if secondChoice == 1:

            tjansteData = read_file('tjanster.csv')
            header = 'varor och tjänster'
            plotta_data(tjansteData, header)

        elif secondChoice == 2:

            livsmedelData = read_file('livsmedel.csv')
            header = 'livsmedel'
            plotta_data(livsmedelData, header)

        elif secondChoice == 3:

            tjansteData = read_file('tjanster.csv')
            header = 'varor och tjänster'
            plotta_data(tjansteData, header)

            livsmedelData = read_file('livsmedel.csv')
            header = 'livsmedel'
            plotta_data(livsmedelData, header)

        else: 
            print('Ogiltigt val. Försök igen från början.\n')


    elif choice == 4:

        livsmedelData = read_file('livsmedel.csv')
        print('Prisutvecklingen för olika kategorier av livsmedel År 1980-2021')
        med_value(livsmedelData)

        print("\n")
        
        tjansteData = read_file('tjanster.csv')
        print('Prisutvecklingen för olika kategorier av varor och tjänster År 1980-2021')
        med_value(tjansteData)   

    elif choice == 5: 

        print(f'Minsta värdet och dess index är: {minimum_value(kpi_10)}')

    else:
        print('Ogiltigt val. Försök igen med en siffra mellan (1-6).\n')

