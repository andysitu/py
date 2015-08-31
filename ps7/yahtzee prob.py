import random

def rollsix():
    prev = random.randrange(1,7)
    for i in range(4):
        value = random.randrange(1,7)
        if value != prev:
            return False
    return True



def yahtzeeIt(times):

    success = 0
    for i in range(times):
        if rollsix():
            success += 1
    print success
    return float(success) / times * 100
        
print yahtzeeIt(1000000)
