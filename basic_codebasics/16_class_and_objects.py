class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def display(self):
        print(f"id: {self.id}, name: {self.name}\n")

emp = Employee(1, "coder")
emp.display()

del emp.id

try:
    print(emp.id)

except Exception as e:
    print('id is not found')

del emp

try:
    print(emp.name)
    emp.display()

except Exception as e:
    print('the object emp is not found')


