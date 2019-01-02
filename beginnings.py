#Intro?
#Here's a small intro for the game, haha
import time
intro = ["Magnet High School is a prestigious STEM school focused on the discipline of engineering.\n",
"Hundreds of students compete vigorously in the selective admission process to be enrolled in the school and further their education in hopes of becoming productive members of society in their near futures.\n",
"Except...\n",
"Once in the school, some of these once restful, dutiful students...",
"if ever dutiful at all...",
"become stress-induced, procrastinating balls of sadness.\n",
"Congrats! You are one of these pitiful students, and you are trying to skirt by yet another week of homework.\n",
"Try to get your work done while also maintaining your energy, by eating, and happiness, by procrastinating!"]
for line in intro:
    print(line, end="")
    time.sleep(3)
print("\n")

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


















