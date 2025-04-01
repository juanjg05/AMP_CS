def check_palindrome(nums: int):
    let = str(nums)
    letrev = let[::-1]
    bins = str(bin(nums))[2::]
    binsss = bins[::-1]
    if let == letrev and bins == binsss:
        return True
    return False

def loops(lim: int):
    n = 0
    for i in range(lim):
        if check_palindrome(i):
            n += i
    return n

if __name__ == "__main__":
    print(loops(1000000))
    