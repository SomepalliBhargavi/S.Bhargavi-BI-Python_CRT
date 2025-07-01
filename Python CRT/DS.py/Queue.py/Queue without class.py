from collections import deque
queue=deque()
queue.append('A')
queue.append('B')
queue.append('C')
print("Queue after enqueing:",queue)
first=queue.popleft()
print("Dequeued element:",queue)
print("Queue after dequeuing:",queue)
if not queue:
    print("Queue is empty")
else:
    print("Queue is not empty")
print("Front element:",queue[0])