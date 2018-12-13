# Simple adventure game for day 3.
hero = input("Name your hero. ")
print("\n" + hero + " has to save their friend from the shark infested waters.")
print("What do they do?")
print("A. Throw a bag of salt and pepper in the water?")
print("B. Drink up the whole ocean?")
print("C. Do nothing.\n")
option = input("What do they do? Type in an option. ");
if(option == "A"):
    print("Great! Theyjust seasoned their friend so the sharks will have a " +
          "delicious lunch!")
elif(option == "B"):
    print("Their body can't handle that? Where does their pee go?")
elif(option == "C"):
    print("Correct. Sharks are actually not that dangerous! " + 
          "Just tell their friend to relax.")
else:
    print("That option is not valid.")