print ("Welcome to my computer quiz!")

playing = input("Would you like to play? ")

if playing.lower () != "yes":
    print ("It's ok. Have nice day!")
    quit()

print ("Ok, let's paly!")
score = 0

answer = input ("What does cpu stand for? ")
if answer.lower () == "cpu":
    print ("Correct! ")
    score +=1
else:
    print ("incorrect")


answer = input ("What does gpu stand for? ")
if answer.lower () == "gpu":
    print ("Correct! ")
    score +=1
else:
    print ("incorrect")


answer = input ("What does ram stand for? ")
if answer.lower () == "ram":
    print ("Correct! ")
    score +=1
else:
    print ("incorrect")


answer = input ("What does psu stand for? ")
if answer.lower () == "psu":
    print ("Correct! ")
    score +=1
else:
    print ("incorrect")

print ("You got " + str (score) + " questions right!")
print ("You got " + str((score/4)*100) + "%")