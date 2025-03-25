# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 21:19:24 2025

@author: Rochus Spekulatius
"""

# Wurf 1 ------------------------------------------------------
# 3, 4, 5, 6 und x wurden gewürfelt # x ist nicht 2

#Strategie A große Straße 6 behalten: --------------------------------
    # 2 Versuche die 2 zu würfeln zu 1 / 6 je Versuch 
P_A = 1/6 + 1/6 # = 1/3 = 3 / 9

# Strategie B große Straße 6 zurücklegen: -----------------------------
# Wurf 2 ---------------------------------------------------------------------
    # 3, 4 und 5 bleiben 6 und x kommen zurük in den Becher
    # 2 Würfel macht 36 Kombinationen 
    # davon gewinnen 4 direkt im ersten Wurf
    # (2,1) (2,6) (1,2) und (6,2)
p1 = 4/36 

# Wurf 3 ---------------------------------------------------------------------
# p21: ---------------------------------------------------------
    # 2 liegt aus Wurf 2 in 7 (=11-4) von 36 Fällen,
    # 12 (Kombinationen mit 2) - 1 (2er pasch) - 4 (aus Wurf 2) = 7
    # 1 Würfel
    # 1 oder 6 gewinnt in 2 von 6 Fällen
p21 = 7/36 * 2/6
# p22: ---------------------------------------------------------------------
    # 1 oder 6 liegt aus Wurf 2 in 16 (=24-4-4) von 36 Fällen
    # 1 Würfel
    # 2 gewinnt
p22 = 16/36 * 1/6 
# p23:  --------------------------------------------------------
    # wurf 2 hat nix getroffen in 9 (=36-4-7-16) von 36 Fällen
    # nochmal 2 Würfel wie bei Wurf 2
    # 2 u 6 oder 2 u 1 gewint in 4 von 36 Fällen
p23 = 9/36 * 4/36  # test 4 + 7 + 16 + 9 == 36

p2 = p21+p22+p23
P_B  = p1 + p2 # = 10/36  = 5 / 18 = 2.5 / 9


# Strategie C starrer Sturrkopf:
#Wurf 2
# wie strategie B
#Wurf 3
p31 = p21
p32 = 0
p33 = (36 - 7 - 4)/36 * 4/36

P_C = p1 + p31 + p33
print(' die Wahrscheinlichkeit für die "Große Strasse" mit der Strategie A ' +
      'nach dem ersten Wurf die 6 (oder 1) zusammen mit der 3, 4 und 5 ' +
      'zu behalten ist \n P_A = \t '+
      str(round(P_A,3)) + ' \n' )

print(' die Wahrscheinlichkeit für die "Große Strasse" mit der Strategie B ' +
      'nach dem ersten Wurf die 6 (oder 1) zurücklegen ist \n P_B = \t '+
      str(round(P_B,3)) + ' \n' )


print(' die Wahrscheinlichkeit für die "Große Strasse" mit der Strategie C ' +
      ' Strarrer Sturrkopf nach dem ersten Wurf und nach dem 2. Wurf' +
      ' (wenn erneut gewürfelt) die 6 (oder 1) zurücklegen ist \n P_B = \t '+
      str(round(P_C,3)) + '\n' )

print('Überprüfung der Wahrscheinlichkeit von Strategie B: \n')
import numpy as np
n = int(1e5)
import random
winlose = np.zeros(n,dtype=bool)
count = 0
count1 = 0
count2 = 0
count3 = 0
count21 = 0
count31 = 0
count4 = 0
count41 = 0
for i in range(n):
    w1 = random.randint(1,6)
    w2 = random.randint(1,6)
    a = w1 == 2 and w2 in [1,6]
    b = w2 == 2 and w1 in [1,6]
    w3 = random.randint(1,6)
    w4 = random.randint(1,6)
    if a or b:
       count1 +=1
       winlose[i] = 1
    else:
        if w1 == 2 or w2 ==2:
            # w3 = random.randint(1,6)
            count2 +=1
            if w3 in [1,6]:
                winlose[i] = 1
                count21 +=1
                # continue
        elif w1 in [1,6] or w2 in [1,6]:
            # w3 = random.randint(1,6)
            count3 +=1
            if w3 == 2:
                winlose[i] = 1
                count31 +=1
                # continue
        else:
            count4 +=1
            w44 = random.randint(1,6)
            w33 = random.randint(1,6)
            aa = w3 == 2 and w4  in [1,6]
            bb = w4 == 2 and w3  in [1,6]
            if aa or bb:
                winlose[i] = 1
                count41 += 1
    
print('\n In dem Zufallsexperiment wurden von ' + str(n) + ' Versuchen ' 
      + str(winlose.sum()) +
      ' Große Straßen gewürfelt das ist eine Qoute von \n '
      + str(winlose.sum()/n))



