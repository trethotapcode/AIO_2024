# Ward và Person có mối quan hệ cộng sinh, tồn tại độc lập.
class Ward:
    def __init__(self, name):
        self.__name = name

    __list_person = []

    def get_name(self):
        return self.__name

    def add_person(self, person):
        self.__list_person.append(person)

    def count_doctor(self):
        count_doctor = 0
        for person in self.__list_person:
            if type(person) is Doctor:
                count_doctor = count_doctor + 1

        return count_doctor

    def sort_age(self):
        # năm sinh càng nhỏ, tuổi càng lớn.
        self.__list_person = sorted(
            self.__list_person, key=lambda person: person.get_yob(), reverse=True)
        return self.__list_person

    def compute_average(self):
        # tạo một list các năm sinh của teacher
        a_teacher_list = [person.get_yob()
                          for person in self.__list_person if type(person) is Teacher]
        average_teacher = sum(a_teacher_list) / len(a_teacher_list)
        return average_teacher

    def describe(self):
        print(f"Ward name: {self.__name}")

        for person in self.__list_person:
            person.describe()


class Person:
    def __init__(self, name, yob):
        self._name = name
        self._yob = yob

    def get_name(self):
        return self._name

    def get_yob(self):
        return self._yob

    def describe(self):
        return f"Name: {self._name} - YoB: {self._yob}"


class Student(Person):

    def __init__(self, name, yob, grade):
        super().__init__(name, yob)
        self.__grade = grade

    def get_grade(self):
        return self.__grade

    def describe(self):
        print(f"Student - {super().describe()} - Grade: {self.__grade}")


class Teacher(Person):

    def __init__(self, name, yob, subject):
        super().__init__(name, yob)
        self.__subject = subject

    def get_grade(self):
        return self.__subject

    def describe(self):
        print(f"Teacher - {super().describe()} - Subject: {self.__subject}")


class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name, yob)
        self.__specialist = specialist

    def get_specialist(self):
        return self.__specialist

    def describe(self):
        print(f"Doctor - {super().describe()
                          } - Specialist: {self.__specialist}")


# test a
student1 = Student(name="studentA", yob=2010, grade="7")
# student1.describe()

teacher1 = Teacher(name="teacherA", yob=1969, subject="Math")
# teacher1.describe()

doctor1 = Doctor(name="doctorA", yob=1945, specialist="Endocrinologist")
# doctor1.describe()

# test b
teacher2 = Teacher(name="teacherB", yob=1995, subject="History")
doctor2 = Doctor(name="doctorB", yob=1975, specialist="Cardiologists")
ward1 = Ward(name="Ward 1")
ward1.add_person(student1)
ward1.add_person(teacher1)
ward1.add_person(teacher2)
ward1.add_person(doctor1)
ward1.add_person(doctor2)
ward1.describe()

# test c
print(f"\nNumber of doctors: {ward1.count_doctor()}")

# test d
print("After sorting age of ward 1 people:")
ward1.sort_age()
ward1.describe()

# test e
print(f"\nAverage year of birth (teachers): {ward1.compute_average()}")
