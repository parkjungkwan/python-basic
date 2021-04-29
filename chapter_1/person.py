class Person:
   def __init__(self, name, age, address):
       self.name = name
       self.age = age
       self.address = address

   def greeting(self):
        print("안녕하세요. 저는 {0} 입니다".format(self.name)  )

   @staticmethod
   def main():
       maria = Person('마리아', 20, '서울')
       maria.greeting()

if __name__ == "__main__":
   Person.main()



