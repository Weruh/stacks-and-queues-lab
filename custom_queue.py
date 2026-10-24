import random


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """Add an item to the back of the queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove the front item, or return None when the queue is empty."""
        if self.is_empty():
            return None
        return self.items.pop(0)

    def peek(self):
        """Return the front item without removing it, or None if empty."""
        if self.is_empty():
            return None
        return self.items[0]

    def is_empty(self):
        """Return whether the queue has no items."""
        return len(self.items) == 0

    def select_and_announce_winner(self):
        """
        Pick a random position, remove everyone through it, and announce the winner.

        Return None without changing the queue when it is empty.
        """
        if self.is_empty():
            return None

        winner_index = random.randrange(len(self.items))
        for _ in range(winner_index + 1):
            winner = self.dequeue()

        print(f"Winner: {winner}")
        return winner
