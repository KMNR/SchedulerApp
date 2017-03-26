class DJ:
    def __init__(self):
        self.timestamp = None
        self.username = None
        self.fullName = None
        self.seniority = None
        self.showName = None
        self.preferences = None
    def __lt__(self, other):
        return float(self.seniority) < float(other.seniority)
    def __getitem__(self,index):
        return self.preferences[index]
    def __setitem__(self,index,value):
        self.preferences[index] = value
    def __len__(self):
        return len(self.preferences)

class Schedule:
    def __init__(self, show, name, time):
        self.showName = show
        self.fullName = name
        self.timeSlot = time
    def __str__(self):
        return "\nShow Name: %s -  DJ Name: %s - Time Slot: %s" % (self.showName, 
                                                                self.fullName, 
                                                                self.timeSlot)
    def __repr__(self):
        return "\nShow Name: %s -  DJ Name: %s -  Time Slot: %s" % (self.showName, 
                                                                self.fullName, 
                                                                self.timeSlot)