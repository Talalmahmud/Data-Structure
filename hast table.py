#without collision
class HashTable:
    def __init__(self):
        self.MAX = 100
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def add(self, key, value):
        h = self.get_hash(key)
        self.arr[h] = value

    def get(self, key):
        key = self.get_hash(key)
        print(self.arr[key])

    def print_arr(self):
        print(self.arr)


t = HashTable()
t.add("talal", 2)
t.add("rahim", 5)
t.add("karim", 7)
t.get("rahim")
t.print_arr()
