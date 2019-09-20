class RingBuffer:
  def __init__(self, capacity):
    self.capacity = capacity
    self.current = 0
    self.storage = [None]*capacity

  def append(self, item):
      if len(self.storage) == self.current:
        print('here!')
      else:
        self.storage.append(item)

  def get(self):
    return self.storage

# ********* TESTS ************

buffer = RingBuffer(3)

# buffer.get() # returns []

buffer.append('a')
# buffer.append('b')
# buffer.append('c')

print(buffer.get()) # returns [a, b, c]

# buffer.append('d')

# buffer.get # returns [d, b, c]

# buffer.append('e')
# buffer.append('f')

# buffer.get() # returns [d, e, f]