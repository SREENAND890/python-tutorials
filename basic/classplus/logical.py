def find_p_sum(nums, t):
    s = set()
    pairs = []
    for num in nums:
        complement = t - num
        if complement in s:
            pairs.append([complement, num])
        s.add(num)
    return pairs

nums = [1, 2, 3, 4, 5, 6]
t = 7
op = find_p_sum(nums, t)
print(op)
