import numpy as np

class binary():

    def __init__(self):
        self.index = 0
        self.array = [0] * 256
        
    def __str__(self):
        return f"{np.flip(self.array)}"

    def increment(self):
        if self.array[0] == 0:
            self.array[0] = 1
            return
        

binary = binary()
binary.increment()
binary.increment()
binary.increment()
binary.increment()
print(binary)