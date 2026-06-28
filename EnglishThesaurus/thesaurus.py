import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
        #return data.get(word, [word])
    elif len(get_close_matches(word, data.keys())) > 0:
        close_match = get_close_matches(word, data.keys())[0]
        response = input(f"Did you mean '{close_match}' instead? Enter Y if yes, or N if no: ")
        if response.lower() == 'y':
            return data[close_match]
        elif response.lower() == 'n':
            return "The word does not exist in the thesaurus. Please double check it."
        else:
            return "We didn't understand your entry."
    else:
        return "The word does not exist in the thesaurus. Please double check it."


word = input("Enter a word: ")

output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)