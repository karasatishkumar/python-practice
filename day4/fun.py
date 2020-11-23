def square(num):
    res = num * num
    print("LOCAL VARS ", locals())
    return res


ans = square(5)
print(ans)
print("GLOBAL VARS ", globals())