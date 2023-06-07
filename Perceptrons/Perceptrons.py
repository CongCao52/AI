

############################################################
# Imports
############################################################

import Perceptrons_data as data

# Include your imports here, if any are used.

############################################################
# Section 1: Perceptrons
############################################################

class BinaryPerceptron(object):

    def __init__(self, examples, iterations):
        self.w = {}
        for i in range (iterations): 
            for x, y in examples:
                dot_result = 0
                for f in x:
                    if f not in self.w:
                        self.w[f]=0
                    dot_result = dot_result + x[f] * self.w[f]
                if dot_result>=0:
                    y_predict = True
                else:
                    y_predict = False
                
                if y_predict != y:
                    if y:
                        for ff in x:
                            self.w[ff] += x[ff]
                    else:
                        for ff in x:
                            self.w[ff] -= x[ff]
    def predict(self, x):
        dot_result = 0
        for f in x:
            if f not in self.w:
                self.w[f] = 0
            dot_result =dot_result + x[f]*self.w[f]
        if dot_result >=0:
            return True 
        else:
            return False

class MulticlassPerceptron(object):

    def __init__(self, examples, iterations):
        self.w = {}
        for i in range(iterations):
            for x,y in examples:
                if y not in self.w:
                    self.w[y] = {}
                max_prod = -999
                y_hat = 0
                for z in self.w:
                    dot = 0
                    for feature in x:
                        if feature not in self.w[z]:
                            self.w[z][feature] = 0
                        dot += x[feature]*self.w[z][feature]
                    if dot > max_prod:
                        y_hat =z
                        max_prod = dot
                if y_hat !=y:
                    for feat in x:
                        self.w[y][feat] += x[feat]
                        self.w[y_hat][feat] -= x[feat]
    def predict(self, x):
        max_prod = -999
        y_hat = 0
        for y in self.w:
            dot = 0
            for feature in x:
                if feature not in self.w[y]:
                    self.w[y][feature] = 0
                dot += x[feature] * self.w[y][feature]
            if dot >max_prod:
                max_prod = dot
                y_hat = y
        return y_hat

############################################################
# Section 2: Applications
############################################################

class IrisClassifier(object):

    def __init__(self, data):
        iterations = 30
        example = []
        for x, y in data:
            dictionary ={}
            for i in range(len(x)):
                featureName = 'feature_'+str(i+1)
                dictionary[featureName] =x[i]
            example.append((dictionary,y))
        self.perceptron =  MulticlassPerceptron(example,iterations)
    

    def classify(self, instance):
        x = {}
        for i in range(len(instance)):
            featureName = 'feature_' +str(i+1)
            x[featureName] = instance[i]
        return self.percpetron.predict(x)

class DigitClassifier(object):

    def __init__(self, data):
        iterations = 15
        example = []
        for x,y in data:
            dictionary = {}
            for i in range(len(x)):
                featureName = 'feature_'+ str(i+1)
                dictionary[featureName] = x[i]
            example.append((dictionary,y))
        self.perceptron =  MulticlassPerceptron(example,iterations)        
        
    def classify(self, instance):
        w = {}
        for i in range(len(instance)):
            featureName = 'feature_'+ str(i+1)
            w[featureName] = instance[i]
        return self.perceptron.predict(w)

class BiasClassifier(object):

    def __init__(self, data):
        iterations = 10
        example = []
        for x,y in data:
            dictionary = {}
            dictionary['feature'] = x - 1
            example.append((dictionary,y))
        self.perceptron =  BinaryPerceptron(example,iterations)    

    def classify(self, instance):
        w = {}
        w['feature'] = instance-1
        return self.preceptron.predict(w)

class MysteryClassifier1(object):

    def __init__(self, data):
        iterations = 5
        example = []
        for x,y in data:
            dictionary = {}            
            dictionary['feature_1']  = pow(x[0],2) + pow(x[1],2) - 4
            example.append((dictionary,y))            
        self.perceptron =  BinaryPerceptron(example,iterations)

    def classify(self, instance):
        x = {}
        x['feature_1']  = pow(instance[1],2) + pow(instance[0],2) - 4
        return self.perceptron.predict(x)

class MysteryClassifier2(object):

    def __init__(self, data):
        iterations = 5
        example = []
        for x,y in data:
            dictionary = {}            
            dictionary['feature_1']  = x[0]*x[1]*x[2]
            example.append((dictionary,y))            
        self.perceptron =  BinaryPerceptron(example,iterations)


    def classify(self, instance):
        x = {}
        x['feature_1']  = instance[0] +instance[1] + instance[2]
        return self.perceptron.predict(x)

