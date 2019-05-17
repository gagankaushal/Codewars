# return masked string
def maskify(cc):
    finalStr = ''

    if len(cc) < 4:
        return cc

    elif len(cc) >= 4:
        for i in range(0, len(cc) - 4):
            finalStr = finalStr + '#'
        for i in range(len(cc) - 4, len(cc)):
            finalStr = finalStr + cc[i]
        return finalStr

    pass