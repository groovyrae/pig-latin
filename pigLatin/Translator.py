
def translate(word):
    translation = ""
    # for a word beginning with a vowel
    for letter in word[0]:
        if letter in "aeiou":
            translation = translation + word + "way"
            return translation
    # for a word beginning with two consonants
    for letter in word[1]:
        if letter in "bcdfghjklmnpqrstvwxz":
            translation = translation + word[2:] + word[:2] + "ay"
            return translation
    # for a word beginning with one consonant
    for letter in word[0]:
        if letter in "bcdfghjklmnpqrstvwxyz":
            translation = translation + word[1:] + word[:1] + "ay"
            return translation


print("*note: compound words must be translated separately!*")
print(translate(input("Enter a word: ")))

while input("To translate another word, enter 'repeat': ") == "repeat":
    print(translate(input("Enter a word: ")))
else:
    if input("To end translation, enter 'stop': ") == "stop":
        print("\U0001F389" " You have completed the use of the Pig Latin Translator " "\U0001F389")
        print("            Have a busting rest of your day/night" + " \U0001F608")
        print("                            ~Raégen" + "\U0001F31A")
    else:
        while input("To translate another word, enter 'repeat': ") == "repeat":
            print(translate(input("Enter a word: ")))
        if input("To end translation, enter 'stop': ") == "stop":
            print("\U0001F389" " You have completed the use of the Pig Latin Translator " "\U0001F389")
            print("            Have a busting rest of your day/night" + " \U0001F608")
            print("                            ~Raégen" + "\U0001F31A")
