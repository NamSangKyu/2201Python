class Count:
    class_count = 0 #클래스 변수, 인스턴스들끼리 공유하는 변수

    # 클래스 메서드는 직접적으로 생성을 안해도 접근이 가능
    @classmethod
    def add_count(cls):
        cls.class_count += 1

    @staticmethod
    def static_method():
        # 클래스 메서드나 변수에 직접 접근이 불가
        print('인스턴스 생성 없이 사용가능한 메서드')
        Count.class_count += 1 #클래스 명으로 접근했기때문에 접근이 가능

c1 = Count()
c2 = Count()

c1.add_count()
c2.add_count()
Count.add_count()
print(c1.class_count)
print(c2.class_count)
Count.static_method()
print(c2.class_count)
