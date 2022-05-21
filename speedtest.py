import rplus

def speedtest(path_to_rplus: str):
    path = path_to_rplus
    print('r+ (rplus) speed test:')
    print('Random word generator #1:', rplus.randomwordgen1(5, True))
    print('Random word generator #2:', rplus.randomwordgen2(True))
    print('Random number generator #1:', rplus.randomnumbergen1(path, 1, 3, return_speed=True))
    print('Random number generator #2:', rplus.randomnumbergen2(path, True))
    print('Random password generator:', rplus.randompassword(path, return_speed=True))
