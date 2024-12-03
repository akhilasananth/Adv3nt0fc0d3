file = "Day1/day1.txt"
with open(file, "r") as f:
    vals = [list(map(int, line.strip().split('   '))) for line in f]

vals = list(zip(*vals))
l1 = list(vals[0])
l2 = list(vals[1])

times_appeared = {}

for n in l2:
    if n in times_appeared:
        times_appeared[n] += 1
    else:
        times_appeared[n] = 1

similarity = []
for n in l1:
    if n in times_appeared:
        similarity.append(n*times_appeared[n])

similarity_score = sum(similarity)

print(similarity_score)


# def main():
#     # read inputs
#     file = "1.txt"
#     with open(file, "r") as f:
#         vals = [list(map(int, line.strip().split('   '))) for line in f]
#
#     # Transpose the lists of lists
#     left, right = list(zip(*vals))
#
#     right_dict = dict()
#     for r in right:
#         right_dict[r] = right_dict.get(r, 0) + 1
#
#     sim = sum((right_dict.get(l, 0) * l) for l in left)
#     return sim