# -*- coding: utf-8 -*-

class Person:
    #変数と関数に同じ名前を割り当てていたためエラーになった。
    def __init__(self,hp,mp,atk,df,satk,sdf):
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.df = df
#        self.satk = satk
#        self.sdf = sdf

    def Atk(self,enm):
        print("Hello!")
        if self.atk > enm.df:    
            enm.hp = enm.hp - (self.atk - enm.df)
            print('ゆうしゃはてきに {} のだめーじをあたえた！'.format(self.atk - enm.df))
            enm.Atk(hero)
class Enemy:
    def __init__(self,hp,mp,atk,df,satk,sdf):
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.df = df
        self.satk = satk
        self.sdf = sdf
        
    def Atk(self,person):
        if self.atk > person.df:
            person.hp = person.hp - (self.atk - person.df)
            print('すらいむはゆうしゃに {} のだめーじをあたえた！'.format(self.atk - person.df))
        else:
            print('すらいむのこうげきはゆうしゃにきかなかった')

hero = Person(20,10,10,10,10,10)
slime1 = Enemy(10,5,20,5,5,5)
#print(hero1.hp)

person = Person(20,10,10,10,10,10)
person.Atk(slime1)
print(hero.hp)
print(slime1.hp)


#Bellow is a code for test.
#class Test:
#    def __init__(self,testval):
#        self.tstval = testval
#        
#    def say_hello(self,elm):
#        print('Hello!!' + str(elm))
#
#test = Test(11)
#test.say_hello(22)