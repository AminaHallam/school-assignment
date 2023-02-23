# coding: utf-8


kpi_10 = [['År', 'Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'], ['2019', '328.56', '331.02', '331.79', '334.11', '334.95', '334.47', '335.8', '334.39', '335.95', '336.04', '336.36', '337.68'], ['2018', '322.51', '324.87', '325.76', '327.1', '327.86', '328.62', '330.33', '329.63', '331.14', '330.72', '330.4', '331.87'], ['2017', '317.5', '319.73', '319.68', '321.54', '321.74', '321.97', '323.69', '323.18', '323.62', '323.38', '324.04', '325.23'], ['2016', '313.13', '314.14', '315.7', '315.64', '316.21', '316.54', '316.73', '316.38', '316.91', '318', '318.1', '319.68'], ['2015', '310.75', '312.93', '313.19', '313.16', '314.24', '313.33', '313.43', '312.81', '314.06', '314.29', '313.75', '314.21'], ['2014', '311.39', '312.7', '312.68', '313.89', '314.05', '314.7', '313.67', '313.35', '313.85', '314.02', '313.56', '314.05'], ['2013', '312', '313.39', '314.65', '314.03', '314.54', '313.99', '313.55', '313.84', '315.05', '314.4', '314.2', '315.04'], ['2012', '311.85', '313.92', '314.8', '315.49', '315.23', '314.45', '313.23', '313.55', '314.81', '314.59', '313.82', '314.61'], ['2011', '306.15', '308.02', '310.11', '311.44', '312.02', '311.28', '311.13', '311.23', '313.41', '313.42', '314.16', '314.78'], ['2010', '299.79', '301.59', '302.32', '302.36', '302.92', '302.97', '302.04', '302.06', '304.6', '305.57', '306.58', '308.73']]

def print_kpi_10(): #Skriver ut listan kpi_10

    print('\nHela Listan:\n') 
    print(kpi_10) # Skriver ut hela listan i en utskrift utan radbrytning för varje rad

    print('\nListan radvis\n')
    for row in kpi_10: # Skriver ut hela listan med radbrytning för varje rad
        print(row)


# Skriv din kod här:


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
# Appenda först average till row och sedan row till min nya lista. insert på index 0 i newList -> myList med strängen 'Medelvärde'. 
# Returparameter: En kopia av ursprungslistan med en extra kolumn med medelvärden sist i listan. 
def med_value(myList):
    myList[0].append('Medelvärde')                  
    newList = []                                    

    for row in myList[1:]:                          
        values = [float(val) for val in row[1:]]    
        average = sum(values) / (len(values))        
        row.append(round(average, 2))
        newList.append(row)                         

    newList.insert(0, myList[0])               

    return newList





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
    print('\n- Meny -\n')

    print('1. Skriv ut listan.')
    print('2. Beräkna summa.')
    print('3. Beräkna medelvärde.')
    print('4. Hitta största värdet.')
    print('5. Hitta minsta värdet.')
    print('6. Avsluta programmet.\n')

    choice = int(input('Välj ett menyalternativ (1-6): ')) 

    if choice == 6:
        print('Tack för denna gång. Programmet avslutas.')
        break                                               # Programmet avslutas och while-loopen avbruts. 
    
    elif choice == 1: 
        print_kpi_10()

    elif choice == 2:
        print(f'Den returnerade listan är: {sum_func(kpi_10)}')

    elif choice == 3:
        print(f'Medelvärdet är: {med_value(kpi_10)}')

    elif choice == 4:
        print(f'Största värdet och dess index är: {great_value(kpi_10)}')

    elif choice == 5: 
        print(f'Minsta värdet och dess index är: {minimum_value(kpi_10)}')

    else:
        print('Ogiltigt val. försök igen med en siffra mellan (1-6).\n')

