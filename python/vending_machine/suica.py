class Suica:
    def __init__(self):
        self.__balance = 500

    def deposit(self, amount):
        if amount >= 100:
            self.__balance += amount
            return self.__balance
        else:
            raise ValueError("100円以上じゃないとチャージできません")
        
    def get_balance(self):
        return self.__balance
    
    def reduce_money(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            raise ValueError('チャージ残高が足りないため購入できません。')