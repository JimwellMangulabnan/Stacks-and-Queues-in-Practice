print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

from queues3 import Stack

lifo = Stack("`1st`", "`2nd`", "`3rd`")

print("\t     `Stack: 1st, 2nd, 3rd`\n")
print("\t\tNos of stack: ", len(lifo))

for element in lifo:
    print("\n\tThis is the order output using LIFO: \n\t\t\t",element)
print()
lifo = []

lifo.append("1st")
lifo.append("2nd")
lifo.append("3rd")

print("The following elements are the order output of LIFO stacks: \n")
print("\t\t\t",lifo.pop())

print("\t\t\t",lifo.pop())

print("\t\t\t",lifo.pop())
print()