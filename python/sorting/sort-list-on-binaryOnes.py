# Complete the function below.
import operator

def  swap_array( a):
    a.sort(reverse=True)
    # Get the decimal number:
    dic = {}
    for el in a:
        dic[el] = GetOnesCount(el)
    sorted_value = sorted(dic.items(), key = operator.itemgetter(1), reverse=True)
    sorted_key = sorted(dic.items(), key = operator.itemgetter(0), reverse=True)
    #print(sorted_x)
    mList = []
    while i < len(sorted_x):
        lista = []
        keyValue = sorted_x[i]
        key, value = keyValue
        lista.append(key)

        if i+1 < len(sorted_x):
            nKeyValue = sorted_x[i+1]
            nKey, nValue = nKeyValue
            while value == nValue and i + 1 < len(sorted_x):
                lista.append(nKey)
                nKeyValue = sorted_x[i]
                nKey, nValue = nKeyValue
                i = i + 1
            
        lista.sort(reverse=True)
        
        mList.extend(lista)
        
    for el in mList:
        print(el)
        
        

def GetOnesCount(el):
    decimal = bin(el)
    decimal = decimal[2:]
    decimalList = [int(i) for i in decimal]
    return sum(decimalList)


a = [2, 3, 4, 6]

swap_array(a)

