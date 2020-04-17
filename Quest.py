# -*- coding: utf-8 -*-
import pandas as pd
import random as rd

class Person:
    #変数と関数に同じ名前を割り当てていたためエラーになった。
    def __init__(self,name,hp,mp,atk,df,satk,sdf):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.df = df
        self.satk = satk
        self.sdf = sdf

    def Atk(self,enm):
        #print("Hello!")
        if self.atk > enm.df:    
            enm.hp = enm.hp - (self.atk - enm.df)
            print('{} は {} に {} のだめーじをあたえた！'.format(self.name,enm.name,self.atk - enm.df))
            enm.Atk(hero)
            
    def status(self):
        print(pd.DataFrame([self.hp,self.mp,self.atk,self.df,self.satk,self.sdf],
                             index = ['HP','MP','攻撃力','防御力','特殊攻撃力','特殊防御力'],columns = [self.name]))
#This class is an example of "Inheritance".
class SuperPerson(Person):
    #This method is one of the example of "Overriding".
    def Atk(self,enm):
        rnds = rd.randrange(10,20)
        print('{} は　{} に {} のだめーじをあたえた！'.format(self.name,enm.name,rnds))
        enm.hp = enm.hp -rnds
        if enm.hp <= 0:
            print('{} はたおれた！'.format(enm.name))
        else:
            enm.Atk(self)
    
    def Supernova(self,enm):
        rnd = rd.randrange(30)
        print('{} は　{} に {} のだめーじをあたえた！'.format(self.name,enm.name,rnd))
        enm.hp = enm.hp -rnd
        if enm.hp <= 0:
            print('{} はたおれた！'.format(enm.name))
        else:
            enm.Atk(self)
class Enemy:
    def __init__(self,name,hp,mp,atk,df,satk,sdf):
        self.name = name
        self.hp = hp
        self.mp = mp
        self.atk = atk
        self.df = df
        self.satk = satk
        self.sdf = sdf
        
    def Atk(self,person):
        if self.atk > person.df:
            person.hp = person.hp - (self.atk - person.df)
            print('{} は {} に {} のだめーじをあたえた！'.format(self.name,person.name,self.atk - person.df))
        else:
            print('{} のこうげきは {} にきかなかった'.format(self.name,person.name))
    def status(self):
        print(pd.DataFrame([self.hp,self.mp,self.atk,self.df,self.satk,self.sdf],
                           index = ['HP','MP','攻撃力','防御力','特殊攻撃力','特殊防御力'],columns = [self.name]))
#This class is example for 'Composition'.
class Sword:
    #This row is an example of 'class variants'.
    swords = []
    
    def __init__(self,name,atk,owner):
        self.name = name
        self.atk = atk
        self.owner = owner
        self.swords.append((self.name,self.atk,self.owner.name))
        print('New sword was created.')
    def status(self):
        print(pd.DataFrame([self.atk,self.owner.name],index = ['攻撃力','オーナー'],columns = [self.name]))
    'Object has a repr method on default status and that can be overrided through write the method.'
    def __repr__(self):
        return self.name
#hero = Person('勇者',20,10,10,20,10,10)
oak = Enemy('オーク',15,5,25,5,5,5)
#hero.Atk(slime1)
#print(hero.hp)
#print(slime1.hp)
#hero.status()
#slime1.status()
sp = SuperPerson('スーパー勇者',30,25,30,30,25,55)
sp.status()
sw1 = Sword('焔の剣',10,sp)
sw2 = Sword('光の剣',20,sp)
sw3 = Sword('闇夜の剣',40,sp)
print(Sword.swords)
sw1.status()
sw2.status()
sw3.status()
#sp.Supernova(oak)
sp.Atk(oak)
print(sw1,sw2,sw3)
print(sw1 is sw2)
print(not sw1 is sw2 and not sw2 is sw3)
