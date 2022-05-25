from account import Account

class Car:
    
    id = int
    lincese = str
    driver = Account("","")
    passenger = int

    def __init__(self, license, driver):
        self.lincese = license
        self.driver = driver
