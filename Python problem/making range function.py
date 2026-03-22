class Range_Iterable:
    def __init__(self,start,end):
        self.start = start
        self.end = end
    def __iter__(self):
        return Range_iterator(self)

class Range_iterator:
    def __init__(self,iterable_object):
        self.iterable = iterable_object
    def __iter__(self):
        return self
    def __next__(self):
        if self.iterable.start >= self.iterable.end:
            raise StopIteration
        current = self.iterable.start
        self.iterable.start += 1
        return current
for i in Range_Iterable(10,20):
    print(i)