print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

from queues2 import Queue

fifo = Queue("1st", "2nd", "3rd")
print("\t     `Stack: 1st, 2nd, 3rd`\n")
print("\t\tNos of stack: ", len(fifo))

for element in fifo:
    print("\n\tThis is the order output using FIFO: \n\t\t\t", element)


print("\n\tCurrent number of stack:", len(fifo))
print()