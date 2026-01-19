print ("Hi, welcome to Buzzfeed. ")
print ("Are you ready to test your love for Josh O'Connor? ")
ready = input ("Let's see how well you know him!!!  ")

if ready.lower() != "yes":
    print ("It's alright. Have nice day! ")
    quit()

print ("Alright, let's get our knives sharpened!! ")
score = 0

answer = int(input("How old was Josh O'Connor when he first joined 'The Crown'? "))
if answer == 28:
    print ("That's right. ")
    score += 1
else:
    print ("Sorry. It's 28")


answer = input("What was Josh O'Connor's first religious job? ")
if answer.lower() == "alterboy":
    print ("Great job!")
    score += 1
else:
    print ("No. He was an alterboy as a child")


answer = input("Who did Josh O'Connor's played in 'Cinderella'? ")
if answer.lower() == "ballroom palace guard":
    print ("Yesss.")
    score += 1
else:
    print ("Not really. It's Ballroom Palace Guard")

print ("Congratulations!! You got " + str (score) + " questions right! You truly know a 'Masterpiece', when you see one. ")