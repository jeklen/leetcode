# 单行注释
'''
多行注释
def join_biggest_int(n, nums):
    for j in range(1, n):
        key = nums[j]
        i = j - 1
        while i >= 0 and compare_str(nums[i], key):
            nums[i+1] = nums[i]
            i = i - 1
        nums[i+1] = key
    print(nums)
    biggest = ''.join(nums)
    return int(biggest)


def compare_str(str1, str2):
    strcom1 = int(str1+str2)
    strcom2 = int(str2+str1)
    if strcom2 > strcom1:
        return True
    else:
        return False

if __name__ == '__main__':
    n = int(input())
    nums = input()
    nums = nums.split(' ')
    nums.sort(compare_str, reverse=True)
    print(''.join(nums))
'''
def cmp(a, b):
    ab = int(a+b)
    ba = int(b+a)
    return 1 if ab > ba else -1
num = input()
l=input().split(' ')
l.sort(cmp, reverse=True)
print(int(''.join(l)))