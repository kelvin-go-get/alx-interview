def canUnlockAll(boxes):
    if not boxes or len(boxes) == 0:
        return False

    n = len(boxes)
    opened = set([0])  # Start with the first box (index 0) being opened
    queue = [0]  # Queue for BFS starting from the first box

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < n and key >= 0 and key not in opened:
                opened.add(key)
                queue.append(key)

    return len(opened) == n
