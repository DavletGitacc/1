class Bank:
    def __init__(self, money:int,user):
        self.__money=money
        self.__user=user
    def setmoney(self, money):
        self.__money=money
    def getmoney(self):
        return self.__money
    def setname(self, user):
        self.__user3=user
    def getname(self):
        return self.__user
    def moneyX(self):
        self.__money+=int(input("Введите сумму:"))
    def _kill(self):
        self.__money=0
    def __jackpot(self):
        self.__money*=10
user=Bank(10000,'Oleg Arigato')
user.moneyX()
print(f"moneX:{user.Bank._money}")
user._Bank__jackpot()
print(f"jackpot:{user._Bank__money}")
user._kill()
print(f"kill:{user._Bank__money}")
