class computer:

    def __init__(self,cpu,ram):
        self.cpu = cpu
        self.ram = ram


    def config(self):
        print("config is :", self.cpu,self.ram)


com1 = computer('i5','16') # here we are passing three arguments in computer(com1,cpu,ram)
com2 = computer('ryzen3',8) # taking com1 & com2 into arguments by default


com1.config()
com2.config()
