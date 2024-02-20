import random #program needs to generate random numbers 

def register(): #signing up
    print('\n'+"REGISTER")
    print('--------')

    username = input("Username: ")

    file = open('nea_accounts.txt', 'r') #opens in read mode
    line = ' '
    while line != '': #reading file
        line = file.readline()
        data = line.split(',')
        while data[0]==username: #when username already exists
            print('Username already in use')
            username = input('Please enter a different username: ')
    file.close()

    password = input("Password: ")

    #length check
    while len(password)<4 or len(password)>10: 
        print("Password must be 4-10 characters long")
        password = input("Please enter a different password: ")

    #validation (strong password)
    while password == username:
        print("Username cannot be used as password")
        password = input("Please enter a different password: ")

    file = open('nea_accounts.txt', 'a') #append mode
    file.write(username+','+password+'\n') #saving account info
    file.close()

()

def dicegame():
    print('\n'+"LOG IN")
    print('--------')
    
    file = open('nea_accounts.txt', 'r') #opens in read mode

    #first authorisation
    print('First player')
    playera = input("Player name: ")
    passworda = input("Password: ")
    
    accessA = False #access not yet granted

    line = ' ' #space

    while line != '': #blank
        line = file.readline()
        data = line.split(',')
        if data[0] == playera: #means the player is authorised
            if str(data[1].rstrip('\n')) == str(passworda.rstrip('\n')): #no space attached
                accessA = True #access granted
                break
            else:
                passworda = input("Wrong password. Please enter again: ") #giving another chance  

    if accessA == True:
        print('Welcome back,', playera)
    else:
        print("Access denied")
    
    file.close()

    file = open('nea_accounts.txt', 'r') #opens in read mode

    #second authorisation
    print('')
    print('Second player')
    playerb = input("Player name: ") #same process for the second player
    while playerb == playera:
        playerb = input("Enter a different username to the first player: ")
    passwordb = input("Password: ")
    
    accessB = False

    line = ' '

    while line != '':
        line = file.readline()
        data = line.split(',')
        if data[0] == playerb:
            if str(data[1].rstrip('\n')) == str(passwordb.rstrip('\n')):
                accessB = True
                break
            else:
                passwordb = input("Wrong password. Please enter again: ")    

    if accessB == True:
        print('Welcome back,', playerb)
    else:
        print("Access denied")
    
    file.close()

    print('\n'+"DICE GAME")
    print('--------')

    if accessA == True and accessB == True: #only when both players are authorised
        totala = 0
        totalb = 0
        for game in range(5): #5 rounds in total
            print('\n'+'Round',game+1)
            for roll in range(2):
               dice = input("\n"+playera+" rolls a die")
               dice = random.randint(1,6)
               print(dice)
               totala += dice
            for roll in range(2):
               dice = input("\n"+playerb+" rolls a die")
               dice = random.randint(1,6)
               print(dice)
               totalb += dice

            print('\n'+playera+'    '+playerb+'\n'+str(totala),'    :    ',str(totalb))

        #if total score is even, add 10 points
        if totala % 2 == 0:
            totala += 10
            print("Additional 10 points for "+playera)
        if totalb % 2 == 0:
            totalb += 10
            print("Additional 10 points for "+playerb)

        #if total score is odd, subtract 5 points
        if totala % 2 != 0:
            totala -=5
            print("5 points from "+playera)
        if totalb % 2 != 0:
            totalb -=5
            print("5 points from "+playerb)
               
        print('\n'+playera+'    '+playerb+'\n'+str(totala),'    :    ',str(totalb))

        if totala > totalb:
            print('\n'+"Congratulations!",playera,"won!")
            winner = playera
        elif totalb > totala:
            print('\n'+"Congratulations!",playerb,"won!")
            winner = playerb
        else:
            while totala == totalb: #when the players draw
                #rolling a die until one achieves the higher score
                print('Tied!')
                dice = input("\n"+playera+" rolls a die")
                dice = random.randint(1,6)
                print(dice)
                totala += dice
                dice = input("\n"+playerb+" rolls a die")
                dice = random.randint(1,6)
                print(dice)
                totala += dice
                print('\n'+playera+'    '+playerb+'\n'+str(totala),'    :    ',str(totalb))
            if totala > totalb:
                print('\n'+"Congratulations!",playera,"won!")
                winner = playera
            elif totalb > totala:
                print('\n'+"Congratulations!",playerb,"won!")
                winner = playerb

        file = open('nea_winners.txt', 'a') #open in append mode
        if winner == playera: #when A wonline.
            file.write(str(totala)+','+str(winner)+'\n')
        else: #when B won
            file.write(str(totalb)+','+str(winner)+'\n')
        file.close()

        file = open('nea_winners.txt', 'r') #open in read mode
        count = 0
        line = ' ' #space
        while line != '': #blank not space, so while loop will run
            line = file.readline() #read through the file   
            count += 1 #counting the number of lines
        file.close() #at the end, count=number of lines

        file = open('nea_winners.txt','r')
        scores = list() #making a list of items in the file
        for loop in range(count-1): #not to include blank at the end
            line = file.readline()
            data = line.split(',')
            scores.append(str(data[0].rstrip('\n')+' - '+data[1].rstrip('\n')))

        scores.sort(reverse=True) #arrange in descending order (from highest)

        print('\n'+'TOP 5 PLAYERS')

        for loop in range(5): #5 highest scores
            print(scores[loop])
        
        file.close()
                   
()

choice = 0
while choice !=3:
    print('')
    print('''        MENU
1. Register
2. Two-player dice game
3. Quit
    ''') #it displays the menu for the user

    choice = int(input("Enter your choice: ")) #a dynamic variable to take user's choice

    if choice == 1:     #a selection to call the subprogram the user wants
        register() #function to allow the user to sign up
    elif choice == 2:
        dicegame() #function that runs a two-player dice game
    elif choice == 3:
        break #quit
    else:
        print('invalid input')

print("Thank you for using the program")





