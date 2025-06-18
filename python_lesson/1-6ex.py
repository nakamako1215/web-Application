class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,name):
        self.__name = name
    
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,age):
        if age < 0:
            raise ValueError("age must be larger than 0")
        self.__age = age
    
class Student(Person):
    def __init__(self,name,age,grade):
        self.grade = grade
        super().__init__(name,age)
    
    def self_introduction(self):
        print(f"私の名前は{self.name}です。{self.grade}の{self.age}歳です。")
        
if __name__ == "__main__":
    p1 = Person('makoto',22)
    p1.name = 'takashi'
    print(p1.name)
    p1.age = 10
    print(p1.age)
    p2 = Student('mikako',30,'女')
    p2.self_introduction() 