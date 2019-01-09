class worker:
    def __init__(self, name, pay):
        self.name=name
        self.pay=pay
    def lastname(self): return self.name#.split(-1)
    def giveRaise(self,percent): self.pay *= (1.0+percent)
bob=worker('Bob Brine',25000)
curt=worker('Curt Wan',35000)
input()
print('bob='+bob.lastname())
bob.giveRaise(0.1)
print('bob pay = '+str(int(bob.pay)))

