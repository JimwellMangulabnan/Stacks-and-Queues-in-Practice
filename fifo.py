print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

from queues import Queue
print("\t     `Stack: 1st, 2nd, 3rd`\n")
fifo = Queue()
fifo.enqueue("1st")
fifo.enqueue("2nd")
fifo.enqueue("3rd")

print("The following elements are the order output of FIFO stacks: \n")
print("\t\t\t", fifo.dequeue())
print("\t\t\t", fifo.dequeue())
print("\t\t\t", fifo.dequeue())
print()
