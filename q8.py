"""Check the punctation if its interrogative, declarative, or other."""

sentence_types = {
    "interrogative": "?",
    "declarative": ".",
    "exclamatory": "!"
}

sentence = input("Enter a sentence: ")

last_char = sentence[-1]

for type in sentence_types:
    if sentence_types[type] == last_char:
        print(f"Sentence is {type}.")
