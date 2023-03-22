import mean
import median
import mode

class stats:
    def mean():
        lst = []
        n = int(input("Enter number of elements : "))
        
        for i in range(0, n):
            ele = int(input())
            lst.append(ele)
            
    def mean(lst):
        Sum = sum(lst)
        average= Sum/len(lst)
        print (average)

mean()
median()
mode()

pass