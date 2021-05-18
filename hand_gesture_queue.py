import random
import queue
import threading
import time
from enum import Enum, auto

class Gesture(Enum):
    SYM1 = auto()
    SYM2 = auto()
    SYM3 = auto()
    SYM4 = auto()
    SYM5 = auto()
    SYM6 = auto()
    SYM7 = auto()
    #SYM8 = auto()
    #SYM9 = auto()
    #SYM10 = auto()
    #SYM11 = auto()
    #SYM12 = auto()

# Creates password of unique gestures
def generatePassword(length):
    if length > len(Gesture):
        length = len(Gesture)
    password = random.sample(list(Gesture),k=length)
    return(password)

def streamer(q):
    print("Initiaing Queue")
    while True:
        gesture = random.choice(list(Gesture))
        holdTime = random.randint(15,30)
        for i in range(holdTime):
            time.sleep(0.1)
            noise = random.choice(list(Gesture))
            sample = random.choices([gesture,noise],weights=[8,1],k=1)
            q.put(sample[0])
            #print(sample[0])

def checkPassword(q,password):
    i = 0
    foundPassword = False
    while not foundPassword:
        gesture = q.get()
        if gesture == password[i]: 
            i += 1
            #print(i)
        else:
            i = 0
        if i == len(password):
            foundPassword = True
            print("Password Correct")
            print(password)
        
pw = generatePassword(3)
dummy_stream = queue.Queue()
t1 = threading.Thread(target=streamer, args=(dummy_stream,), daemon=True)
t1.start()
checkPassword(dummy_stream,pw)




