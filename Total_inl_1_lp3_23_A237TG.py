# coding: utf-8

# Import av olika moduler för att underlätta kodning. Första importen döps om till förkortningen 'plt'  
import matplotlib.pyplot as plt
import csv 


########## Inlämningsuppgift 1 ########## 

# Funktion som summerar värdena av samtliga element förutom lista med index 0 som är strängar samt första element i varje lista. 
# Först skapas en ny lista.
# For-loopen startar från index 1 och renderar listan, andra for-loopen renderar elementen från index 1, och sedan adderar elementen och lägger resultatet i tot. 
# Returparameter: returnerar den nya listan med det totala summan av elementen. 
# insert() lägger till i början av listan en sträng 'Radsumma'. 
def sum_func(my_list):
    new_list = []                                   

    for i in range(1, len(my_list)):                
        tot = 0

        for j in range(1, len(my_list[i])):        
            tot += float(my_list[i][j])            
        new_list.append(tot)                        
            
    new_list.insert(0, 'Radsumma')                  
    return new_list                                 

 



########## Inlämningsuppgift 2 ##########

#Funktion för att läsa csv-filer. With open() som tar in "r" - Read. 
# list() som skapar en ny lista av variabeln reader. 
# for-loopen för att rendera listan i row och sätts i variabeln data. 
# returparameter: returnerar det nya listan som ligger i variablen data. 
def read_file(csv_files):
    with open(csv_files, "r", encoding='UTF-8') as file:
        reader = csv.reader(file, delimiter=';')
        csv_files = list(reader)
        data = [row for row in csv_files]
    return data



# funktion som beräknar medelvärdet av värdena för varje rad i en 2D-lista. 
# Skapar en ny lista. for-loopen startar från index 1 och renderar listan. Konverterar val till Float.  
# Tot_price beräknar total prisutveckling genom att ta sista index minus första index.  
# Beräknar medelvärdet från år 1981 - 2021. 
# Samtliga printar skriver ut en tabell med hjälp av F-sträng och for-loopen av varje rad med 3 element för sig. 
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





########## Inlämningsuppgift 3 ##########

# Funktion som skapar ett diagram beroende på vilket argument som skickas med i funktionen. 
# funktionen tar in två argument, data som är listan från antingen LivsmedelData eller TjansteData, header är rubriken ovanför diagrammet. 
# for-loopen renderar listan från index 1.
# x och y variabler tar in en one-line for-loop som konverterar elementen till float. 
# plot() tar in (x, y), och label som börjar från lista 1 och alla index 0 som hamnar på legend().    
def plotta_data(data, header):

    for i in range(1, len(data)):
        x = [float(rows) for rows in data[0][1:]]
        y = [float(row) for row in data[i][1:]]
        plt.plot(x, y, label=data[i][0])

    plt.title(f'Prisutvecklingen för olika kategorier av {header} År 1980-2021', fontsize= 'small')
    plt.xlabel('År', fontsize='small')
    plt.ylabel('Prisutvecklingen', fontsize='small')
    plt.legend(fontsize= 'xx-small', loc='upper left')
    plt.grid()
    plt.show()





########## Inlämningsuppgift 4 ##########

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
# one-lines for-loopar som tar in value från index 1 och uppåt sedan renderar listan beroende på om man vill plocka åren eller värden (värden ligger på slutet av listan därav används indexet [-1]).
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

    # Ny lista som innehåller samtliga månader skrivna på rätt sätt och inte som i det ursprungliga lista som hade förkortningar av månaderna.
    monthList = ['', 'Januari', 'Februari', 'Mars', 'April', 'Maj', 'Juni', 'juli', 'Augusti', 'September', 'Oktober', 'November', 'December']


    # Plottar den röda linjen med label= monthList[index] indexet är det som användaren anger. 
    plt.plot(yearsOfInput, months, c="red", label=f'Linjediagram för {monthList[index]}')

    # Plottar först linjediagramet med svart färg och sedan stapeldiagram med ljusblå färg. 
    plt.plot(years, values, c="black", label="Linjediagram för medelkpi")
    plt.bar(years, values, color="lightblue", label="kpiMedel")

    plt.title("Konsumentprisindex År 1980 - 2022", fontsize= 'small')
    plt.xlabel('År', fontsize='small')
    plt.xlim(left=1980)
    plt.xticks(rotation=90)
    plt.ylabel('Konsumentprisindex', fontsize='small')
    plt.ylim(bottom=100)
    plt.legend(fontsize= 'xx-small', loc='upper left')
    plt.grid()
    plt.show()
    




########## Inlämningsuppgift 5 ##########

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
# For-loopen börjar från index 1 och renderar listorna. Min() funktionen tar fram minsta värdet från index 1: och index() tar fram indexet till values.
# Returparameter: En kopia av ursprungslistan med minsta värde och indexet till det. 
def minimum_value(myList):
    min_value = []                                   

    for row in myList[1:]:                            
        values = [float(val) for val in row[0:]]      
        min_val = min(values[1:])                     
        min_index = values.index(min_val)             
        min_value.append([min_val, min_index])

    return min_value



