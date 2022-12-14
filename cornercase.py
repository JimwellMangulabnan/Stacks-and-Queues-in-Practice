print("\n\t*********  PROGRAMMED BY  ********")
print("\t***** JIMWELL L. MANGULABNAN *****")
print("\t********** BSCOE 2-2 *************")
print()

from queues6 import PriorityQueue
from dataclasses import dataclass

CRITICAL = 3
IMPORTANT = 2
NEUTRAL = 1


@dataclass
class Message:
    event: str


wipers = Message("Windshield wipers turned on")
hazard_lights = Message("Hazard lights turned on")

print(wipers < hazard_lights)

messages = PriorityQueue()
messages.enqueue_with_priority(NEUTRAL, "Radio station tuned in")
messages.enqueue_with_priority(CRITICAL, "Brake pedal depressed")
messages.enqueue_with_priority(CRITICAL, wipers)
messages.enqueue_with_priority(IMPORTANT, hazard_lights)

print()
print(messages.dequeue())
print()