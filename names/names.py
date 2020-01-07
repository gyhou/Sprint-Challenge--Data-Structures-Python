import time
from binary_search_tree import BinarySearchTree

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()
"""
Starter code runtime: O(n^2)
"""
duplicates = []
bst = BinarySearchTree(10000)
for name_1 in names_1:
    n = int(''.join(str(ord(c)) for c in name_1))
    bst.insert(n)
for name_2 in names_2:
    n = int(''.join(str(ord(c)) for c in name_2))
    if bst.contains(n):
        duplicates.append(name_2)

end_time = time.time()
print(f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print(f"runtime: {end_time - start_time} seconds")

# ---------- Stretch Goal -----------
# Python has built-in tools that allow for a very efficient approach to this problem
# What's the best time you can accomplish with no restrictions on techniques or data
# structures?
