from suica import Suica
from vending_machine import VendingMachine

suica = Suica()
vending =VendingMachine()

print(vending.buy_juice(suica, 'ペプシ', 2))
