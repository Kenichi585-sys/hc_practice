from juice import Juice


class VendingMachine:
    def __init__(self):
        self.__juice_stock = []
        self.__sales = 0

        pepsi = Juice('ペプシ', 150)
        self.__juice_stock.append([pepsi, 5])

        monster = Juice('モンスター', 230)
        self.__juice_stock.append([monster, 5])

        irohasu = Juice('いろはす', 120)
        self.__juice_stock.append([irohasu, 5])

# 自動販売機はペプシが購入できるかどうかを取得できる。
    def get_available_juice(self):
        self.__available = []
        for juice in self.__juice_stock:
            if juice[1] > 0:
                self.__available.append(juice)
        if self.__available == []:
            print('購入可能商品はありません。')
        return self.__available
                
# ジュース値段以上のチャージ残高がある条件下で購入操作を行うと以下の動作をする
    def buy_juice(self, suica, juice_name, quantity):
        if quantity <= 0 or not isinstance(quantity, int):
            raise ValueError('1以上の整数でないと購入できません。')
        # ジュース値段以上のチャージ残高があるかを確認する
        for juice in self.__juice_stock:
            if not juice[0].get_name() == juice_name:
                raise ValueError('そのような商品はありません。')
            if juice[1] < quantity:
                raise ValueError('在庫がないため購入できません。')
            else:
                juice[1] -= quantity
            # ちゃんと支払いできることを確認してから売り上げ金額を増やす
                suica.get_balance() > juice[0].get_price()
                total = juice[0].get_price() * quantity
                suica.reduce_money(total)
                self.__sales += total
                return True
                
        
    def add_inventory(self, juice_name, quantity):
        if quantity > 0 and isinstance(quantity, int):
            for juice in self.__juice_stock:
                if juice[0].get_name() == juice_name:
                    juice[1] += quantity
                return juice[1]
