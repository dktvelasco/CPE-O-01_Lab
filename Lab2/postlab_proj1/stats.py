def mean(s):
    if len(s) == 0:
        return 0
    else:
        return sum(s) / len(s)

def median(s):
    if len(s) == 0:
        return 0
    ss = sorted(s)
    if len(s) % 2 == 0:
        return (ss[len(s)//2 - 1] + ss[len(s)//2]) / 2
    else:
        return ss[len(s)//2]

def mode(s):
    count = {}
    maxcount = 0
    maxelem = None
    for n in s:
        count[n] = count.get(n, 0) + 1
        if count[n] > maxcount:
            maxcount = count[n]
            maxelem = n
    return maxelem

def main():
    userList = [3, 1, 7, 1, 4, 10]
    print("List:", userList)
    print("Mode:", mode(userList))
    print("Median:", median(userList))
    print("Mean:", mean(userList))

main()