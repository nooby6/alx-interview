#!/usr/bin/python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.

    Args:
        boxes (list of lists): Each list contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    # Initialize the set of opened boxes and start with box 0
    opened_boxes = set([0])
    keys = [0]  # List to process boxes with keys

    # Process boxes as long as there are keys to check
    while keys:
        current_box = keys.pop()  # Get the current box to check
        for key in boxes[current_box]:
            if key not in opened_boxes and key < len(boxes):
                opened_boxes.add(key)
                keys.append(key)

    # Check if the number of opened boxes equals the total number of boxes
    return len(opened_boxes) == len(boxes)
