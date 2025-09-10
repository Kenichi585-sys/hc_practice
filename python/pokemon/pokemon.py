# クラスとは
class Pokemon:
    def __init__(self):
        self.name = "リザードン"
        self.type1 = "ほのお"
        self.type2 = "ひこう"
        self.hp = 100

    def attack(self):
        print(f"{self.__name}のこうげき！")


# コンストラクタ
class Pokemon:
    def __init__(self, name):
        self.name = name


class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 =type1
        self.type2 =type2
        self.hp = hp


class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type
        self.exText = f"{self.name}は{self.type}タイプのポケモン。"

# 継承とポリモーフィズム
# 良くない例
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self._type1 = type1
        self._type2 = type2
        self._hp = hp

    def attack(self):
        print(f"{self.name}のこうげき!")

    def thunderboltAttack(self):
        print(f"{self.name}の10万ボルト!")

    def watergunAttack(self):
        print(f"{self.name}のみずでっぽう!")


class Pikachu(Pokemon):
    def __init__(self, _name, _type1, _type2, _hp):
        super().__init__(_name, _type1, _type2, _hp)
    
    def attack(self):
        print(f"{self.name}の10万ボルト!")
        # ここでattackはオーバーライドしているので上のthunderboltAttackとwatergunAttackはなくていいと思いますが、
        # 課題としてどのあたりを書いておけばいいのか良くわかってないので一応残してます。


class Pikachu(Pokemon):
    def __init__(self, _name, _type1, _type2, _hp):
        super().__init__(_name, _type1, _type2, _hp)
    
    def attack(self):
        super().attack()
        print(f"{self._name}の10万ボルト!")



# クラスの抽象化
class Pokemon:
    def __init__(self, name="String", type1="String", type2="String", hp=int):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack():
        pass


class Pikachu(Pokemon):
    def __init__(self, name="ピカチュウ", type1="でんき", type2="かくとう", hp=100):
        super().__init__(name, type1, type2, hp)
    
    def attack(self):
        print(f"{self._name}の10万ボルト!")


# 抽象クラスの使い方余談
class Pokemon:
    def __init__(self, name="String", type1="String", type2="String", hp=int):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        print(f"{self.name}のこうげき!")


class Pikachu(Pokemon):
    def __init__(self, name="String", type1="String", type2="String", hp=int):
        super().__init__(name, type1, type2, hp)

    def attack(self):
        super().__init__()
        print(f"{self._name}の10万ボルト!")








class Pokemon:
    def __init__(self, name="リザードン",  type1="ほのお",  type2="ひこう",  hp=10):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        print(f"{self._name}のこうげき！")


# 抽象クラスとインターフェース
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        pass


# カプセル化の例
class Pokemon:
    def __init__(self, __name, type1, type2, hp):
        self.__name = __name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def change_name(self, new_name):
        if new_name == 'うんこ':
            print("不適切な名前です")
            return
        else:
            name = new_name

    def get_name(self):
        return self.__name