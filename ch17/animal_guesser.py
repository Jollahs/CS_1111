# Write a program with an animal class in which
import random

class Animal:
    def __init__(self, name, num_legs, diet, type, size, color):
        self.name = name
        self.num_legs = num_legs
        self.diet = diet # omnivore, herbivore, carnivore
        self.type = type # bird, mammal, reptile, or amphibian
        self.size = size
        self.color = color

    def __str__(self):
        return self.name



animals = [
    Animal("African Elephant", 4, "herbivore", "mammal", "large", "gray"),
    Animal("Bald Eagle", 2, "carnivore", "bird", "medium", "brown/white"),
    Animal("Green Iguana", 4, "herbivore", "reptile", "medium", "green"),
    Animal("American Bullfrog", 4, "carnivore", "amphibian", "small", "green"),
    Animal("Cheetah", 4, "carnivore", "mammal", "medium", "spotted"),
    Animal("Blue Whale", 0, "carnivore", "mammal", "large", "blue"),
    Animal("Koala", 4, "herbivore", "mammal", "small", "gray"),
    Animal("Komodo Dragon", 4, "carnivore", "reptile", "large", "brown"),
    Animal("Penguin", 2, "carnivore", "bird", "medium", "black/white"),
    Animal("Red Fox", 4, "omnivore", "mammal", "small", "red"),
    Animal("Giraffe", 4, "herbivore", "mammal", "large", "yellow/brown"),
    Animal("Tiger", 4, "carnivore", "mammal", "large", "orange/black"),
    Animal("Kangaroo", 2, "herbivore", "mammal", "medium", "brown"),
    Animal("Polar Bear", 4, "carnivore", "mammal", "large", "white"),
    Animal("Mountain Goat", 4, "herbivore", "mammal", "medium", "white"),
    Animal("Alligator", 4, "carnivore", "reptile", "large", "green"),
    Animal("Snowy Owl", 2, "carnivore", "bird", "medium", "white"),
    Animal("Hummingbird", 2, "omnivore", "bird", "tiny", "green/red"),
    Animal("Siberian Husky", 4, "omnivore", "mammal", "medium", "gray/white"),
    Animal("Salamander", 4, "carnivore", "amphibian", "small", "black/yellow"),
    Animal("Moose", 4, "herbivore", "mammal", "large", "brown"),
    Animal("Python Snake", 0, "carnivore", "reptile", "medium", "brown"),
    Animal("Toucan", 2, "omnivore", "bird", "small", "black/yellow"),
    Animal("Chimpanzee", 4, "omnivore", "mammal", "medium", "black"),
    Animal("Orangutan", 4, "omnivore", "mammal", "medium", "orange"),
    Animal("Arctic Hare", 4, "herbivore", "mammal", "small", "white"),
    Animal("Grizzly Bear", 4, "omnivore", "mammal", "large", "brown"),
    Animal("Peacock", 2, "omnivore", "bird", "medium", "blue/green"),
    Animal("Ostrich", 2, "omnivore", "bird", "large", "brown/white"),
    Animal("Rattlesnake", 0, "carnivore", "reptile", "small", "tan"),
    Animal("Sea Turtle", 4, "omnivore", "reptile", "medium", "green"),
    Animal("Axolotl", 4, "carnivore", "amphibian", "small", "pink"),
    Animal("Horse", 4, "herbivore", "mammal", "large", "brown"),
    Animal("Zebra", 4, "herbivore", "mammal", "medium", "black/white"),
    Animal("Raccoon", 4, "omnivore", "mammal", "small", "gray/black"),
    Animal("Parrot", 2, "omnivore", "bird", "small", "green/red"),
    Animal("Gorilla", 4, "herbivore", "mammal", "large", "black"),
    Animal("Hippopotamus", 4, "herbivore", "mammal", "large", "gray"),
    Animal("Red Panda", 4, "omnivore", "mammal", "small", "red/white"),
    Animal("Armadillo", 4, "omnivore", "mammal", "small", "brown"),
    Animal("Sloth", 4, "herbivore", "mammal", "medium", "brown"),
    Animal("Blue Poison Dart Frog", 4, "carnivore", "amphibian", "tiny", "blue/black"),
    Animal("King Cobra", 0, "carnivore", "reptile", "medium", "brown"),
    Animal("Falcon", 2, "carnivore", "bird", "small", "gray/white"),
    Animal("Puffin", 2, "carnivore", "bird", "small", "black/white"),
    Animal("Bison", 4, "herbivore", "mammal", "large", "brown"),
    Animal("Hyena", 4, "carnivore", "mammal", "medium", "spotted"),
    Animal("Meerkat", 4, "omnivore", "mammal", "small", "tan"),
    Animal("Beaver", 4, "herbivore", "mammal", "small", "brown"),
    Animal("Mallard Duck", 2, "omnivore", "bird", "small", "green/brown"),
    Animal("Flamingo", 2, "omnivore", "bird", "large", "pink"),
    Animal("Tapir", 4, "herbivore", "mammal", "medium", "black/white"),
    Animal("Ocelot", 4, "carnivore", "mammal", "small", "spotted"),
    Animal("Jackrabbit", 4, "herbivore", "mammal", "small", "brown"),
    Animal("Crocodile", 4, "carnivore", "reptile", "large", "green"),
    Animal("Stingray", 0, "carnivore", "mammal", "medium", "gray"),
    Animal("Black Bear", 4, "omnivore", "mammal", "large", "black"),
    Animal("Sea Lion", 2, "carnivore", "mammal", "medium", "brown"),
    Animal("Wolverine", 4, "omnivore", "mammal", "small", "brown/black"),
    Animal("Llama", 4, "herbivore", "mammal", "medium", "white"),
    Animal("Emu", 2, "omnivore", "bird", "large", "brown"),
    Animal("Mako Shark", 0, "carnivore", "mammal", "large", "blue/gray"),
    Animal("Weasel", 4, "carnivore", "mammal", "small", "brown"),
    Animal("Okapi", 4, "herbivore", "mammal", "medium", "brown/white"),
    Animal("Badger", 4, "omnivore", "mammal", "small", "black/white"),
    Animal("Quail", 2, "omnivore", "bird", "tiny", "brown"),
    Animal("Swan", 2, "herbivore", "bird", "medium", "white"),
    Animal("Cougar", 4, "carnivore", "mammal", "large", "tan"),
    Animal("Antelope", 4, "herbivore", "mammal", "medium", "brown"),
    Animal("Gecko", 4, "carnivore", "reptile", "tiny", "green"),
    Animal("Chameleon", 4, "omnivore", "reptile", "small", "various"),
    Animal("Boar", 4, "omnivore", "mammal", "medium", "brown"),
    Animal("Caribou", 4, "herbivore", "mammal", "large", "brown"),
    Animal("Bat", 2, "omnivore", "mammal", "small", "black"),
    Animal("Manatee", 0, "herbivore", "mammal", "large", "gray"),
    Animal("Pelican", 2, "carnivore", "bird", "medium", "white"),
    Animal("Snow Leopard", 4, "carnivore", "mammal", "medium", "gray/black"),
    Animal("Raven", 2, "omnivore", "bird", "small", "black"),
    Animal("Starling", 2, "omnivore", "bird", "tiny", "iridescent"),
    Animal("Marmot", 4, "herbivore", "mammal", "small", "brown"),
    Animal("Fennec Fox", 4, "omnivore", "mammal", "small", "tan"),
    Animal("Tortoise", 4, "herbivore", "reptile", "small", "brown"),
    Animal("Vulture", 2, "carnivore", "bird", "medium", "brown"),
    Animal("Lobster", 8, "omnivore", "mammal", "small", "red"),
    Animal("Octopus", 8, "carnivore", "mammal", "medium", "purple"),
    Animal("Jellyfish", 0, "carnivore", "mammal", "medium", "transparent"),
    Animal("Porcupine", 4, "herbivore", "mammal", "small", "brown"),
    Animal("Walrus", 2, "carnivore", "mammal", "large", "brown"),
    Animal("Hawk", 2, "carnivore", "bird", "small", "brown"),
    Animal("Lynx", 4, "carnivore", "mammal", "medium", "gray"),
    Animal("Goose", 2, "omnivore", "bird", "medium", "white"),
    Animal("Ibis", 2, "omnivore", "bird", "small", "white"),
    Animal("Squirrel", 4, "omnivore", "mammal", "small", "gray"),
    Animal("Bobcat", 4, "carnivore", "mammal", "medium", "tan"),
    Animal("Alpaca", 4, "herbivore", "mammal", "medium", "cream"),
    Animal("Mandrill", 4, "omnivore", "mammal", "medium", "multicolored"),
    Animal("Seal", 2, "carnivore", "mammal", "medium", "gray"),
    Animal("Barracuda", 0, "carnivore", "mammal", "medium", "silver")
]

