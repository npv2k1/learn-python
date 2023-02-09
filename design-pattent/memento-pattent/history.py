class History:
    states =  list()
    def __init__(self):
        self.states = []
    def push(self, state):
        self.states.append(state)
    def pop(self):
        return self.states.pop()
        
    