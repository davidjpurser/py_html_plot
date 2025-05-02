
class Normaliser:

    def __init__(self, min_val, max_val):
        self.min_val = min_val
        self.max_val = max_val

    def normalise(self, val):   
        if self.min_val <= val <= self.max_val:
            val = (val - self.min_val) / (self.max_val - self.min_val) * 100
        elif val < self.min_val: 
            val = 0
        elif val > self.max_val:
            val = 100

        return val
    
