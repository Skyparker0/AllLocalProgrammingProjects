# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:49:07 2022

@author: batte
"""

#1 to 10 game

import itertools

def sequence_works(numSequence,goals,printResults = False):
    remainingGoals = goals.copy()
    
    for perm in itertools.permutations(numSequence):
        A,B,C,D = perm
        
        parenthesesPossibilities = """A.B.C.D,(A.B).C.D,A.(B.C).D,A.B.(C.D),(A.B.C).D,A.(B.C.D),(A.B).(C.D),((A.B).C).D,(A.(B.C)).D,A.((B.C).D),A.(B.(C.D))"""\
            .replace("A",A).replace("B",B).replace("C",C).replace("D",D).split(",")  # . is opperation filler
            
        operationPossibilities = []
        for first in "+-*/":
            for second in "+-*/":
                for third in "+-*/":
                    operationPossibilities.append(first+second+third)
                    
        
        
        for parentheses in parenthesesPossibilities:
            for operations in operationPossibilities:
                newEquation = parentheses[:]
                i = 0
                for index in range(len(parentheses)):
                    if parentheses[index] == ".":
                        newEquation = newEquation[:index] + operations[i] + newEquation[index+1:]
                        i += 1
                        
                try:
                    solution = eval(newEquation)
                except ZeroDivisionError:
                    solution = None
                
                if solution in remainingGoals:
                    if printResults:
                        print(newEquation,solution)
                    remainingGoals.remove(solution)
                    if len(remainingGoals) == 0:
                        return True
            
    return False

alreadyBeenTried = []

lstOfWorking = []

for i in range(1,10000):
    iString = "0"*(4-len(str(i))) + str(i)
        
    if "".join(sorted(iString)) in alreadyBeenTried:
        continue
        
    alreadyBeenTried.append(iString)
    if sequence_works(iString,list(range(1,11))):
        print(iString)
        lstOfWorking.append(iString)