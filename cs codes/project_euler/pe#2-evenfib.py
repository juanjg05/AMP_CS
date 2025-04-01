def evenf (n:int):
    
    first = 1
    second = 2
    tot = 0
    
    while second <= n:  
        if second%2 == 0:
            tot = tot + second
        first, second = second, (first+second)
    return tot

if __name__ == "__main__":
    print(evenf(4000000))

