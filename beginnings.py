
#Here's a small intro for the game, haha
import time
import random
intro = ["Magnet High School is a prestigious STEM school focused on the discipline of engineering.\n",
"Hundreds of students compete vigorously in the selective admission process to be enrolled in the school and further their education in hopes of becoming productive members of society in their near futures.\n",
"Except...\n",
"Once in the school, some of these once restful, dutiful students...\n",
"if ever dutiful at all...\n",
"become stress-induced, procrastinating balls of sadness.\n",
"Congrats! You are one of these pitiful students, and you are trying to skirt by yet another week of homework.\n",
"Try to get your work done while also maintaining your energy and happiness!\n\n"]
#for line in intro:
    #print(line, end="")
    #time.sleep(3)
#print("-----------------")

#each character has different stats of base energy, work done per click, and base happiness; the base for all these traits, respectively, is 50, 5, 50
class Magneteer:

    def __init__(self, name, energy, work, happiness):
        self.name = name
        self.energy = energy
        self.work = work
        self.happiness = happiness

    def stats(self):
        global WORK
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        #note: Unicode used to bold the numbers
        print(f"""
        You have:
        \033[1m{WORK}\033[0m  work done out of 50
        \033[1m{ENERGY}\033[0m energy left
        \033[1m{HAPPINESS}\033[0m happiness
        \033[1m{NUM_CLICKS}\033[0m clicks left""")
        print("\n")
        #if work/happiness/num_clicks low, give a warning

    def work(self):
        global WORK
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        print("You do some work.\n")
        WORK += self.work
        ENERGY -= 3
        HAPPINESS -= 2
        NUM_CLICKS -= 1

    def eat(self):
        global ENERGY
        global NUM_CLICKS
        eating = ["Mother made some porridge, how nice.", "Crackers and cheese replenish your soul.", "Let's take a break for some grapes.", "You eat a cinnamon bun. It's sweet, just like you <3.", "Mmmm, sesame candy...", "You...drink some water? That's it? Ok..."]
        print("You eat something.", end=" ")
        print(random.choice(eating))
        ENERGY += 2
        NUM_CLICKS -= 1

    def sleep(self):
        global NUM_CLICKS
        global ENERGY
        print("You catch a few winks. But at what cost? You lost some clicks to do your work!")
        ENERGY += 4
        NUM_CLICKS -= random.randint(3,6)

    def procrastinate(self):
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        pro = ["You take a break to browse Twitter. You laugh at another stupid Trump tweet.", "You doodle on the edge of your pa- wait, no, you just finished a fully colored illustration...", "WAIT, IS THERE A NEW EPISODE OF *insert fave show*!!??-", "You literally just sit there and stare at your paper, trying to empty your mind of stress. It kinda works, but not really.", "You really just wanna play Smash Ultimate, so you do. Isabelle's sweet smile makes it all worth it."]
        print("You procrastinate.", end=" ")
        print(random.choice(pro))
        ENERGY -= 2
        HAPPINESS += 1
        NUM_CLICKS -= 1

characters = {
    "owl": Magneteer("Night Owl", 70, 4, 50),
    "genius": Magneteer("MIT Genius", 50, 7, 40),
    "studious": Magneteer("Studious Student", 40, 5, 70)}

#print("What type of Magneteer are you? \n")
time.sleep(3)
#I have used Unicode to bold certain words
print(f"★★ The \033[1m Night Owl \033[0m can stay up to do more work, but they work more slowly. They start off with {characters['owl'].energy} ENERGY and {characters['owl'].happiness} HAPPINESS, and get {characters['owl'].work} WORK done per click.\n")
time.sleep(3)
print(f"★★ The \033[1m MIT Genius \033[0m can work quickly, but they tend to procratinate more. They start off with {characters['genius'].energy} ENERGY and {characters['genius'].happiness} HAPPINESS, and get {characters['genius'].work} WORK done per click.\n")
time.sleep(3)
print(f"★★ The \033[1m Studious Student \033[0m has less energy, but doesn't need to procrastinate as much. They start off with {characters['studious'].energy} ENERGY and {characters['studious'].happiness} HAPPINESS, and get {characters['studious'].work} WORK done per click.\n")
time.sleep(3)

char = input("So, how do you work? (owl)(genius)(studious)\n")

print(f"\nNice! So you're the {characters[char].name} type, huh?\n")

NUM_CLICKS = 50
WORK = 0
ENERGY = characters[char].energy
HAPPINESS = characters[char].happiness

for x in range(10):
    characters[char].procrastinate()
    characters[char].stats()

#THE GAME PLAN FROM HERE
#player  input to choose a character
#set default values for ENERGY(100), WORK(0), and HAPPINESS(100)
#within the Magneteer class, create functions to perform Work, Procrastinate, Nap, Eat, Cry
#for ex. def work(): ENERGY -=2, WORK +=2, HAPPINESS -=1
#for ex. def procrastinate(): ENERGY -=1, HAPPINESS +=2
#for ex. def cry(): print("A simple calculus problem managed to hurl you into a fury of tears. You feel only slightly better."), HAPPINESS += 1 **PERHAPS MAKE THE CRY FUNCTION RANDOMLY AFFECT A VARIABLE (i.e might bring up/down energy, or up/down work)
#for one night, create a function(outside of Magneteer class) that contains a loop of user inputs (loop lasts for 120 or so turns?)
#when user types "w" perform Work function once, when user types "c" perform cry function once
#at end of # of turns, if work points are at 100, player wins, if 100>p>80, player wins, but with penalty for next night, if less than 80, player loses
#do the same for happiness and energy (however, whether or not the player wins the night is not determined by these, they can only add a penalty for the next night)
#make a loop to play a "night" five times, for each day of the week
#...still don't know how to determine overall win/lose, perhaps total_points=0, and at the end of every night your performance gives you a # of points; at the end of the game, points added up and result in a "grade" (ex. A for excellent, F for fail)
#OOF














