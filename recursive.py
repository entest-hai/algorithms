# 22 JUL 2021 
# basic recursive and dynamic programmming 
def factor(n):
    if n == 1:
        return 1 
    else:
        return n * factor(n-1)


def permute(s):
    """
    p('abc') = ['a'] + p('bc') + ['b'] + p('ac') + ... 
    """
    # result 
    result = []
    # base case [['a']]
    if len(s) == 1:
        return [s]
    else:
        for x in s:
            # remain 
            remain = [y for y in s if y!=x]
            z = permute(remain)
            # combine result 
            print(z)
            for t in z:
                result.append([x] + t)
    # return 
    return result


def testFactor(n):
    print("test factor")
    print("factor {0} = {1}".format(n, factor(n)))


def testPermute():
    result = permute(['a','b','c'])
    for x in result:
        print(x)


if __name__ == "__main__":
    testFactor(5)
    testPermute()
    
