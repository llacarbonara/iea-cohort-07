"""
This is a module
It contains the calculate fx
Thank you
"""
import datetime
import sys

x=datetime.datetime.now()
print(f"Today is {x.strftime('%x')}")
print(f"Time is {x.strftime('%X')}")

def calculate(op_a,op_b,operator):
    from math import log as log
    # return eval(str(x)+z+str(y))
    if operator == '+':
        return op_a + op_b
    if operator == '-':
        return op_a - op_b
    if operator == '*':
        return op_a * op_b
    if operator == '/':
        try:
            return op_a / op_b    
        except ZeroDivisionError:
            print("Can't divide by Zero")
            return None
    elif operator == 'log':
        try:
            log(op_b)(op_a)
            
        except ValueError:
            print('Value Error!')
        except TypeError:
            print('Type Error!')
    else:
        print('Unknown Operator')
        return None
        

print('woooo! MyModule has imported')

if __name__ == "__main__":
    print('Running as a script')
    print(f"My name is {__name__}")
args=sys.argsv[1:]



class Calculator:
    import math

    def __init__(self, init_val):
        self.total = init_val
        return self.total

    def __add__(self, value):
        self.total += value
        self.equation = 
        return self.total
    
    def __sub__(self, value):
        self.total -= value
        return self.total
    
    def __mult__(self, value):
        self.total *= value
        return self.total

    def __div__(self, value):
        self.total /= value
        return self.total
    
    def __pow__(self, value):
        self.total = pow(value)
        return self.total

    def __log__(self, value):
        self.total = log[value](self.total)
        return self.total

    def __ac__(self):
        self.total = None



    
class BankAccount(object):
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance
        #if self.Calculator_balance:
        #    self.recent_deposit = amount
        #else:
        #self.recent_deposit = initial_balance

    '''representation of the object "feedable" to Python
    interpreter'''
    def __repr__(self):
        return self.__class__.__name__ + '(' + repr(self.name) \
               + ', ' + repr(self.balance) + ')'

    '''string representation of object, for humans
    __repr__ is used if __str__ does not exist'''
    def __str__(self):
        print('in the __str__() function')
        return self.name + ' ' + str(self.balance)

    def __add__(self, other):
        return BankAccount(self.name + ' ' + other.name,
                    self.balance + other.balance)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.recent_deposit = amount
            return self.balance
        else:
            print("can't deposit nonpositive amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                self.recent_withdrawl = amount
                return self.balance
            else:
                print("can't withdraw", amount, "or you would be overdrawn!")
        else:
            print("can't withdraw nonpositive amount!")
