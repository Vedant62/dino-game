set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = {1,3}
print(set1 | set2)  #union of set1 and set2 
print(set1  & set2) #intersection

print(set1.symmetric_difference(set2)) #prints everything except intersection
print(set1 ^ set2)  # things in set1 and set2 but not in both = A + B - A&B

print(set1 - set2)  #elements in set1 that are not in set 2 
print(set1.difference(set2))

print(set3.issubset(set1)) #checks is set3 is subset of set1
print(max(set1),min(set1))

print(set1.isdisjoint(set2)) #check if no elements are common

(set1.difference_update(set2))# set1 = set1 - set2 , removes intersection
print(set1, set2)