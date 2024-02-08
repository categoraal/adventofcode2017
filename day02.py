import re
data = open('in2').read().strip().split('\n')

p1 = 0
p2 = 0
for i in data:
    nums = [int(k) for k in re.findall(r'\d+',i)]
    for n1 in range(len(nums)):
        for n2 in range(len(nums)):
            if nums[n1]%nums[n2] == 0 and nums[n1] != nums[n2]:
                p2 += int(nums[n1]/nums[n2])
    p1 += max(nums)-min(nums)

print(p1)
print(p2)