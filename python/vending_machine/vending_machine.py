from juice import Juice


class VendingMachine:
    def __init__(self):
        pepsi = Juice('ペプシ', 150)
        monster = Juice('モンスター', 230)
        irohasu = Juice('いろはす', 120)

        self.__stocks = {pepsi: 5, monster: 5, irohasu: 5}

        self.__sales = 0

# 自動販売機はペプシが購入できるかどうかを取得できる。
    def get_available_juice(self):
        self.__available = []
        for stock in self.__stocks.values():
            if stock > 0:
                self.__available.append(stock)
        if self.__available == []:
            print('購入可能商品はありません。')
        return self.__available
                
# ジュース値段以上のチャージ残高がある条件下で購入操作を行うと以下の動作をする
    def buy_juice(self, suica, juice_name, quantity):
        if quantity <= 0 or not isinstance(quantity, int):
            raise ValueError('1以上の整数でないと購入できません。')
        # ジュース値段以上のチャージ残高があるかを確認する
        for juice, stock in self.__stocks.items():
            if not juice.get_name() == juice_name:
                raise ValueError('そのような商品はありません。')
            if stock < quantity:
                raise ValueError('在庫がないため購入できません。')
            else:
                stock -= quantity
            # ちゃんと支払いできることを確認してから売り上げ金額を増やす
                suica.get_balance() > juice.get_price()
                total = juice.get_price() * quantity
                suica.reduce_money(total)
                self.__sales += total
                return True
                
        
    def add_inventory(self, juice_name, quantity):
        if quantity > 0 and isinstance(quantity, int):
            for juice, stock in self.__stocks.items():
                if juice.get_name() == juice_name:
                    stock += quantity
                return stock
