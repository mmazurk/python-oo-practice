"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "Creates a serial generator object with a start value"
        self.start = start
        self.new = start - 1
    
    def generate(self):
        "Incremenets the number by one"
        self.new += 1
        return self.new
    
    def reset(self):
        self.new = self.start - 1
    

    

    


