#bits and bobs of various functions/other things to be added

#each character has different stats of base energy, work done per click, and base happiness
class Magneteer:

    def __init__(self, energy, work, happiness):
        self.energy = energy
        self.work = work
        self.happiness = happiness

owl = Magneteer(70, 4, 50)
genius = Magneteer(50, 7, 40)
studious = Magneteer(40, 5, 60)

print("Choose your character!/n")
print(f"The Night Owl character can stay up to do more work, but they work more slowly. They start off with {owl.energy} energy and {owl.happiness} happiness, and get {owl.work} work done per click.")
print(f"The MIT Genius character can work quickly, but they tend to procratinate more. They start off with {genius.energy} energy and {genius.happiness} happiness, and get {genius.work} work done per click.")
print(f"The Studious Student character has less energy, but doesn't procrastinate as much. They start off with {studious.energy} energy and {studious.happiness} happiness, and get {studious.work} work done per click.")