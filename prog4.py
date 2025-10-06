# Enter two collections of integers. Check
# (a) Whether they are of the same length
# (b) Whether they sum to the same value
# (c) Whether any value occurs in both


A = {1, 2, 3}
B = {3, 2, 1}
print(len(A) == len(B))
print(sum(A) == sum(B))
print(bool(A & B))



# True
# True
# True