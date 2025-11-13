# Start with a list of strings (e.g., fruits).
fruits = ["apple", "watermelon", "raspberry", "strawberry", "banana", "cantaloupe"]

# Use list comprehension to create a separate list
# containing only the first letter of those strings.
first_letters = [fruit[0] for fruit in fruits]

print(first_letters)

temps_C = [0, 100, -40]
temps_F = []
for temp in temps_C:
    temps_F.append(temp * 9/5 + 32)

print(temps_F)

temps_F = [temp * (9/5) + 32 for temp in temps_C]
print(temps_F)

emails = ["asdfasdf@gmail.com", "asfasdf@isu.edu", "fasdf@isu.edu", "adsf@msn.com"]
print([address for address in emails if address[-4:] == ".edu"])

filenames = ["untitled.doc","untitled.pdf","untitled.txt"]
print([string[string.find('.')+1:] for string in filenames])

strings = ["racecar", "abcdedcba", "Hello!", "I'm not a palindrome"]
print([string for string in strings if string == string[::-1]])
print(["x" for _ in strings])

sentence = ["Marley", "was", "dead", "to", "begin", "with"]
print([word for word in sentence if len(word)%2 == 0])

even_len_words = []
for word in sentence:
    if len(word) % 2 == 0:
        even_len_words.append(word)

print(even_len_words)
