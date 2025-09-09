name1 = input("Please give me a name: ")
num1 = int(input("Give me an integer: "))
pounds_per_pail_of_water = 8.34

story = name1 + " and Jill went up the hill\nto fetch " + str(num1) +\
        " pail(s) of water (collectively weighing " +\
        str(num1 * pounds_per_pail_of_water) + " pounds).\n" + name1 +\
        " fell down and broke his crown,\nand Jill came tumbling after."

print(story)
