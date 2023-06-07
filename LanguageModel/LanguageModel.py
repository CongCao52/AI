
############################################################
# Imports
############################################################

# Include your imports here, if any are used.

import string
import random
import math
import re

############################################################
# Section 1: Markov Models
############################################################

def tokenize(text):
    words = re.findall(r"[\w]+|[^\s\w]",text)
    return words


def ngrams(n, tokens):
    ngrams = []
    length = len(tokens)
    if n ==1:
        for i in range(length):
            ngrams.append(((),tokens[i]))
        ngrams.append(((),'<END>'))
    else: 
        for i in range(length):
            if i<n-1:
                first_lst = []
                for j in range(n-1,0,-1):
                    if i-j<0:
                        first_lst.append('<START>')
                    else:
                        first_lst.append(tokens[i-j])
                t = (tuple(first_lst),tokens[i])
            else:
                t = ((tuple(tokens[i+1-n:i])),tokens[i])
            ngrams.append(t)
        t = ((tuple(tokens[length+1-n:length])),'<END>')
        ngrams.append(t)
    return ngrams

class NgramModel(object):

    def __init__(self, n):
        self.n = n 
        self.ngram = []
        self.tokens_set = set()
        self.tokens_sorted = []
        self.dict = {}
    def update(self, sentence):
        new_ngrams = ngrams(self.n,tokenize(sentence))
        self.ngram += new_ngrams
        
        #new_set = set([ele[1] for ele in new_ngrams])
        self.tokens_set.update(set([ele[1] for ele in new_ngrams]))
        self.tokens_sorted = sorted(list(self.tokens_set))
        
    def prob(self, context, token):
        up =0 
        down = 0
        for ele in self.ngram:
            if ele[0] == context:
                down = down +1
                if ele[1] ==token:
                    up = up + 1
        return up/down

    def random_token(self, context):
        r = random.random()
        toke_lst = [self.ngram[i][1] for i in range(len(self.ngram)) if self.ngram[i][0] == context]
        toke_lst.sort()
        length =len(toke_lst)
        if length ==0:
            return ''
        else:
            d = int(length*r)
            if d>length-1:
                d = length-1
            return toke_lst[d]
        
        
    def random_text(self, token_count):
        
        start = tuple(['<START>'] * (self.n - 1))
        current = start
        
        tokens_gen = []
        for i in range(token_count):
            t = self.random_token(current)
            tokens_gen.append(t)
            if self.n > 1:
                current= current[1:] + tuple(t)
            if t == "<END>":
                current = start                
        sen = ' '.join(tokens_gen) 
        self.update(sen)
        return sen   
        

    def perplexity(self, sentence):
        log_p = 0
        sen = ngrams(self.n,tokenize(sentence))
        length = len(sen)
        for i in range(length):
            p = self.prob(sen[i][0], sen[i][1])
            log_p = log_p + math.log(1/p)
        total_p = math.exp(log_p)
        result = pow(total_p, 1/length)
        return result
            
def create_ngram_model(n, path):
    f = NgramModel(n)
    file = open(path)
    l = file.readlines()
    # if len(l) ==0:
    #     return f
    for s in l :
        f.update(s)
    file.close()
    return f 


#m = create_ngram_model(1,'frankenstein.txt'); m.random_text(15)



