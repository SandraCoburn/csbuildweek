def firsNissigPositive(nums):

    seen = [False] *len(nums)
    for num in nums:
        if 0 < num <= len(nums):
            seen[num-1] = True
    for idx in range(len(seen)):
        if seen[idx] == False:
            return idx + 1
    # print(max(nums) + 1)
    return len(nums) + 1

a = [3,4,-1,1]
b = [7,8,9,11,12]
print(firsNissigPositive(a))

def solution2(A):
    sort_A = sorted(A)
    k = 1
    list_of_int = []
    while k <= len(a):
        list_of_int.append(k)
        k += 1
    if list_of_int == sort_A:
        small = max(sort_A) + 1
    elif list_of_int != sort_A:
        j = 1
    for i in sort_A:
        if i <= 0:
            small = 1
        elif j != i:
            small = j
        elif j == i:
            j += 1
        else:
            small = "error"
    return small

print(solution2([7,8,9,11,12]))

def solution3(A):
    # write your code in Python 3.6
    A.sort()
    min = 1
    for a in A:
        if a > min:
            return min
        if a > 0:
            min = a+1
    
    return min

c = [1,2,0]
print(solution3(a))