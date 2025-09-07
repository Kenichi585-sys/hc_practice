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
    
        
class Juice:
    def __init__(self, name, price):
        self.__name = name
        self.__price = price

    def get_name(self):
        return self.__name
    
    def get_price(self):
        return self.__price
    

class VendingMachine:
    def __init__(self):
        self.__juices = []
        self.__sales = 0

        pepsi = Juice('ペプシ', 150)
        self.__juices.append({"name": pepsi, "stock": 5})

        monster = Juice('モンスター', 230)
        self.__juices.append({"name": monster, "stock": 5})

        irohasu = Juice('いろはす', 120)
        self.__juices.append({"name": irohasu, "stock": 5})

# 自動販売機はペプシが購入できるかどうかを取得できる。
    def get_available_juice(self):
        self.__available = []
        for juice in self.__juices:
            if juice["stock"] > 0:
                self.__available.append(juice)
        if self.__available == []:
            print('購入可能商品はありません。')
        return self.__available
                
# ジュース値段以上のチャージ残高がある条件下で購入操作を行うと以下の動作をする
    def buy_juice(self, suica, juice_name, quantity):
        if quantity <= 0 or not isinstance(quantity, int):
            raise ValueError('1以上の整数でないと購入できません。')
        # ジュース値段以上のチャージ残高があるかを確認する
        for juice in self.__juices:
            if juice["name"].get_name() == juice_name:
                if suica.get_balance() > juice["name"].get_price() and juice["stock"] > quantity:
                # 自動販売機はジュースの在庫を減らす
                    juice["stock"] -= quantity
                # 売り上げ金額を増やす
                    total = juice["name"].get_price() * quantity
                    self.__sales += total
                # Suica のチャージ残高を減らす
                    my_balance = suica.get_balance()
                    my_balance -= total
                    return True
                else:
                    raise ValueError('チャージ残高が足りないか、在庫がないため購入できません。')
        
    def add_inventory(self, juice_name, quantity):
        if quantity > 0 and isinstance(quantity, int):
            for juice in self.__juices:
                if juice["name"].get_name() == juice_name:
                    juice["stock"] += quantity
                return juice["stock"]



my_suica = Suica()
vending =VendingMachine()

print(vending.add_inventory('ペプシ', 2))