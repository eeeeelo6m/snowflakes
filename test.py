class Man():
    def __init__(self):
        self.god_znachenie=2022
        self.vosrast=0
    @property
    def god(self):
        return 2022-self.vosrast
    @god.setter
    def god(self,voum):
        self.god_znachenie=voum




















chell=Man()
print(chell.vosrast,chell.god)
chell.vosrast=10
print(chell.vosrast,chell.god)
chell.god=1
print(chell.vosrast,chell.god)
