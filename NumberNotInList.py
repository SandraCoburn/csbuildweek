'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

Write an efficient algorithm for the following assumptions:

N is an integer within the range [1..100,000];
each element of array A is an integer within the range [−1,000,000..1,000,000].

'''
def solution(A):
    l = set(A)
    all_pos = [i for i in A if i > 0]
    length = len(A)

    flag=length+2
    check=0

    #mark all non-required numbers with flag
    for i in range(length):
        if(all_pos[i]>length):
            all_pos[i]=flag
    for i in range(length):
        if all_pos[i] == flag:
            continue
        v=abs(all_pos[i])
        all_pos[v-1]*=-1
        print(all_pos)
    #check for index of first positive number
    for i in range(length):
        if all_pos[i]>0:
            print(i+1)
            check=1
            break
    if check == 0:
        print(length+1)

l = [3, 4, -1, 1,2,5,6,10]
print(solution(l))

def solution2(A):
    return next(i for i, e in enumerate(sorted(A) + [None], 1) if i != e)
print(solution2([3, 4, -1, 1,2,5,6,10]))
    