'''
Merge sort is an example of recursive programming.
It's a way of sort of the list.
Repeatedly decompose the list into two smaller lists.
When you can't divide the list anymore, aggregate to one sorted list.
'''

import random

def perfomrMergeSort(lstElementToSort):
    if len(lstElementToSort) == 1: #escape when the list not for recursion
        return lstElementToSort

    #decompose of the given list
    lstSubElementToSort1 = [] 
    lstSubElementToSort2 = []
    for itr in range(len(lstElementToSort)):
        if len(lstElementToSort)/2 > itr:
            lstSubElementToSort1.append(lstElementToSort[itr])
        else:
            lstSubElementToSort2.append(lstElementToSort[itr])

    #recursion - repeatedly decompose the list until it can't be divded anymore
    lstSubElementToSort1 = perfomrMergeSort(lstSubElementToSort1)
    lstSubElementToSort2 = perfomrMergeSort(lstSubElementToSort2)

    #aggregate
    idxCount1 = 0
    idxCount2 = 0
    for itr in range(len(lstElementToSort)):
        if idxCount1 == len(lstSubElementToSort1):
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        elif idxCount2 == len(lstSubElementToSort2):
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
        elif lstSubElementToSort1[idxCount1] > lstSubElementToSort2[idxCount2]:
            lstElementToSort[itr] = lstSubElementToSort2[idxCount2]
            idxCount2 = idxCount2 + 1
        else:
            lstElementToSort[itr] = lstSubElementToSort1[idxCount1]
            idxCount1 = idxCount1 + 1
    
    return lstElementToSort

#Test
lstRandom = []
for itr in range(0, 10):
    lstRandom.append(random.randrange(0, 100))
print(lstRandom)

lstRandom = perfomrMergeSort(lstRandom)
print(lstRandom)