#Here's a small intro for the game, haha
import time
import random
print("""
WELCOME TO
+= 𝕄𝕒𝕘𝕟𝕖𝕥ℂ𝕝𝕚𝕜 =+
""")
time.sleep(2)
intro = ["Magnet High School is a prestigious STEM school focused on the discipline of engineering.\n",
"Hundreds of students compete vigorously in the selective admission process to be enrolled in the school and further their education in hopes of becoming productive members of society in their near futures.\n",
"Except...\n",
"Once in the school, some of these once restful, dutiful students...\n",
"if ever dutiful at all...\n",
"become stress-induced, procrastinating balls of sadness.\n",
"Congrats! You are one of these pitiful students, and you are trying to skirt by yet another week of homework.\n",
"Try to get your WORK done while also maintaining your ENERGY and HAPPINESS!\n\n"]
for line in intro:
    print(line, end="")
    time.sleep(2)
print("-----------------")

class Magneteer:

    def __init__(self, name, energy, work, happiness):
        """A class to create Magnet students; each of which has a name and different stats of base energy, work done per click, and base happiness; This class also contains to functions to perform different tasks to raise/lower different stats"""
        self.name = name
        self.energy = energy
        self.work = work
        self.happiness = happiness

    def stats(self):
        """A function to display your progress throughout the game"""
        global WORK
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        if WORK > 150:
            WORK = 150
        if ENERGY < 0:
            ENERGY = 0
        if HAPPINESS < 0:
            HAPPINESS = 0
        if NUM_CLICKS < 0:
            NUM_CLICKS = 0
        #note: Unicode used to bold the numbers
        print(f"""
        You have:
        \033[1m{WORK}\033[0m WORK done out of 150
        \033[1m{ENERGY}\033[0m ENERGY left
        \033[1m{HAPPINESS}\033[0m HAPPINESS left
        \033[1m{NUM_CLICKS}\033[0m CLICKS left""")
        #A warning is issued if any of your stats are too low
        if WORK < 150:
            if ENERGY <= 5:
                print("Woah, there buddy; you're low on ENERGY. Maybe you should sleep(s) or eat(e)?")
            if HAPPINESS <= 5:
                print("Uh oh, your HAPPINESS is running a bit low and it's getting ya down. Take a break and procrastinate(p) a little, huh?")
            if NUM_CLICKS <= 10:
                print("You're running out of CLICKS there, man! Prioritize getting that WORK done!!")
        print("\n")

    def working(self):
        """A function to do an amount of work, the rate of which is different for every character; other stats also go down as a result"""
        global WORK
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        hw = ["UGH, inverse derivatives.", "It's just some simple stochiometry.", "AutoCAD can be relaxing. OnShape on the other hand...", "Seems like you're the only one working on this group project :/.", "Trabajas en la presentación del pan de Cuba.", "You work on the coding midterm proj- wait, wait a minute here...", "Since when does gym give written homework!!??", "The usual ten pages of history, except for some reason, it's actually fifteen...Drats.", "It's physics...yay...", "You write a poem for literature about memes. Didn't she say it had to be serious? Oh well."]
        print(f"You do some WORK. \033[1m{random.choice(hw)}\033[0m")
        WORK += self.work
        ENERGY -= 3
        HAPPINESS -= 2
        NUM_CLICKS -= 1

    def eat(self):
        """A function to eat and restore energy"""
        global ENERGY
        global NUM_CLICKS
        eating = ["Mother made some porridge, how nice.", "Crackers and cheese replenish your soul.", "Let's take a break for some grapes.", "You eat a cinnamon bun. It's sweet, just like you <3.", "Mmmm, sesame candy...", "You...drink some water? That's it? Ok...", "GUAVA CANDIES!!", "Hot cheetos, hot cheetos, what would we do without you?", "A damn napkin, because you just don't care anymore.", "You have Lunchables because you're just totally rad like that B).", "Apple slices and caramel, classy.", "You inhale half a pack of Oreos...That can't be healthy..."]
        print(f"You eat something. \033[1m{random.choice(eating)}\033[0m")
        ENERGY += 3
        NUM_CLICKS -= 1

    def sleep(self):
        """A function to sleep and restore a large amount of energy, but lose a random amount of clicks from 3-5"""
        global NUM_CLICKS
        global ENERGY
        dreams = ["acing that physics lab report", "absolutely bombing that chem-co quiz", "hanging out in the senior lounge with your best buds, but you aren't seniors, so it's clandestine :O", "the lunch room actually being big enough to accomodate everyone who goes there to eat", "being Mr.Sanservino's favorite student", "Mr. Nowakoski coming back and abolishing vocab quizzes like the god he is", "some freshman crushing on you. Pffft, like they have a chance", "INTERIOR CROCODILE ALLLIGATOR, I DRIVE A CHEVROLET MOVIE THEATRE", "KITTIES"]
        print(f"You catch a few winks and dream about \033[1m{random.choice(dreams)}\033[0m. But at what cost? You lost some CLICKS to do your WORK!")
        ENERGY += 5
        NUM_CLICKS -= random.randint(3,5)

    def procrastinate(self):
        """A function to procrastinate and restore happiness; lowers energy and number of clicks"""
        global ENERGY
        global HAPPINESS
        global NUM_CLICKS
        pro = ["You take a break to browse Twitter. You laugh at another stupid Trump tweet.", "You doodle on the edge of your pa- wait, no, you just finished a fully colored illustration...", "WAIT, IS THERE A NEW EPISODE OF *insert fave show*!!??-", "You literally just sit there and stare at your paper, trying to empty your mind of stress. It kinda works, but not really.", "You really just wanna play Smash Ultimate, so you do. Isabelle's sweet smile makes it all worth it.", "You have a lovely conversation about pigeons with the disembodied gentlemanly voice that lives in your head. He somehow changes the subject to that of long-awaited revenge, but you decide that's enough chit-chat for today.", "You play tickles with your pet.", "Acting on random impulse, you vacuum your entire room and rearrange your Devilman figurine collection."]
        print(f"You procrastinate. \033[1m{random.choice(pro)}\033[0m")
        ENERGY -= 2
        HAPPINESS += 3
        NUM_CLICKS -= 1

    def cry(self):
        """A function to cry which has a 50/50 chance of either increasing or decreasing your happiness"""
        global HAPPINESS
        global NUM_CLICKS
        p = [1, 2]
        pp = random.choice(p)
        if pp == 1:
            print("\033[1mYou get a bit overwhelmed and some tears come a-flowing. But that's understandable, it can get stressful sometimes. You feel a bit better afterward.\033[0m")
            HAPPINESS += 3
        else:
            print("\033[1mA simple problem and a brain fart manage to hurl you into a fury of tears. You feel worse now. Oh no.\033[0m")
            HAPPINESS -= 3
        NUM_CLICKS -= 1

