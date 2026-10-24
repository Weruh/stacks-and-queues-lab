import unittest
from unittest.mock import patch
from custom_queue import Queue
from custom_stack import is_valid_parentheses

class TestQueueLab(unittest.TestCase):
    def setUp(self):
        self.queue = Queue()
        self.customers = [f"Customer #{i}" for i in range(1, 21)]
        for customer in self.customers:
            self.queue.enqueue(customer)
        print(f"\n[Setup] Queue initialized with customers: {self.queue.items}")

    def test_enqueue_count(self):
        print("\n[Test] Enqueue count...")
        self.assertEqual(len(self.queue.items), 20)
        print("[Pass] Queue contains 20 customers")

    def test_peek(self):
        print("\n[Test] Peek...")
        front = self.queue.peek()
        print(f"[Peeked] Customer at front: {front}")
        self.assertEqual(front, "Customer #1")
        print("[Pass] Peek returns the correct customer")

    def test_select_and_announce_winner(self):
        print("\n[Test] Select and announce winner...")
        winner = self.queue.select_and_announce_winner()
        print(f"[Winner Selected] {winner}")
        self.assertIsInstance(winner, str)
        self.assertTrue(winner.startswith("Customer #"))
        self.assertNotIn(winner, self.queue.items)
        print(f"[Queue State] Remaining: {self.queue.items}")
        print("[Pass] Winner selected and queue dequeued properly")

    def test_fifo_and_empty_queue(self):
        self.assertEqual(self.queue.dequeue(), "Customer #1")
        self.assertEqual(self.queue.peek(), "Customer #2")
        for _ in range(19):
            self.queue.dequeue()
        self.assertTrue(self.queue.is_empty())
        self.assertIsNone(self.queue.peek())
        self.assertIsNone(self.queue.dequeue())
        self.assertIsNone(self.queue.select_and_announce_winner())

    def test_winner_removes_exactly_through_selected_position(self):
        with patch("custom_queue.random.randrange", return_value=2):
            winner = self.queue.select_and_announce_winner()
        self.assertEqual(winner, "Customer #3")
        self.assertEqual(self.queue.items, self.customers[3:])

    def test_duplicate_names_still_use_selected_position(self):
        queue = Queue()
        for name in ("Alex", "Sam", "Alex", "Lee"):
            queue.enqueue(name)
        with patch("custom_queue.random.randrange", return_value=2):
            self.assertEqual(queue.select_and_announce_winner(), "Alex")
        self.assertEqual(queue.items, ["Lee"])

class TestStackLab(unittest.TestCase):
    def test_valid(self):
        print("\n[Test] Valid parentheses strings...")
        cases = ["()", "{[()]}", "([]{})"]
        for s in cases:
            print(f"[Check] Testing: {s}")
            result = is_valid_parentheses(s)
            print(f"[Stack Check] Final result for {s}: {result}")
            self.assertTrue(result)
            print(f"[Pass] {s} is valid")

    def test_invalid(self):
        print("\n[Test] Invalid parentheses strings...")
        cases = ["(", "([)]", "(()"]
        for s in cases:
            print(f"[Check] Testing: {s}")
            result = is_valid_parentheses(s)
            print(f"[Stack Check] Final result for {s}: {result}")
            self.assertFalse(result)
            print(f"[Pass] {s} is invalid")

    def test_empty_and_non_bracket_characters(self):
        self.assertTrue(is_valid_parentheses(""))
        self.assertFalse(is_valid_parentheses("(a)"))
        self.assertFalse(is_valid_parentheses("[] "))
        self.assertFalse(is_valid_parentheses("]"))

if __name__ == "__main__":
    unittest.main()
