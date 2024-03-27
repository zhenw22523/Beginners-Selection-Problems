print ("Welcome!")
ans1 = input("You come across a lake.\nDo you want to swim across, or wait for a boat? (swim/wait)\n>>")
if ans1 == "swim":
    print ("You get eaten by a hungry shark. Game over.")
elif ans1 == "wait":
    print ("A boat arrives and you arrive at the island safely. ")
    ans2 = input("You come to a cave.\nDo you want to venture inside or walk on? (venture/walk)\n>>")
    if ans2 == "venture":
        print ("You are squished by boulders never to be seen again. Game over.")
    elif ans2 == "walk":
        ans3 = input("You're at a crossroads.\nDo you go left, right, or straight? (left/right/straight)\n>>")
        if ans3 == "left":
            print ("You are trampled by a herd of wildebeest. Game over.")
        elif ans3 == "straght":
            print ("You get stung by a poisonous wasp. Game over.")
        elif ans3 == "right":
            print ("You march on and find the buried treasure! Yippee!!")

