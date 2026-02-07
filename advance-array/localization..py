def localization():
    n = int(input())
    while n > 0:
        s = str(input())
        if len(s) <= 10:
            print(s)
        else:
            first = s[0]
            last = s[-1]
            print(first + str(len(s) - 2) + last)
        n -= 1
localization()