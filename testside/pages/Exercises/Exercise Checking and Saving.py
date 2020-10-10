class Saving:
    def __init__(self, interest_rate):
        self.interest_rate = interest_rate

    def transfer(self, amount):
        return amount * self.interest_rate


class Checking:
    def __init__(self, account=0, interest_rate=0):
        if account <= 250:
            print("You can't open an account because you require $250")
        else:
            self.account = account
            self.interest_rate = interest_rate

