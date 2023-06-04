def is_queue_empty(queue):
    return queue.is_empty()

# Assume my_queue is a pre-defined queue
if is_queue_empty(my_queue):
    print("Queue is empty.")
else:
    print("Queue is not empty.")

def get_queue_size(queue):
    return queue.size()

# Assume my_queue is a pre-defined queue
size = get_queue_size(my_queue)
print("Queue size:", size)