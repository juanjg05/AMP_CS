import math

def get_two(num: int):
    powers_list = []
    str = bin(num)[2:]

    for i in range(len(str)):
        num = int(str[i])
        if num == 1:
            powers_list.append(2**(len(str)-i-1))
    powers_list.sort()

    return powers_list

if __name__ == "__main__":

    print(get_two(10**25))


