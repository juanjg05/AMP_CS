def fib(n):
     
    first = 1
    second = 2
    tot = 0
    fib = [1,2]
    for i in range(n-2):  
        first, second = second, (first+second)
        fib.append(second)
    return fib



if __name__ == "__main__": 
    print(fib(30))