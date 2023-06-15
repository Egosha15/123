'''z=100
n="Lena"

print(f"У {n} зарплата в месяц {z}")
print(f"Таким образом в год он получает {z*10}")'''

'''e = {'n':'Lena',
    'z':100}
print(f"У {e['n']} зарплата в месяц {e.get('z')}")'''

'''#реализация списком, если сотрудников много
employee_list = [
    {'name' : 'Danil',
    'salary': 200000}, 

    {'name': 'Oleg',
    'salary': 150000,},

    {'name': 'Ivan',
    'salary': 180000,}
    ]

print(employee_list[0]["name"])

for employee in employee_list:
    print(f'У {employee["name"]} зарплата в месяц: {employee["salary"]} ')
#добавление сотрудника
new_employee = {'name' : 'Kirill',
    'salary': 12000}, 
employee_list.append(new_employee)
#уволить сотрудника
print(employee_list)
for employee in employee_list:
    if employee['name']=='Ivan':
        employee_list.remove(employee)
        break
print(employee_list)'''

#реализация в виде класса
class Employee:
    def __init__(self, name, salary, vacantion, good):
        self.name = name
        self.salary = salary
        self.on_vacantion = vacantion
        self.is_good_employee = good

    def get_info(self):
        return f'У {self.name} зарплата в месяц = {self.salary} его доложность {self.on_vacantion}'
    def uvolnenie(self):
        return f'{self.name} уволен'
    
baza = [Employee('Danil', 200000, 'uborshik', True), Employee('Oleg', 250000, 'menedzer', True), Employee('Olga', 200000, 'stroitel', False)]

for i in baza:
    print(i.get_info())
    if not i.is_good_employee:
        print(i.uvolnenie())
