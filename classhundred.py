class Atm(object):
    def __init__(self,User,Id,Balance,Age):
        self.User = User
        self.Id = Id
        self.Balance = Balance
        self.Age = Age
      
    def start(self):
        print("started")
        
    def stop(self):
        print("stopped")

    def accelerate(self):
        print("started")
        
        
userone = Atm("Arnav","123456","2000","13")
usertwo = Atm("Arnnav","123","200","43")
print(userone.start())