# Funktion som ritar ett punktdiagram med punktform och jämför olika kattegorier under åren 1980 - 2021. 
# Anropa funktionerna som beräknar största- och minsta värdet och skickar in data. Sedan vänder på listorna med hjälp av reverse(). 
# for-loopar som tar in listorna och returnerar sista indexet som är [-1] och lägger resultatet i en variabel max_ och min_value. 
# Variabeln years renderar åren från 1980, 2023 (samma längd som listorna ovanför). 
def plot_comparison(data):

    greatValue = great_value(data)
    greatValue.reverse()

    minValue = minimum_value(data)
    minValue.reverse()

    max_value = [rows[-1] for rows in greatValue]
    min_value = [rows[-1] for rows in minValue]
    years = range(1980, 2023)
    
    # plotta diagrammet med två olika färger beroende på om det är max_ eller min_värde lista. 
    plt.scatter(max_value, years, c="blue", label="Årsmax")
    plt.scatter(min_value, years, c="red", label="Årsmin")

    plt.title(f'Månad med högsta resp. lägsta årsvärde av KPI under åren 1980-2022', fontsize= 'small')
    plt.xlabel('Månad', fontsize='small')
    plt.ylabel('År', fontsize='small')
    plt.legend(fontsize= 'small', loc='lower center')
    plt.grid()
    plt.show()
    




########## Menyn ##########

# if-sats som utgår från användarens val och skriver ut resp. funktion.
# While-loop som kör if-satsen varje gång efter att användaren har gjort sitt val, samt ett break som avbruter programmet om användaren väljer alt. 6. 
# Användaren måste välja först alternativ 1 för att läsa in csv-filerna och sedan välja mellan resterande alternativen. 
while True:                                      
    
    # Skriver ut första menyn med 6 val: 
    print('\nMeny \n')
    print('1. Läs in filer.')
    print('2. Konsumentprisindex under åren 1980 - 2022.')
    print('3. Diagram över prisutvecklingen för de olika kategorierna 1980 – 2021.')
    print('4. Tabell över prisutvecklingen för de olika kategorierna 1980 – 2021.')
    print('5. Diagram över högsta och lägsta årskpi under åren 1980 - 2022.')
    print('6. Avsluta programmet.\n')

    choice = str(input('Välj ett menyalternativ (1-6): ')) 

    if choice == '6':
        print('\nTack för denna gång. Programmet avslutas.')
        break                      # Programmet avslutas och while-loopen avbruts. 
    
    elif choice == '1': 

        kpi_file = str(input('Ange filnamn eller tryck bara Enter för kpi.csv: ')) or 'kpi.csv'
        kpiData = read_file('kpi.csv')
        print(kpiData[:2])         # Printar 2 första listor från kpi.csv

        tjanster_file = str(input('Ange filnamn eller tryck bara Enter för tjanster.csv: ')) or 'tjanster.csv'
        tjansteData = read_file('tjanster.csv')
        print(tjansteData[:2])     # Printar 2 första listor från tjanster.csv

        livsmedel_file = str(input('Ange filnamn eller tryck bara Enter för livsmedel.csv: ')) or 'livsmedel.csv'
        livsmedelData = read_file('livsmedel.csv')
        print(livsmedelData[:2])   # Printar 2 första listor från livsmedel.csv

    elif choice == '2':
        # Funktionen som printar ut grafen och tar in kpiData som parameter.  
        plot_kpi_data(kpiData)

    elif choice == '3':
        # Skriver ut undermenyn med 3 val och ett input:
        print('\n- Undermeny -\n')
        print('Välj vilken/vilka listor vill du få diagram från:')
        print('1. livsmedelData')
        print('2. tjansteData')
        print('3. Både livsmedelData och tjansteData\n')

        secondChoice = str((input('Välj ett av menyalternativ ovan (1-3): ')))

        # ny header skapas som tas in i funktionen och sedan körs den. 
        if secondChoice == '1':
            header = 'livsmedel'
            plotta_data(livsmedelData, header)

        elif secondChoice == '2':
            header = 'varor och tjänster'
            plotta_data(tjansteData, header)

        elif secondChoice == '3':
            header = 'livsmedel'
            plotta_data(livsmedelData, header)

            header = 'varor och tjänster'
            plotta_data(tjansteData, header)

        else: 
            print('Ogiltigt val. Försök igen från början.\n')

    elif choice == '4':

        print('\nPrisutvecklingen för olika kategorier av livsmedel År 1980-2021')
        med_value(livsmedelData)

        print("\n")
        
        print('Prisutvecklingen för olika kategorier av varor och tjänster År 1980-2021')
        med_value(tjansteData)   

    elif choice == '5': 
        plot_comparison(kpiData)

    else:
        print('Ogiltigt val. Försök igen med en siffra mellan (1-6).\n')

