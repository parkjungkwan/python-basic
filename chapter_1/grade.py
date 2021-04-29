class Grade:
    def __init__(self,name):
        self.name = name
        self.marks = []
        print(" {} 학생 ".format(name))

    def addmarks(self, mark):
        self.marks.append(mark)
    def avg(self):
        return sum(self.marks) / len(self.marks)


    '''
        클래스에 학생의 이름을 추가하신 후 
        학생의 과목은 총 5개 입니다.
        평균을 구한뒤,
        A ~ F 가 출력되도록 하시오.
        예) 홍길동 평균 87점 B
    '''
    @staticmethod
    def main():
        st = Grade(input("이름을 입력하세요"))
        for i in ["국어","영어","수학","사회","과학"]:
            st.addmarks(int(input(i+"점수 :")))
        avg = st.avg()
        if avg >= 90:
            grade = "A"
        elif avg >= 80:
            grade = "B"
        elif avg >= 70:
            grade = "C"
        elif avg >= 60:
            grade = "D"
        elif avg >= 50:
            grade = "E"
        else:
            grade = "F"
        print("{} 평균 {}점 {}".format(st.name, st.avg(), grade))


if __name__=="__main__":
    Grade.main()