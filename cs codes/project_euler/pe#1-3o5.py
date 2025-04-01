def tof(n: int):
    x = 0
    for i in range(n):
        if i%5 == 0 or i%3 == 0:
            x = x+i
    return x

if __name__ == "__main__":
   print(tof(1000))

