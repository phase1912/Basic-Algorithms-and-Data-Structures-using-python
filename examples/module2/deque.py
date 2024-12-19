from collections import deque

d = deque()
print(d)  # deque([])

d.append('right')
d.appendleft('left')
print(d)  # deque(['left', 'right'])

d.pop()
d.popleft()
print(d)  # deque([])

d.extend(['a', 'b', 'c'])
d.extendleft(['x', 'y', 'z'])
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

d.rotate(2)
print(d)  # deque(['b', 'c', 'z', 'y', 'x', 'a'])

d.rotate(-2)
print(d)  # deque(['z', 'y', 'x', 'a', 'b', 'c'])

d = deque(maxlen=3)
d.extend([1, 2, 3])
print(d)  # deque([1, 2, 3])

d.append(4)
print(d)  # deque([2, 3, 4])

d = deque([1, 2, 3, 4, 2, 5])
print(d.count(2))  # 2