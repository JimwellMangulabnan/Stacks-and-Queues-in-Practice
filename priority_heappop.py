print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

from heapq import heappop
from heapq import heappush

fruits = []
heappush(fruits, "orange")
heappush(fruits, "apple")
heappush(fruits, "banana")

print("\n\tThe first element appeared is: ",heappop(fruits))

print("\n\tThe remaining elements are: ",fruits)
print()

