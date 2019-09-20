class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
      if self.current == self.capacity:
        self.current = 0
      self.storage[self.current] = item
      self.current += 1


  def get(self):
    my_list = []
    for item in self.storage:
      if item == None:
        pass
      else:
        my_list.append(item)
    
    return my_list

# ********* TESTS ************

buffer = RingBuffer(3)

# buffer.get() # returns []

buffer.append('a')
buffer.append('b')
buffer.append('c')

# print(buffer.get()) # returns [a, b, c]

buffer.append('d')

print(buffer.get()) # returns [d, b, c]

# buffer.append('e')
# buffer.append('f')

# buffer.get() # returns [d, e, f]