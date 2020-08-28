def sumNumber(nums):
    nums = [int(d) for d in str(nums)]
    print(nums)
    total_even = 0
    total_odd = 0
    for ind,num in enumerate(nums):
        
        if ind % 2 == 0:
            total_even = total_even + num
            print("even",total_even)
        elif ind + 2:
            total_odd -= num
            print("total else", total_odd)
    return total_even + total_odd
       
nums = 325566
print(sumNumber(nums))
#3-2+5-5+6-6=1