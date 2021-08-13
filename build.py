import re

# Source text file to build wordlist from
text_to_build = "text.txt"
# Wordlist will be outputted to the following file within the same directory as build.py
output_file = "wordlist.txt"
# Keep track of how many times we have seen a word. We only care about one occurence of a word.
words = {}

with open(text_to_build) as t, open(output_file, 'w') as o:
    # Remove all special characters and new lines, leaving spaces to split on space.
    new_text = re.sub('[&\/\\#,+()$~%.\'":*?<>{}-]\n', '', t.read())
    # Grab individual words
    word_list = new_text.split(' ')

    # Build hash table of individual words
    for word in word_list:
        if word.lower() not in words:
            words[word.lower()] = 1

    # Write our output to new wordlist.txt file
    for word in words.items():
        o.write(word[0] + '\n')