# ternary-logic

Overview
-
I created 5 gates, ON, OFF, SWITCH, AND and OR.  
I chose to represent the 3 possible states with the  
letters R, B, G where R is the 'off' or 0 state, and  
B and G are on states or 1 and 2 respectively.  

ON gate truth table  
A X  
R R  
B R  
G G  

OFF gate truth table  
A X  
R G  
B R  
G R  

SWITCH gate truth table  
A X  
R R  
B G  
G B  

AND gate truth table  
A B X  
R R R  
R B R  
R G R  
B R R  
B B B  
B G R  
G R R  
G B R  
G G G  

OR gate truth table  
A B X  
R R R  
R B B  
R G G  
B R B  
B B B  
B G G  
G R G  
G B G  
G G G  

These 5 gates should be enough to anything  
binary logic can. At the very least, it is  
possible to approximate binary logic  
using them.  

Usage
-
A ternary object is created using A = ternary()

The 3 gates that only take 1 input can be called  
using dot notation. e.g. A.on() Note that this  
does not change the state of A that would be done  
like so A = A.on()

Alternativey ternary_logic.gates.ON(A) can be used

The OR gate can be called using '^'. e.g. A ^ B  
or ternary_logic.gates.OR(A, B)

The AND gate can be called using '+'. e.g. A + B  
or ternary_logic.gates.AND(A, B)

for a demonstration, see main.py
