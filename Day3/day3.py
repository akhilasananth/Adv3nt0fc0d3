import re
from functools import reduce
from operator import mul

file = "day3.txt"

with open(file, "r") as f:
    lines = f.readlines()

pattern = re.compile(r'mul\((\d+,\d+)\)|(do\(\))|(don\'t\(\))', re.IGNORECASE)
products = []

is_multiply = True

for s in lines:
    pattern_matches = re.findall(pattern, s)

    for nums_str in pattern_matches:
        nums, do, do_not = nums_str

        if do:
            is_multiply = True
        elif do_not:
            is_multiply = False

        if is_multiply and nums:
            products.append(reduce(mul, list(map(int, nums.split(',')))))


print(sum(products))
