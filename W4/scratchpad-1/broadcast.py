a = sc.parallelize([1,2,3,4])
broadcastVar = sc.broadcast(True)
a.filter(lambda x:broadcastVar)
print(a.collect())