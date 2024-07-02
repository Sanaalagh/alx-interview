#!/usr/bin/python3
"""
0-lockboxes.py

This module contains the canUnlockAll function that determines if all boxes in
a list of lists can be unlocked. Each box may contain keys to other boxes,
and the goal is to determine if you can unlock all boxes starting with the
first one.

Function:
    canUnlockAll(boxes): Determines if all boxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked.
    Args:
        boxes (list of lists): List of lists representing the boxes
        and the keys they contain.
    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    n = len(boxes)
    unlocked = set([0])
    keys = boxes[0]

    while keys:
        new_keys = []
        for key in keys:
            if key not in unlocked and key < n:
                unlocked.add(key)
                new_keys.extend(boxes[key])
        keys = new_keys

    return len(unlocked) == n

# Test cases


if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Should print: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Should print: False