#A dictionary to contain the three characters and make it easy to select them
characters = {
    "owl": Magneteer("Night Owl", 70, 5, 50),
    "genius": Magneteer("MIT Genius", 50, 8, 30),
    "studious": Magneteer("Studious Student", 30, 7, 70)}

#A short description of each character type
print("What type of Magneteer are you? \n")
time.sleep(2)
#I have used Unicode to bold certain words
print(f"★★ The \033[1m Night Owl \033[0m can stay up to do more WORK, but they WORK more slowly. They start off with {characters['owl'].energy} ENERGY and {characters['owl'].happiness} HAPPINESS, and get {characters['owl'].work} WORK done per click.\n")
time.sleep(2)
print(f"★★ The \033[1m MIT Genius \033[0m can WORK quickly, but they tend to procratinate more. They start off with {characters['genius'].energy} ENERGY and {characters['genius'].happiness} HAPPINESS, and get {characters['genius'].work} WORK done per click.\n")
time.sleep(2)
print(f"★★ The \033[1m Studious Student \033[0m has less ENERGY, but doesn't need to procrastinate as much. They start off with {characters['studious'].energy} ENERGY and {characters['studious'].happiness} HAPPINESS, and get {characters['studious'].work} WORK done per click.\n")
time.sleep(2)

#player chooses what character to play as
char = input("So, how do you WORK? (owl)(genius)(studious)\n").lower()
while char not in characters:
    char = input("So, how do you WORK? (owl)(genius)(studious)\n").lower()

print(f"\nNice! So you're the {characters[char].name} type, huh?\n")
time.sleep(2)

#To count how many wins you get; max is 5
WINS = 0

#Quick directions on how to play the game
directions = ["Directions:", "Press (w) to work", "Press (e) to eat", "Press (s) to sleep", "Press (p) to procrastinate", "Press (c) to... cry", "Be careful, sleeping and crying may have some consequences...", "Stragetize! You've only got 50 CLICKS to get it done, so use 'em wisely!", "Try not to lose! Depleting your ENERGY or HAPPINESS completely will cause you to start the next night with lower ENERGY/HAPPINESS!", "Let's begin the week!"]
for line in directions:
    print(line)
    time.sleep(1)
print("\n")

