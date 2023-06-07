############################################################
# Section 1: Python Concepts
############################################################

python_concepts_question_1 = """
Strong typed: the variable have a type and that type only matters when doing operation on that variable.
example:'foo' + 3 can cause a TypeError: cannot concatenate 'str' and 'int' objects


Dynamic typed: the type of variable is determined only during the runtime. 
example when write x = 'sss', type of x is a string, when write x = 1, type of x is a int
"""

python_concepts_question_2 = "list need to be the value and names need to be the key since list is a unhashable type. "

python_concepts_question_3 = "The second approch is faster due to the less time of complexity and effective memory allocation."

############################################################
# Section 2: Working with Lists
############################################################

def extract_and_apply(l, p, f):
    return [f(x) for x in l if p(x)]

def concatenate(seqs):
    result = []
    for s in seqs: 
        for e in s:
            result.append(e)
    return result

def transpose(matrix):
    result = []
    for j in range(len(matrix[0])):
        s = []
        for i in range(len(matrix)):
            s.append(matrix[i][j])
        result.append(s)
    return result
############################################################
# Section 3: Sequence Slicing
############################################################

def copy(seq):
    if type(seq) ==type(()):
        #tuple
        new_seq = seq +tuple()
    elif type(seq) ==type([]):
        #list
        new_seq =[]
        for e in seq:
            new_seq.append(e)
    else:#string
        new_seq=''
        for e in seq: 
            new_seq +=e
    return new_seq

def all_but_last(seq):
    if type(seq) ==type(()):
        #tuple
        new_seq = seq[:-1] +tuple()
    elif type(seq) ==type([]):
        #list
        new_seq =[]
        for e in seq[:-1]:
            new_seq.append(e)
    else:#string
        new_seq=''
        for e in seq[:-1]: 
            new_seq +=e
    return new_seq

def every_other(seq):
    if type(seq)==type(()): #tuple
        new_seq = tuple(every_other(list(seq)))
    elif type(seq) == type([]): #list
        new_seq = []
        for i in range(len(seq)): 
            if i%2==0:
                new_seq.append(seq[i])       
    else:  
        new_seq = ''
        for i in range(len(seq)):
            if i%2==0:
                new_seq += seq[i]
    return new_seq
        

############################################################
# Section 4: Combinatorial Algorithms
############################################################

def prefixes(seq):
    for i in range(len(seq)+1):
        yield seq[:i]


def suffixes(seq):
    for i in range(len(seq)+1):
        yield seq[i:]


def slices(seq):
    l = len(seq)
    a = 0
    b = 1
    while a < l and b <= l:
        yield seq[a:b]
        if b !=l:
            b +=1
        else:
            a += 1
            b = a+1


############################################################
# Section 5: Text Processing
############################################################

def normalize(text):
    l = text.lower().strip()
    words = l.split(' ')
    result = [w for w in words if len(w)>0]
    return ' '.join(result)
    

def no_vowels(text):
    result = ''
    for t in text:
        if t not in 'AEIOUaeiou':
            result+=t
    return result

def digits_to_words(text):
    num = {'1':'one',
      '2':'two',
      '3':'three',
      '4':'four',
      '5':'five',
      '6':'six',
      '7':'seven',
      '8':'eight',
      '9':'nine',
      '0':'zero'}
    result = ''
    for t in text:
        if t in '1234567890':
            result += num[t]+' '
    r = result.strip()
    return r

def to_mixed_case(name):
    result = ''
    n = name.strip('_').lower()
    for i in n: 
        if len(result)==0 or result[-1] != '_':
            result += i
        elif i =='_' and result[-1] != '_':
            result +=i
        else:
            result +=i.upper()
    result = result.replace('_','')
    return result
        

############################################################
# Section 6: Polynomials
############################################################

