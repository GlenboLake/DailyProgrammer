'''
Created on Jun 3, 2015

@author: ghaber
'''
import unittest

from dailyprogrammer.C201P_priority_queue import DoublePriorityQueue


class DoublePriorityQueueTest(unittest.TestCase):
    """Test suite for DoublePriorityQueue"""

    def test_countEmpty(self):
        """Test counting an empty DPQ."""
        dpq = DoublePriorityQueue()
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)
        
    def test_countOneNode(self):
        """Test counting a DPQ with one entry."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.enqueue(string, priorityA, priorityB)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_countTwoNodes(self):
        """Test counting a DPQ with two entries."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popQueueOnce(self):
        """Test popping the queue in a DPQ once."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.enqueue(string, priorityA, priorityB)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeue()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popQueueTwice(self):
        """Test popping the queue in a DPQ twice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeue()
        self.assertEqual(expected, actual)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.dequeue()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popQueueThrice(self):
        """Test popping the queue in a DPQ thrice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string3 = "Charlie"
        priorityA3 = 3.45
        priorityB3 = 6.78
        dpq.enqueue(string3, priorityA3, priorityB3)
        expected = 3
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeue()
        self.assertEqual(expected, actual)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.dequeue()
        self.assertEqual(expected, actual)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Charlie", 3.45, 6.78)
        actual = dpq.dequeue()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popPriorityQueueAOnce(self):
        """Test popping the first priority queue in a DPQ once."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.enqueue(string, priorityA, priorityB)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeueA()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popPriorityQueueATwice(self):
        """Test popping the first priority queue in a DPQ twice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.dequeueA()
        self.assertEqual(expected, actual)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeueA()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popPriorityQueueAThrice(self):
        """Test popping the first priority queue in a DPQ thrice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string3 = "Charlie"
        priorityA3 = 3.45
        priorityB3 = 6.78
        dpq.enqueue(string3, priorityA3, priorityB3)
        expected = 3
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.dequeueA()
        self.assertEqual(expected, actual)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Charlie", 3.45, 6.78)
        actual = dpq.dequeueA()
        self.assertEqual(expected, actual)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeueA()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)
    
    def test_popPriorityQueueBOnce(self):
        """Test popping the second priority queue in a DPQ once."""
        dpq = DoublePriorityQueue()
        string = "Alice"
        priorityA = 1.23
        priorityB = 4.56
        dpq.enqueue(string, priorityA, priorityB)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeueB()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popPriorityQueueBTwice(self):
        """Test popping the second priority queue in a DPQ twice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeueB()
        self.assertEqual(expected, actual)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.dequeueB()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_popPriorityQueueBThrice(self):
        """Test popping the second priority queue in a DPQ thrice."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string3 = "Charlie"
        priorityA3 = 3.45
        priorityB3 = 6.78
        dpq.enqueue(string3, priorityA3, priorityB3)
        expected = 3
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Charlie", 3.45, 6.78)
        actual = dpq.dequeueB()
        self.assertEqual(expected, actual)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Alice", 1.23, 4.56)
        actual = dpq.dequeueB()
        self.assertEqual(expected, actual)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        expected = ("Bob", 7.89, 0.12)
        actual = dpq.dequeueB()
        self.assertEqual(expected, actual)
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)

    def test_clear(self):
        """Test clearing a DPQ."""
        dpq = DoublePriorityQueue()
        string1 = "Alice"
        priorityA1 = 1.23
        priorityB1 = 4.56
        dpq.enqueue(string1, priorityA1, priorityB1)
        expected = 1
        actual = len(dpq)
        self.assertEqual(expected, actual)
        string2 = "Bob"
        priorityA2 = 7.89
        priorityB2 = 0.12
        dpq.enqueue(string2, priorityA2, priorityB2)
        expected = 2
        actual = len(dpq)
        self.assertEqual(expected, actual)
        dpq.clear()
        expected = 0
        actual = len(dpq)
        self.assertEqual(expected, actual)


if __name__ == "__main__":
    unittest.main()