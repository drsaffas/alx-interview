#!/usr/bin/python3

def canUnlockAll(boxes):
    if len(boxes) == 0:
        return False

    keys = [0]  # Start with the key to the first box (box 0)
    visited = set()  # Set to keep track of visited boxes

    while keys:
        box = keys.pop()  # Get the last key from the list

        if box not in visited:
            visited.add(box)  # Mark the box as visited

            for key in boxes[box]:
                if key < len(boxes):
                    keys.append(key)  # Add new keys to the list

    return len(visited) == len(boxes)
