# Yathzee_BigStraight
Three Strategies to a Big Straigth after the first role with 3, 4, 5, 6, x (any except 2) 
Probabilities are calculated
Strategy B ist tested with a Monte-Carlo-Expriment

# Wurf 1 ------------------------------------------------------
# 3, 4, 5, 6 und x wurden gewürfelt # x ist nicht 2 und nicht 1

#Strategie A große Straße 6 behalten: --------------------------------
    # 2 Versuche die 2 zu würfeln zu 1 / 6 je Versuch 
P_A = 1/6 + 5/6*1/6 # = 11/36 = 30.6 %


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
P_B  = p1 + p2 # = 10/36  = 5 / 18 = 2.5 / 9 = 27.8 %


# Strategie C starrer Sturrkopf:
#Wurf 2
# wie strategie B
#Wurf 3
p31 = p21
p32 = 0
p33 = (36 - 7 - 4)/36 * 4/36 # = 25.3 %

P_C = p1 + p31 + p33
