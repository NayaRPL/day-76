# algoritma pencarian bagi-dua
def binarysearch(alist,value):
    first=0
    last=len(alist)-1
    found= False
    while first <= last and not found:
        middle = (first + last) // 2
        if alist[middle] == value :
            found = True
        else:
            if value < alist[middle]:
                last = middle -1
            else:
                first = middle +1
    return found
data =[10,40,80,30,60,50]
data.sort()
print(data)
print(binarysearch(data,50))
print(binarysearch(data,11))   