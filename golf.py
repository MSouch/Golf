import csv

# gets the number of players for the times to loop through the program 
numPlayers = (int(input("Please enter the number of players: ")))
#create an array for a player variable 
players = []

#create a counter for range of numPlayers
for i in range(numPlayers):
    #create variables for name and score - increase counter by 1 given the numPlayers
    name = input("Enter the name of the player: ".format(i+1))
    score = input("Enter the score of the player: ".format(i+1))
    #format the array such that name:score
    players.append((name, score)) 

#open a txt doc in write mode, start on new line
with open('golf.txt', 'w', newline='') as x:
    #create a writer with csv plugin
    writer = csv.writer(x)
    #writer writes rows with formatted array
    writer.writerows(players)