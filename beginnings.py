
#Here's a small intro for the game, haha
import time
intro = ["Magnet High School is a prestigious STEM school focused on the discipline of engineering.\n",
"Hundreds of students compete vigorously in the selective admission process to be enrolled in the school and further their education in hopes of becoming productive members of society in their near futures.\n",
"Except...\n",
"Once in the school, some of these once restful, dutiful students...\n",
"if ever dutiful at all...\n",
"become stress-induced, procrastinating balls of sadness.\n",
"Congrats! You are one of these pitiful students, and you are trying to skirt by yet another week of homework.\n",
"Try to get your work done while also maintaining your energy and happiness!\n\n"]
for line in intro:
    print(line, end="")
    time.sleep(3)


#each character has different stats of base energy, work done per click, and base happiness; the base for all these traits, respectively, is 50, 5, 50
class Magneteer:

    def __init__(self, energy, work, happiness):
        self.energy = energy
        self.work = work
        self.happiness = happiness

owl = Magneteer(70, 4, 50)
genius = Magneteer(50, 7, 40)
studious = Magneteer(40, 5, 70)

print("What type of Magneteer are you? \n")
print(f"(1)The Night Owl can stay up to do more work, but they work more slowly. They start off with {owl.energy} energy and {owl.happiness} happiness, and get {owl.work} work done per click.")
print(f"(2)The MIT Genius can work quickly, but they tend to procratinate more. They start off with {genius.energy} energy and {genius.happiness} happiness, and get {genius.work} work done per click.")
print(f"(3)The Studious Student has less energy, but doesn't procrastinate as much. They start off with {studious.energy} energy and {studious.happiness} happiness, and get {studious.work} work done per click.")

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
















