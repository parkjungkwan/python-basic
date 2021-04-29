class Money:
    def __init__(self):
        pass

    def main(self):
        money = input('총액을 입력하세요\n')
        amount = int(money)
        if amount <100 :
            discount = amount * 0.05
            print("5% 할인금액",discount)
        else :
            discount = amount * 0.1
            print("10% 할인금액 ",discount)


if __name__ == "__main__":
   money = Money()
   money.main()

