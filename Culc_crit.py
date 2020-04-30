# -*- coding: utf-8 -*-

import random as rnd

#To calicurate the possibility of critical hit of the battle of 'Pocket Monster'
def critical_hit(count):
    for i in range(0,100):
        rndnum = rnd.randint(1,16)
        if rndnum == 16:
            print('Critical Hit!!')
            count += 1
    return count
    possibility_crit = []
    for i in range(0,10):
        cnt = critical_hit(0)
        possibility_crit.append(cnt)
        print(possibility_crit)
        avg_crit = sum(possibility_crit)/10
    print(avg_crit)
    print('Avg num of crit hit percentage is ' + str(avg_crit) + ' percent.')

#Culculate the possibility of encoutering 6V monster.
def cul_6v():
    stcnt = 0
    flg = False
    while flg == False:
        status = []
        for i in range(0,6):
            rndint = rnd.randint(0,31)
            status.append(rndint)
        #This code is nonsence...
        if status[0] == 31 and status[1] == 31 and status[2] == 31 and status[3] == 31\
         and status[4] == 31 and status[5] == 31:
            print('This has the best status.')
            flg = True
            stcnt += 1
            print(stcnt)
            for k in range(0,6):
                print(status[k])
        else:
            for i in range(0,6):
                print(status[i])
            stcnt += 1
def print_second_opiton():
    #Through using 'end' keyword, you can connnect strings.
    print('Hello',end = '')
    print('World')
    #Therouh using 'sep' keyword, you can separate strings by comma etc...
    print('Hawk','Tiger','Hopper',sep = ',')

#This is a code for understanding diff bet local and grobal scope.
#def spam():
#    eggs = 99
#    bacon()
#    print(eggs)
#def bacon():
#    ham = 101
#    print(ham)
#    eggs = 0
#spam()

#Local variants can use its local scope, but global is not.
#Naming same names to local and global scope and diff defs is not recommeded.
#Naming a unique name is desireble.
#def spam():
#    eggs = 'spam local'
#    print(eggs)
#def bacon():
#    eggs = 'bacon local'
#    print(eggs)
#    spam()
#    print(eggs)
#    
#eggs = 'global'
#bacon()
#print(eggs)

##If you use 'global' keyword in local scope, you can define the variants as global ones.    
#def spam():
#    global eggs
#    eggs = 'spam'
#    
#eggs = 'grobal'
#spam()
#print(eggs)

#Compare the difference between two spam definition.
def spam(divided_by):
    try:
        return 42 / divided_by
    except ZeroDivisionError:
        print('Error:Invalid Value')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))

def spam(divided_by):
    return 42 / divided_by
#Exception can be catched in exeuting 'try' clause.
try:
    print(spam(2))
    print(spam(12))
    print(spam(0))
    print(spam(1))
except ZeroDivisionError:
    print('Error: Invalid Value')