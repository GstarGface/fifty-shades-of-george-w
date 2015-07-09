import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, the_file1, the_file2):
        """Given a list of files, make chains from them."""

        # your code here
        file_object1 = open(the_file1)
        all_text1 = file_object1.read()
        corpus_text1 = all_text1.replace("\n", " ").split(" ")

        file_object2 = open(the_file2)
        all_text2 = file_object2.read()
        corpus_text2 = all_text2.replace("\n", " ").split(" ")

        corpus_text = corpus_text1 + corpus_text2
        return corpus_text




    def make_chains(self, corpus_text):
        """Takes input text as string; stores chains."""

    
        chain_dict = {}
        i = 0
        for i in range(len(corpus_text)-2):
            key = tuple([corpus_text[i], corpus_text[i +1]])
            value = corpus_text[i+2]
           
            chain_dict.setdefault(key, []).append(value)
            i += 1

        return chain_dict 

    def make_text(self, chains):
        """Takes dictionary of markov chains; returns random text."""

        # your code here


        random_key = choice(chains.keys())
        random_val = choice(chains[random_key])
        first_phrase = [random_key[0], random_key[1],  random_val]
        #print first_phrase
        
        
        next_key = (first_phrase[-2], first_phrase[-1])
        #print next_key

        while next_key in chains:
            first_phrase.append(choice(chains[next_key]))
            # print first_phrase
            next_key = (first_phrase[-2], first_phrase[-1])
            
        sentence = " ".join(first_phrase)
        print sentence 



# if __name__ == "__main__":

#     # we should get list of filenames from sys.argv
#     # we should make an instance of the class
#     # we should call the read_files method with the list of filenames
#     # we should call the make_text method 5x


#     pass


Test_Markov_Generator = SimpleMarkovGenerator()

files_read = Test_Markov_Generator.read_files(sys.argv[1], sys.argv[2]) 
chains_made = Test_Markov_Generator.make_chains(files_read)
text_made = Test_Markov_Generator.make_text(chains_made)