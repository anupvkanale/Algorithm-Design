def countInv(inp,inv):
    if (len(inp))==1:
        return (inp,inv)
    else:
        mid = round(len(inp)*0.5)
        left = inp[:mid]
        right = inp[mid:]

        (left,inv) = countInv(left,inv)
        (right,inv) = countInv(right,inv)

        i=0; j=0; k=0;
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                inp[k] = left[i]
                i+=1
            else:
                inp[k] = right[j]
                j+=1
                inv+=len(left)-i
            k+=1

        while i<len(left):
            inp[k] = left[i]
            i+=1; k+=1
        while j<len(right):
            inp[k] = right[j]
            j+=1; k+=1
        

        return (inp,inv)

#inp = [1,3,5,2,4,6]
f = open('IntegerArray.txt', 'r')
inp = [0]*100000
inpdup = [0]*100000
for i in range(100000):
    inp[i] = int(f.readline())
    inpdup[i] = inp[i]
    
(inp, inv) = countInv(inp,0)
print(inv)
