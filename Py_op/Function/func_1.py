
import math
print(math.ceil(100.9)) # 101
print(math.floor(100.9)) # 100

# Return self
# Returning self from a method simply means that your method returns a reference to the instance object 
# on which it was called. This can sometimes be seen in use with object oriented APIs that are 
# designed as a fluent interface that encourages method cascading. So, for example,

 class Counter(object):
     def __init__(self, start=1):
         self.val = start
     def increment(self):
         self.val += 1
         return self
     def decrement(self):
         self.val -= 1
         return self

 c = Counter()
# Now we can use method cascading:
c.increment().increment().decrement()
# <__main__.Counter object at 0x1020c1390>
# Notice, the last call to decrement() returned <__main__.Counter object at 0x1020c1390>, which is self. Now:

# Notice, you cannot do this if you did not return self:

 class Counter(object):
     def __init__(self, start=1):
         self.val = start
     def increment(self):
         self.val += 1
         # implicitely return `None`
     def decrement(self):
         self.val -= 1
         # implicitely return `None`

 c = Counter()
 c.increment().increment()
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# AttributeError: 'NoneType' object has no attribute 'increment'
#  c
# <__main__.Counter object at 0x1020c15f8>
