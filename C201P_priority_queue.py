"""
Created on Jun 3, 2015

@author: ghaber
"""
class DoublePriorityQueue(object):
    """
    A priority queue that contains two different priority fields
    """

    def __init__(self):
        """
        Constructor
        """
        self.clear()
    
    def enqueue(self, item, priority_a, priority_b):
        self._queue.append((item, priority_a, priority_b))
    
    def dequeue(self):
        return self._queue.pop(0)
    
    def _dequeue_by_priority(self, priority):
        idx = 0
        for item in range(len(self._queue)):
            if self._queue[item][priority] > self._queue[idx][priority]:
                idx = item
        return self._queue.pop(idx)
    
    def dequeueA(self):
        return self._dequeue_by_priority(1)
    
    def dequeueB(self):
        return self._dequeue_by_priority(2)
    
    def __len__(self):
        # 'Count' method is not Pythonic!
        return len(self._queue)

    def clear(self):
        self._queue = []