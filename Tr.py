#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 25 14:28:23 2018

@author: ZanZver
"""
import time

def ChristmasTreeBub(n):
    z=n-1
    x=1
    Space = ' '
    y = [Space]
    con = True
    BubleCount = 1
    for i in range(0,n):
        for i in range(0,z):
            print(' ',end='')
            if con == True:
                y.append(Space)
        for i in range(0,x):
            if BubleCount % 2 ==0:
                print('0',end='')
            else:
                print('1',end='')
            BubleCount = BubleCount + 1
                
        for i in range(0,z):
            print(' ',end='')
         
        time.sleep(0.3)    
        x=x+2
        z=z-1
        print()
        con = False
    z=n-1
    x=1
    y.pop()

    B = y[0:len(y)//2]
    C = y[len(B)//2:]
    print(*B ,'101')
    time.sleep(0.3)
    
    for i in range(0, 2):
        print(*B ,'010')
        time.sleep(0.3)

def main():
    ChristmasTreeBub(20)
    

if __name__ == '__main__': main()
