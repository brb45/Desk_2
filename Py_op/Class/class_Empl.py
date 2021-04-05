class Employee:
    def __init__(self, first_name, last_name, e_ID, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.user_id = e_ID
        # private attibute, start with 2 understore, __
        self.__salary = salary

    def show_employee(self):
        print("First Name is", self.first_name)
        print("Last Name is ", self.last_name)
        print("ID is ", self.user_id)
        print("Salary is ", self.emp_salary)
        

    @property
    def emp_salary(self):
        return self.__salary

    @emp_salary.setter
    def emp_salary(self, s):
        self.__salary = s

    def __str__(self):
        return self.last_name + ', ' +  self.first_name


def main():
    test_engineer = Employee("Jack", "Wallace", "747612", 10000)
    test_engineer.show_employee()
    print(test_engineer)

    test_engineer.emp_salary = 2000
    print(test_engineer.emp_salary)


if __name__ == "__main__":
    main()

# First Name is Jack
# Last Name is  Wallace
# ID is  747612
# Salary is  10000
# Wallace, Jack
# 2000
