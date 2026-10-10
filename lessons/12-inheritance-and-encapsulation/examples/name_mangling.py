class Secretive:
    def __init__(self):
        self.public = "anyone can see me"
        self._protected = "please don't look at me"
        self.__private = "you can't see me... or can you?"

    def reveal(self):
        return self.__private


s = Secretive()
print(s.public)
print(s._protected)
print(s.reveal())
print(s._Secretive__private)
print(s.__private)
