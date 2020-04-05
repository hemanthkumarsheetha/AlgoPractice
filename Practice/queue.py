from collections import deque
max_len = int(input())
d = deque(maxlen=max_len)
d.append(2)
d.appendleft(23)
for e in d:print(e)
d.append(4)
d.popleft()
for e in d:print(e)