#This is the base of the hidden repurcussion stat(explained below)
repurcussion_E = 0
repurcussion_H = 0

#For each day of the week, a "night" is played (a loop of 5 turns); there is a different "start game" line depending on the day
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
for day in days:
    if day == 'Monday':
        print("The weekend's just ended, darn... It's Monday night. Let's get to WORK!")
    elif day == 'Friday':
        print("It's the last night for this week, Friday! Let's get to WORK and make it count!")
    else:
        print(f"It's the next night, {day}. Let's get to WORK!")
    time.sleep(2)

    #Stats reset for every night
    NUM_CLICKS = 50
    WORK = 0
    ENERGY = characters[char].energy
    HAPPINESS = characters[char].happiness

    #repurcussion is a stat that determines a penalty on energy/happiness for the night if the previous night was failed
    if repurcussion_E == 1:
        ENERGY -= 10
        print("You lost all your ENERGY last night, and you're still a bit tired. You start this night with 10 less ENERGY!")
        time.sleep(2)
    if repurcussion_H == 1:
        HAPPINESS -= 10
        print("You lost all your HAPPINESS last night, and you're still a bit down. You start this night with 10 less HAPPINESS!")
        time.sleep(2)
    #repurcussion resets as well
    repurcussion_E = 0
    repurcussion_H = 0

    #Within "weekday loop" there is a loop of at most 50 turns(the max number of "clicks") that asks the player what action to perform until work is completed or a stat is depleted
    while WORK < 150:
        if NUM_CLICKS <= 0:
            print("Fiddlesticks! You ran out of CLICKS to do your WORK!\n")
            break
        if ENERGY <= 0:
            print("Aw, rats, your ENERGY... I- I think you passed out from exhaustion, dude.\n\n")
            repurcussion_E = 1
            break
        if HAPPINESS <=0:
            print("You let your HAPPINESS deplete, and you broke down in tears from the mounting stress on your shoulders...I think you need a break...")
            repurcussion_H = 1
            break
        action = input("What do you want to do?\n").lower()
        if action == "w":
            characters[char].working()
            characters[char].stats()
        elif action == "e":
            characters[char].eat()
            characters[char].stats()
        elif action == "s":
            characters[char].sleep()
            characters[char].stats()
        elif action == "p":
            characters[char].procrastinate()
            characters[char].stats()
        elif action == "c":
            characters[char].cry()
            characters[char].stats()

    #When work is complete or a stat is depleted, a win or lose line is displayed, respectively; the lose line is different if the day is Friday
    time.sleep(2)
    if WORK == 150:
        print("Homework COMPLETED! You finished all of your night's WORK, with your sanity still intact! Well, mostly intact...\n")
        WINS += 1
    else:
        if day == 'Friday':
            print("Homework INCOMPLETE! You've still got calc to do, but with the weekend ahead, you've got time......Sunday night it is!\n")
        else:
            print("Homework INCOMPLETE! There's still a worksheet to be done, but let's just hope tomorrow's co is enough time to get it done...\n")
    time.sleep(3)

print(".")
time.sleep(1)
print(".")
time.sleep(1)
print(".")
time.sleep(1)
print("\n")

#Total win nights are counted up, and depending on how many wins the player gets, they receive a different "grade"; you cannot earn a 100, because life's not fair sometimes, bro
print(f"Well, {characters[char].name}, you've completed {WINS} day's work out of 5.")
if WINS == 0:
    print("LMAO buddy, you ok? You got a whole-ass 0 on, like, EVERY assignment. Like, were you just playing Deltarune the entire week or something? How did you even get into Magnet??")
elif WINS == 1:
    print("You got a..54? Just didn't care, huh? Can't blame ya, I guess, who needs to know what a derivative is, amirite? ...No, actually, I'm really disappointed in you; please try harder next time, sweety.")
elif WINS == 2:
    print("Welp, that's a 68 in your gradebook, lmao. Just wasn't your luck, huh? Eh, you've still got a week till the marking period ends. Hopefully, there's some extra credit oppurtunities...")
elif WINS == 3:
    print("OOF, that there's a 75 perciento. Lo siento, but you've gotta do better than that! Maybe Señora will extended the due date, and you can cop some extra puntos.")
elif WINS == 4:
    print("Ok, ok, you got a 92. Not too shabby for bum-rushing that chem packet at one in the morning. Good job! (I mean the grade, not the procrastination)")
elif WINS == 5:
    print("Ayyyyyyyyyyyyyyyy, 98 FOR. THE. WIN!!! Haha, yEET, dab on 'em......*ahem* Congratulations on your grade, keep up the good work.")






