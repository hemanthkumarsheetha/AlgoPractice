class HashTable(object):
    def __init__(self):
        self.table = [None]*100000

    def store(self,string):
        s = self.gethashvalue(string)
        if s!=-1:
            print(s)
            if self.table[s]:
                self.table[s].append(string)
            else:
                self.table[s] = string

    def gethashvalue(self,string):
        return ord(string[0])*120 + ord(string[1])

    def lookup(self,string):
        s = self.gethashvalue(string)
        if s!=-1:
            if self.table[s]:
                if string in self.table[s]:
                    return (True)
        return False
h = HashTable()
h.store("abcd")
h.store("sfdfd")
h.store("sdgdg")
print(h.lookup("abcd"))
print(h.lookup("weqww"))