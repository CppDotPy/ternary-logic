class ternary:

    R = 1
    B = 2
    G = 3
    BASE = 3

    valid_states = [R, B, G]

    def __init__(self, *value):

        if value == (): value = (ternary.R, None)
        if value[0] not in ternary.valid_states: raise TypeError('Invalid value for state')

        self.state = value[0]
        self.carry = 0

    def __repr__(self):
        case = {ternary.R: 'R', ternary.B: 'B', ternary.G: 'G'}
        return case[self.state]

class gates:

    def validate(value):

        valid_state = type(ternary(ternary.R))
        valid = type(value) == valid_state
        if not valid: raise TypeError('Invalid State')

    def AND(A, B):

        gates.validate(A)
        gates.validate(B)

        if A.state == B.state: return A
        else: return ternary(ternary.R)
    
    def OR(A, B):

        gates.validate(A)
        gates.validate(B)

        return ternary(max(A.state, B.state))

    
    def ON(A):

        gates.validate(A)

        if A.state == ternary.G: return ternary(ternary.G)
        else: return ternary(ternary.R)
    
    def OFF(A):

        gates.validate(A)

        if A.state == ternary.R: return ternary(Ternary.G)
        else: return ternary(ternary.R)

    def SWITCH(A):

        # should be done with math
        if A.state == ternary.R: return ternary(ternary.R)
        if A.state == ternary.B: return ternary(ternary.G)
        if A.state == ternary.G: return ternary(ternary.B)

class math:

    def divide_with_remainder(A, B):

        problem = type(A) != int
        problem = type(B) != int
        if problem: raise ValueError('divide_with_remainder only takes int as arguments')

        remainder = A % B
        result = (A - remainder) / B

        return (int(result), remainder)

    def add(A, B):

        gates.validate(A)
        gates.validate(B)

        output = ternary()
        a = A.state
        b = B.state
        x = math.divide_with_remainder(((a - ternary.R) + (b - ternary.R)), ternary.BASE)
        output.state = x[1] + ternary.R
        output.carry = x[0]

        return output

class ternary(ternary):

    def count(self):

        self.state = math.add(self, ternary(ternary.B)).state
        return self

    def __add__(self, other):

        gates.validate(other)
        return gates.AND(self, other)

    def __xor__(self, other):
        
        gates.validate(other)
        return gates.OR(self, other)

    def on(self): return gates.ON(self)
    def off(self): return gates.OFF(self)
    def switch(self): return gates.SWITCH(self)















