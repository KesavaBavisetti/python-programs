#Set Operations:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

#Union of two sets
union_set = set1.union(set2)
print(union_set)  #Output: {1, 2, 3, 4, 5, 6}

#Intersection of two sets
intersection_set = set1.intersection(set2)
print(intersection_set)  #Output: {3, 4}

#Difference between two sets
difference_set = set1.difference(set2)
print(difference_set)  #Output: {1, 2}

#Symmetric Difference (elements in either set, but not in both)
symmetric_difference_set = set1.symmetric_difference(set2)
print(symmetric_difference_set)  #Output: {1, 2, 5, 6}

#Membership Test:
my_set = {1, 2, 3, 4, 5}
print(3 in my_set)  #Output: True
print(6 not in my_set)  #Output: True