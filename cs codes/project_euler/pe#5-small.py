def get_small():
    small = 0
    z = 0
    while small == 0:
        z +=20
        if z%11 == 0 and z%12 == 0 and z%13 == 0 and z%14 == 0 and z%15 == 0 and z%16 == 0 and z%17 == 0 and z%18 == 0 and z%19 == 0 and z%20 == 0:
            small = z
    return small

if __name__ == "__main__":
    print(get_small())