'''
There is an array of  integers. There are also  disjoint sets,  and , each containing  integers. You like all the integers in set  and dislike all the integers in set . Your initial happiness is . For each  integer in the array, if , you add  to your happiness. If , you add  to your happiness. Otherwise, your happiness does not change. Output your final happiness at the end.

Note: Since  and  are sets, they have no repeated elements. However, the array might contain duplicate elements.
'''

input()

array = map(int, input().split())

A = set(map(int, input().split()))
B = set(map(int, input().split()))

H = 0
for i in array:
    if i in A:
        H += 1
    elif i in B:
        H -= 1
    else:
        H += 0

print(H)