class Gugudan(object):
    dan = 0

    def print_selected_dan(self):
        for i in range(1, 10):
            print(f'{self.dan} * {i} = {self.dan * i} ')

    def print_selected_dan2(self):
        dict = {}
        for i in range(1, 10):
            dict[i] = self.dan * i
        print(dict)
        for k in dict.keys():
            print(f'{self.dan} * {k} = {dict.get(k)} ')

    @staticmethod
    def print_all_dan():
        for i in range(2, 10):
            for j in range(1, 10):
                print(f'{i} * {j} = {i * j}')




    @staticmethod
    def main():
        g = Gugudan()
        while 1:
            menu = input('0-exit 1-Selected Dan 2-All Dan 3-Selected Dan with Dict\n')
            if menu=='0':
                print('Exit Program')
                break
            elif menu=='1':
                g.dan = int(input('Input Dan'))
                g.print_selected_dan()
            elif menu=='3':
                g.dan = int(input('Input Dan'))
                g.print_selected_dan2()
            elif menu=='2':
                g.print_all_dan()
            else:
                print('Wrong Number')
                continue

Gugudan.main()



