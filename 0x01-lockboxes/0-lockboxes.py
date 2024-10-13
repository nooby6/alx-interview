def canUnlockAll(boxes):
    n = len(boxes)  # Number of boxes
    unlocked = set([0])  # Set to track unlocked boxes, initially only box 0 is unlocked
    keys = set(boxes[0])  # Keys found in the first box

    # Continue unlocking boxes until no new boxes can be unlocked
    while keys:
        new_keys = set()  # New set to collect keys from newly unlocked boxes

        for key in keys:
            if key < n and key not in unlocked:  # Ensure key is valid and the box isn't already unlocked
                unlocked.add(key)  # Mark the box as unlocked
                new_keys.update(boxes[key])  # Add new keys from this unlocked box

        keys = new_keys  # Move to the next set of keys

    return len(unlocked) == n  # Check if all boxes are unlocked

