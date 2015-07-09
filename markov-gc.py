import sys
import random


def make_chains(the_file):
    """Takes input text as string; returns dictionary of markov chains."""
    file_object = open(the_file)
    all_text = file_object.read()
    corpus_text = all_text.replace("\n", " ").split(" ")
    
    chain_dict = {}
    i = 0
    for i in range(len(corpus_text)-2):
        key = tuple([corpus_text[i], corpus_text[i +1]])
        value = corpus_text[i + 2]
       
        chain_dict.setdefault(key, []).append(value)
        i += 1

    return chain_dict 

# make_chains(sys.argv[1])


def make_text(chains):
    """Takes dictionary of markov chains; returns random text."""


    random_key = random.choice(chains.keys())
    random_val = random.choice(chains[random_key])
    first_phrase = [random_key[0], random_key[1],  random_val]
    #print first_phrase
    
    
    next_key = (first_phrase[-2], first_phrase[-1])
    #print next_key

    while next_key in chains:
        first_phrase.append(random.choice(chains[next_key]))
        # print first_phrase
        next_key = (first_phrase[-2], first_phrase[-1])
        
    sentence = " ".join(first_phrase)
    print sentence 







make_text(make_chains(sys.argv[1]))



# Change this to read input_text from a file, deciding which file should
# be used by examining the `sys.argv` arguments (if neccessary, see the
# Python docs for sys.argv)

# input_text = "sys.argv"

# Get a Markov chain
# chain_dict = make_chains(input_text)

# Produce random text
# random_text = make_text(chain_dict)

# print random_text
