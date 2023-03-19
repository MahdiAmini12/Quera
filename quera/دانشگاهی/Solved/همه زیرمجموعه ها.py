def generate_subsets(n, elements):
    if n == 0:
        return [[]]
    subsets = generate_subsets(n-1, elements)
    new_subsets = []
    for subset in subsets:
        new_subset = subset + [n]
        new_subsets.append(new_subset)
    return subsets + new_subsets

n = int(input())
elements = sorted(list(range(1, n+1)))
subsets = generate_subsets(n, elements)
for subset in sorted(subsets):
    print("{" + ", ".join(str(x) for x in subset) + "}")
