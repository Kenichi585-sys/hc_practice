from juice import Juice


class VendingMachine:
    def __init__(self):
        pepsi = Juice('ペプシ', 150)
        monster = Juice('モンスター', 230)
        irohasu = Juice('いろはす', 120)

        self.__stocks = {pepsi: 5, monster: 0, irohasu: 5}

        self.__sales = 0

    def get_available_juice(self):
        for juice, stock in self.__stocks.items():
            if stock == 0:
                print(f"{juice}は在庫がないため購入できません。")
            else:
                print(f"現在{juice}は{stock}個まで購入可能です。")
                
    def buy_juice(self, suica, juice_name, quantity):
        if quantity <= 0 or not isinstance(quantity, int):
            raise ValueError('1以上の整数でないと購入できません。')
        for juice, stock in self.__stocks.items():
            if juice.get_name() == juice_name and stock >= quantity:
                total = juice.get_price() * quantity
                suica.pay(total)
                stock -= quantity
                self.__stocks[juice] = stock
                self.__sales += total
                return True
        raise ValueError('在庫がないかその商品はありません。')
        
    def add_inventory(self, juice_name, quantity):
        if quantity > 0 and isinstance(quantity, int):
            for juice, stock in self.__stocks.items():
                if juice.get_name() == juice_name:
                    stock += quantity
                return stock
