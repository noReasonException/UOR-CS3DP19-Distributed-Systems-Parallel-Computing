a = sc.parallelize([1,2,3,4])
a.filter(lambda x:x>2)
print(a.collect())