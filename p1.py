# wapp to perform set operations

java_batch = {"amit", "sumit", "neha"}
android_batch = {"amit", "pooja", "sagar", "raj"}

# students who joined both the batches
r1 = java_batch.intersection(android_batch)
print(r1)
r2 = java_batch & android_batch

# all the students
r3 = java_batch.union(android_batch)
r3 = java_batch | android_batch
print(r3)
# | = pipe
# students who joined java but not android
r5 = java_batch.difference(android_batch)
print(r5)
r6 = java_batch - android_batch
print(r6)

# students who joined java but not android
r7 = android_batch - java_batch
print(r7)
print(android_batch)