possibilities = animals[:]

#TODO: find a better way to avoid asking the same question multiple times that
# also allows the program to know when to quit
questions_asked = []

# the computer asks the user to think of an animal
# (one that appears in its database) and
while len(possibilities) > 5:

    # pick a random criteria
    chosen_criteria = random.randrange(5)

    # pick a random animal that's still a possibility and use its value for the criteria
    chosen_value = "UNSET"
    if chosen_criteria == 0:
        chosen_value = random.choice(possibilities).num_legs
    elif chosen_criteria == 1:
        chosen_value = random.choice(possibilities).diet
    elif chosen_criteria == 2:
        chosen_value = random.choice(possibilities).type
    elif chosen_criteria == 3:
        chosen_value = random.choice(possibilities).size
    elif chosen_criteria == 4:
        chosen_value = random.choice(possibilities).color

    question  = f"Does {chosen_value} describe your animal (Y/N)? "

    if question in questions_asked:
        continue

    # then asks the user questions
    response = input(question)
    questions_asked.append(question)


    if response == "Y":
        # remove all animals where diet isn't carnivore
        for i in reversed(range(len(possibilities))):
            if chosen_criteria == 0:
                if possibilities[i].num_legs != chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 1:
                if possibilities[i].diet != chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 2:
                if possibilities[i].type != chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 3:
                if possibilities[i].size != chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 4:
                if possibilities[i].color != chosen_value:
                    del possibilities[i]
    else:
        # remove all animal where diet is carnivore
        for i in reversed(range(len(possibilities))):
            if chosen_criteria == 0:
                if possibilities[i].num_legs == chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 1:
                if possibilities[i].diet == chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 2:
                if possibilities[i].type == chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 3:
                if possibilities[i].size == chosen_value:
                    del possibilities[i]
            elif chosen_criteria == 4:
                if possibilities[i].color == chosen_value:
                    del possibilities[i]

# until it narrows down which animal the user is thinking of
print(f"Is your animal one of these {len(possibilities)}? ")
print("\n".join([str(animal) for animal in possibilities]))
