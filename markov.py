import sys
from random import choice


class SimpleMarkovGenerator(object):

    def read_files(self, the_file1, the_file2):
        """Given a list of files, make chains from them."""

        file_object1 = open(the_file1)
        all_text1 = file_object1.read()
        corpus_text1 = all_text1.replace("\n", " ").split(" ")

        file_object2 = open(the_file2)
        all_text2 = file_object2.read()
        corpus_text2 = all_text2.replace("\n", " ").split(" ")

        corpus_text = corpus_text1 + corpus_text2
        self.corpus_text = corpus_text

        self.make_chains()


    def make_chains(self):
        """Takes input text as string; stores chains."""

    
        chain_dict = {}
        for i in range(len(self.corpus_text)-2):
            key = tuple([self.corpus_text[i], self.corpus_text[i +1]])
            value = self.corpus_text[i+2]
           
            chain_dict.setdefault(key, []).append(value)
        self.chains = chain_dict

    def make_text(self, limit=140):
        """Takes dictionary of markov chains; returns random text."""

        random_key = choice(self.chains.keys())
        random_val = choice(self.chains[random_key])
        first_phrase = [random_key[0], random_key[1], random_val]
        
        
        next_key = (first_phrase[-2], first_phrase[-1])


        while next_key in self.chains:
            next_key_list = list(next_key)
            check_limit_list = first_phrase + next_key_list
            check_limit = " ".join(check_limit_list)

            if len(check_limit) < limit:
                first_phrase.append(choice(self.chains[next_key]))
                next_key = (first_phrase[-2], first_phrase[-1])
            else:
                break
            
        sentence = " ".join(first_phrase)
        return sentence 



if __name__ == "__main__":

    Test_Markov_Generator = SimpleMarkovGenerator()
    Test_Markov_Generator.read_files(sys.argv[1], sys.argv[2])
    sentence = Test_Markov_Generator.make_text()

    print sentence
