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
import numpy as np 
import csv 


#Funktion för att läsa csv-filer.  
def read_file(csv_files):
    with open(csv_files, "r", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        csv_files = list(reader)
        data = [row for row in csv_files]
    return data


# Globala variabler som tar in funktionen ovan och har resp. csv-fil som parameter 
# Dessa variabler ligger längst upp i filen för att man ska kunna nå de överallt. 
# Dessa variabler används längst ner i menyn för att läsa filerna. 
livsmedelData = read_file('livsmedel.csv')
tjansteData = read_file('tjanster.csv')
kpiData = read_file('kpi.csv')



# Funktion som summerar värdena av samtliga element förutom lista med index 0 som är strängar samt första element i varje lista. Först skapas en ny lista.
# For-loopen startar från index 1 och renderar listan, andra for-loopen adderar elementen och lägger resultatet i tot. 
# Returparameter: returnerar den nya listan med det totala summan av elementen. 
def sum_func(my_list):
    new_list = []                                   

    for i in range(1, len(my_list)):                
        tot = 0

        for j in range(1, len(my_list[i])):        
            tot += float(my_list[i][j])            
        new_list.append(tot)                        
            
    new_list.insert(0, 'Radsumma')                  
    return new_list                                 

                       



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


    header1 = "livsmedel" if myList == livsmedelData else False
    header2 = "varor och tjänster" if myList == tjansteData else False

    print("+","-"*70,"+")
    print(f'{"|"} {"Kategorier av"} {header1 or header2:<26} {"|"} {"Medelvärde":>12} {"|"} {"Totalt":>12} {"|"}')
    print("+","="*40,"+", "="*12, "+", "="*12, "+")

    for i in range(0, len(newList), 3):
        print(f'{"|"} {newList[i+0]:<40} {"|"} {newList[i+1]:>12} {"|"} {newList[i+2]:>12} {"|"}')
        print("+","-"*40,"+", "-"*12, "+", "-"*12, "+")




# Funktion som skapar ett diagram beroende på vilket argument som skickas med i funktionen. 
# funktionen tar in två argument, data och header som 

def plotta_data(data, header):

    x = range(1, len(data[0]))

    if data == tjansteData or data == livsmedelData:
        
        for i in range(1, len(data)):
            y = [float(row) for row in data[i][1:]]
            plt.plot(x, y, label=data[i][0])

            
            
        """
        elif data == livsmedelData:

            prices_1 = [float(row) for row in data[1][1:]]
            prices_2 = [float(row) for row in data[2][1:]]
            prices_3 = [float(row) for row in data[3][1:]]
            prices_4 = [float(row) for row in data[4][1:]]
            prices_5 = [float(row) for row in data[5][1:]]
            prices_6 = [float(row) for row in data[6][1:]]
            prices_7 = [float(row) for row in data[7][1:]]
            prices_8 = [float(row) for row in data[8][1:]]
            
            plt.plot(prices_1, c='blue')
            plt.plot(prices_2, c='orange')
            plt.plot(prices_3, c='green')
            plt.plot(prices_4, c='red')
            plt.plot(prices_5, c='purple')
            plt.plot(prices_6, c='brown')
            plt.plot(prices_7, c='pink')
            plt.plot(prices_8, c='grey')

        """

    else:
        print('felaktig data')

    #x_values = np.linspace(1980, 2020, 5)

    categories = [col[0] for col in data[1:]]

    #years = [rows for rows in data[0][1:]]

    plt.title(f'Prisutvecklingen för olika {header} År 1980-2021', fontsize= 'x-small')
    plt.xlabel('År', fontsize='x-small')
    plt.ylabel('Prisutvecklingen', fontsize='x-small')
    plt.legend(categories, fontsize= 'xx-small', loc='upper left')
    #plt.xlim(1980, 2020)

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
    
    # Skriver ut menyn med 6 val: 
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
        break                                               # Programmet avslutas och while-loopen avbruts. 
    
    elif choice == 1: 

        # Alternativ 1: 
        csv_file = input('Ange filnamn avsluta med (.csv) eller tryck bara Enter för kpi.csv: ')

        if csv_file == "tjanster.csv":
            print(tjansteData)
        elif csv_file == "livsmedel.csv":
            print(livsmedelData)
        elif csv_file == "kpi.csv":
            print(kpiData)
        else:
            print(kpiData)
        
        # Alternativ 2: 
        """
        kpi_file = input('Ange filnamn eller tryck bara Enter för kpi.csv: ') or 'kpi.csv'
        print(kpiData)

        tjanster_file = input('Ange filnamn eller tryck bara Enter för kpi.csv: ') or 'tjanster.csv'
        print(tjansteData)

        livsmedel_file = input('Ange filnamn eller tryck bara Enter för kpi.csv: ') or 'livsmedel.csv'
        print(livsmedelData)

        """

    elif choice == 2:
        print(f'Den returnerade listan är: {sum_func(kpi_10)}')

    elif choice == 3:
        print('\n- Meny - ')
        print('1. Skriv ut TjansteData diagrammet.')
        print('2. Skriv ut LivsmedelData diagrammet.')
        print('3. Skriv ut båda diagrammen.\n')

        secondChoice = int(input('Välj ett av menyalternativ ovan (1-3): '))

        if secondChoice == 1:
            header = 'kategorier av varor och tjänster'
            plotta_data(tjansteData, header)
            # anropa funktionen med två argument 

        elif secondChoice == 2:
            header = 'livsmedel'
            plotta_data(livsmedelData, header)
            # anropa funktionen med två argument

        elif secondChoice == 3:

            header = 'kategorier av varor och tjänster'
            # anropa funktionen med två argument
            plotta_data(tjansteData, header)


            header = 'livsmedel'
            # anropa funktionen med två argument
            plotta_data(livsmedelData, header)


        else: 
            print('Ogiltigt val. försök igen från början.\n')


    elif choice == 4:
        print('Prisutvecklingen för olika kategorier av livsmedel År 1980-2021')
        med_value(livsmedelData)
        print("\n")
        print('Prisutvecklingen för olika kategorier av varor och tjänster År 1980-2021')
        med_value(tjansteData)   

    elif choice == 5: 
        print(f'Minsta värdet och dess index är: {minimum_value(kpi_10)}')

    else:
        print('Ogiltigt val. försök igen med en siffra mellan (1-6).\n')

