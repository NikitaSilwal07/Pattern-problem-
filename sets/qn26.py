#26.How do you perform set operations (union, intersection, etc.) on more than two sets?
s1={10,20,30,40,50}
s2={40,20,10,60}
s3={10,50,70,30}
print(s1.intersection(s2.union(s3.difference(s1)))) 
print(s1.union(s2,s3)) 
print(s1.difference(s2,s3)) 