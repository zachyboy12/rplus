"""
Generates the randomist numbers/items possible.
Powered by random.randint, secrets.choice, and time.strftime, which are not third-party modules.
The pros:
- Detects if number was generated earlier
- Has a function which generates the hour + the minute of the time, which is really random
The cons:
- Is really slow
"""
from random import randint as __randint
from time import time as __time, strftime as __strftime
from secrets import choice as __choice


def randomnumbergen1(path_to_rplus: str, low: int, high: int, more_random_but_slow=False, return_speed=False):
    start_time = __time()
    try:
        open(path_to_rplus + '/numcache.txt')
    except:
        open(path_to_rplus + '/numcache.txt', 'w').write('1')
    # Checking if user wants randomer numbers
    if more_random_but_slow is True:
        performance = 4000000  # The con of randomer numbers is that it is very slow
    elif more_random_but_slow is False:
        performance = 1000000
    cache = open(f'{path_to_rplus}/numcache.txt').read()  # Information of earlier calculated numbers
    rnums = []  # The random numbers to choose from
    for i in range(performance):  # Performance depends if more_random_but_slow is True or is False
        rnums.append(__randint(low, high))  # Appending semi-random numbers
    rnum = __choice(rnums)  # The random number
    if str(rnum) == cache:  # Checking if random number is equal to the previous random number
        if high - low == 1:
            pass
        else:
            rnum = __choice(rnums)  # Resetting rnum
    open(f'{path_to_rplus}/numcache.txt', 'w').write(str(rnum))  # Write rnum to numcache.txt
    end_time = __time()
    if return_speed is True:
        return end_time - start_time, rnum
    elif return_speed is False:
        return rnum
    
    
def randomnumbergen2(path_to_rplus: str, return_speed=False):
    start_time = __time()
    rnum = int(__strftime('%S')) + int(__strftime('%I'))
    end_time = __time()
    if return_speed is True:
        return end_time - start_time, rnum
    elif return_speed is False:
        return rnum
    
    
def randompassword(path_to_rplus: str, numberofletters=12, return_speed=False):
    start_time = __time()
    rpl = []
    p = ''
    for i in range(numberofletters + 1):
        lon = __choice(['l', 'n'])
        word = __choice(open('/usr/share/dict/words').read().splitlines())
        if lon == 'l':
            rpl.append(word[0])
        else:
            rpl.append(randomnumbergen1(path_to_rplus, 0, 9))
    for j in rpl:
        p += str(j)
    end_time = __time()
    if return_speed is True:
        return end_time - start_time, p
    elif return_speed is False:
        return p
    
    
def randomwordgen1(numberofletters: int, return_speed=False):
    start_time = __time()
    for word in open('/usr/share/dict/words').read().splitlines():
        if len(word) != numberofletters:
            continue
        else:
            break
    end_time = __time()
    if return_speed is False:
        return word
    elif return_speed is True:
        return end_time - start_time, word


def randomwordgen2(return_speed=False):
    start_time = __time()
    word = __choice(open('/usr/share/dict/words').read().splitlines())
    end_time = __time()
    if return_speed is True:
        return end_time - start_time, word
    elif return_speed is False:
        return word
