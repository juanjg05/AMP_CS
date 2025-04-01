def check_palindromez():
    listt = []
    for i in range(999,99,-1):
        for z in range(999,99,-1):
            nums = i*z
            let = str(nums)
            letrev = let[::-1]
            if let == letrev:
                listt.append(nums)
    listt.sort()
    return listt[-1]
if __name__ == "__main__":
    print(check_palindrome())
    
#this is very non-optimal
#spent most of my brain-power doing 98