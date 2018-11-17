money = input('총액을 입력하세요')
amount = int(money)
if amount <100 :
    discount = amount * 0.05
    print("5% 할인금액 ",discount)
else :
    discount = amount * 0.1
    print("10% 할인금액 ",discount)

