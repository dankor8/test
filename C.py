class Room:
    instances = []
    def __init__(self, i, a, b, w, h):
        self.instances.append(self)
        self.i = i + 1
        self.s = a * b * 10000 - w * h
    def __str__(self):
        return str(self.i)
for i in range(int(input())):
    Room(i, *list(map(int, input().split())))
print(*sorted(Room.instances, key=lambda r: r.s + r.i / 10000))