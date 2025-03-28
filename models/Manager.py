class Manager:
    def __init__(self,ManagerId, ManagerName, UserName, Password):
        self.ManagerId=ManagerId
        self.ManagerName=ManagerName
        self.UserName=UserName
        self.Password=Password
    def __str__(self):
        return f"{self.ManagerId}\t{self.ManagerName}"