class Polynomial(object):

    def __init__(self, polynomial):
        self.coefficients = []
        self.degrees = []
        
        l = len(polynomial)
        for i in range(l):
            self.coefficients.append(polynomial[i][0])
            self.degrees.append(polynomial[i][1])

    def get_polynomial(self):
        polynomial = []
        for i in range(len(self.coefficients)):
            polynomial.append((self.coefficients[i],self.degrees[i]))
        return tuple(polynomial)

    def __neg__(self):
        polynomial = []
        for i in range(len(self.coefficients)):
            polynomial.append((-self.coefficients[i],self.degrees[i]))
        return Polynomial(polynomial)
            

    def __add__(self, other):
        polynomial = []
        polynomial = list(self.get_polynomial())+ list(other.get_polynomial())
        return Polynomial(polynomial)

    def __sub__(self, other):
        polynomial = []
        polynomial = list(self.get_polynomial())
        for i in range(len(other.coefficients)):
            polynomial.append((-other.coefficients[i], other.degrees[i]))
        return Polynomial(polynomial)
        
        

    def __mul__(self, other):
        polynomial = []
        for i in range(len(self.coefficients)):
            for j in range(len(other.coefficients)):
                polynomial.append((self.coefficients[i]*other.coefficients[j],self.degrees[i]+other.degrees[j]))
        return Polynomial(polynomial)
    

    def __call__(self, x):
        length = len(self.coefficients)
        results = [self.coefficients[i]*x**(self.degrees[i]) for i in range(length)]
        return sum(results)

    def simplify(self):
        d = {}
        for l in range (len(self.degrees)):
            if self.degrees[l] not in d.keys():
                d[self.degrees[l]] = self.coefficients[l]
            else:
                d[self.degrees[l]] += self.coefficients[l]
        for j in list(d.keys()):
            if d[j] ==0:
                del d[j]
        
        self.degrees = sorted(list(d.keys()),reverse = True)
        self.coefficients = [d[i] for i in self.degrees]
        if self.degrees ==[] or self.coefficients ==[]:
            self.degrees = [0]
            self.coefficients=[0]
        
                
                

    def __str__(self):
        result = ''
        for i in range(len(self.coefficients)):
            if result=='':
                if self.coefficients[i]==-1:
                    result+='-'
                elif self.coefficients[i]!=-1 and self.coefficients[i] !=1:
                    result += str(self.coefficients[i])
                
                if self.degrees[i] !=0 and self.degrees[i]!=1:
                    result +='x^'+str(self.degrees[i])
                elif self.degrees[i]==1:
                    result +='x'
                elif (self.coefficients[i]==1 or self.coefficients[i]==-1) and self.degrees[i]==0:
                    result +='1'
                    
                
            else: 
                if self.coefficients[i] <0:
                    result+=' - '
                elif self.coefficients[i] >=0:
                    result+=' + '
                
                if self.coefficients[i] !=-1 and self.coefficients[i] !=1:
                    result += str(abs(self.coefficients[i]))
                elif (self.coefficients[i] ==1 or self.coefficients[i]==-1) and self.degrees[i]==0:
                    result+='1'
                    
                if self.degrees[i] !=0 and self.degrees[i]!=1:
                    result +='x^'+str(self.degrees[i])
                elif self.degrees[i]==1:
                    result +='x'
        return result

############################################################
# Section 7: Python Packages
############################################################
import numpy
def sort_array(list_of_matrices):
    l = []
    for m in list_of_matrices:
        l += [numpy.sort(m,axis = None)]
    result = numpy.sort(numpy.concatenate(l))[::-1]
    return result

# matrix1 = numpy.array([[1,2],[3,4]])
# matrix2 = numpy.array([[5,6,7],[7,8,9],[0,-1,-2]])
# sort_array([matrix1, matrix2])

import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

def POS_tag(sentence):
    s = sentence.lower()
    ts = nltk.word_tokenize(s)
    result = [t for t in ts if t not in nltk.corpus.stopwords.words('english') and t.isalnum()]
    r = nltk.pos_tag(result)
    return r



