"""
Author: Tenny Akihary
Class: *** ***
Project: ***** *
Purpose: Implement Radix Sort using Queue. Implementation for postfix notation input/output.
"""
import math


##########i.

#Implementation of queue
class Queue:
    def __init__(self):
        self._element = []

    def is_empty(self):
        return self._element == []

    def size(self):
        return len(self._element)

    def enqueue(self, item):
        self._element.insert(0,item)

    def dequeue(self):
        return self._element.pop()

#Method to find max digits
def findpower(n):
    count = 0
    for i in range(0, len(n)):
        temp = 0
        num = 1
        while n[i]/num >= 1:
            temp += 1
            num *= 10
        if temp > count:
            count = temp
    return count


#Method to Radix Sort the array
def RadixSort(n, exp):
    i = 0
    den = 1
    _length = len(n)
    output = [0]*_length
    while exp >= 1:
        num = 0
        index = 0
        while num < 10:
            while i < _length:
                digit = math.floor((n[i]/den)%10)
                if digit == num:
                    output[index] = n[i]
                    index += 1
                i += 1
            i = 0
            num += 1
        while i < _length:
            n[i] = output[i]
            i += 1
        i = 0
        den *= 10
        exp -= 1
    return output

array = [35, 53, 55, 33, 52, 32, 25]
print(RadixSort(array, findpower(array)))



##########ii.

# Implementation of stack
class Stack:
    def __init__(self):
        self._element = []

    def is_empty(self):
        return self._element == []

    def push(self, item):
        self._element.append(item)

    def pop(self):
        return self._element.pop()

    def top(self):
        return self._element[len(self._element)-1]

    def size(self):
        return len(self._element)

# Asking user to input the postfix notation expression
expression = input("Enter expression(postfix notation)")

# Method of finding the outcome of the postfix notation
def solvePFN(pfn):
    num = Stack()
    numerals = ["0","1","2","3","4","5","6","7","8","9"]
    operators = ['+','-','*','/']
    for n in range(0, len(pfn)):
        if pfn[n] in numerals:
            num.push(int(pfn[n]))
        elif pfn[n] in operators:
            if pfn[n] == operators[0]:
                exp2 = num.pop()
                exp1 = num.pop()
                num.push(exp1+exp2)
            elif pfn[n] == operators[1]:
                exp2 = num.pop()
                exp1 = num.pop()
                num.push(exp1-exp2)
            elif pfn[n] == operators[2]:
                exp2 = num.pop()
                exp1 = num.pop()
                num.push(exp1*exp2)
            elif pfn[n] == operators[3]:
                exp2 = num.pop()
                exp1 = num.pop()
                num.push(exp1/exp2)
        else:
            raise "Incorrect syntax for Postfix Notation"
    return num.pop()

print(solvePFN(expression))
