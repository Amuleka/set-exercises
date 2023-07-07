def find_intersection(set1, set2):
    # Complete this function
    intersection = set1.intersection(set2)
    return intersection

# Test Cases
# Case 1: Sets with common elements
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(find_intersection(set1, set2))  # Expected output: {4, 5}

# Case 2: Sets with no common elements
set3 = {1, 2, 3}
set4 = {4, 5, 6}
print(find_intersection(set3, set4))  # Expected output: set()

# Case 3: One set is a subset of the other
set5 = {1, 2, 3}
set6 = {1, 2, 3, 4, 5}
print(find_intersection(set5, set6))  # Expected output: {1, 2, 3}
