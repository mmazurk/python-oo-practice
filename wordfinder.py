"""Word Finder: finds random words from a dictionary."""

from random import randint

class WordFinder:
    def __init__(self, path):
        "Reads a file containing words, one per line"
        file = open(path)
        self.list = file.readlines()
        self.list_length = len(self.list)
        file.close()
        print(f"{self.list_length} words read")
    
    def random(self):
        "Returns a random word"   
        return self.list[randint(0,self.list_length-1)].strip()