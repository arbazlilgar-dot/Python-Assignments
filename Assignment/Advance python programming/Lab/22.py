# Practical 12: Write a Python program to demonstrate the use of local and global variables in a class.

score = 0 # ye global variable hai

class Game:
    def play(self):
        level = 1 # ye local variable hai, sirf is function me chalega
        print("Global score:", score)
        print("Local level:", level)

g = Game()
g.play()