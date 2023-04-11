class Event:
    def __init__(self):
        self.listeners = []

    def __iadd__(self, other):
        self.listeners.append(other)

    def __isub__(self, other):
        if other in self.listeners:
            self.listeners.remove(other)

    def Trigger(self, args):
        for f in self.listeners:
            f(args)