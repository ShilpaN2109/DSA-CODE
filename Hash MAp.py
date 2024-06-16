import collections
n = int(input())
arr = [int(x) for x in input().split()]

# precompute
mp = collections.Counter(arr)


q = int(input())
for _ in range(q):
    number = int(input())
    print(mp[number])
