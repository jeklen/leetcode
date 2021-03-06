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
    print(nums)
    biggest = join_biggest_int(n, nums)
    print(biggest)