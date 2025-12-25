class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.id = emp_id
    
    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}"

class Manager:
    def __init__(self, name, emp_id, department):
        Employee.__init__(self, name, emp_id)  
        self.department = department
    
    def manage_project(self):
        return f"{self.name} управляет проектом"
    
    def get_info(self):
        return f"{Employee.get_info(self)}, Отдел: {self.department}"

class Technician:
    def __init__(self, name, emp_id, specialization):
        Employee.__init__(self, name, emp_id)  
        self.specialization = specialization
    
    def perform_maintenance(self):
        return f"{self.name} выполняет техобслуживание ({self.specialization})"
    
    def get_info(self):
        return f"{Employee.get_info(self)}, Специализация: {self.specialization}"

class TechManager(Manager, Technician):
    def __init__(self, name, emp_id, department, specialization):
        self.name = name
        self.id = emp_id
        self.department = department
        self.specialization = specialization
        self.team = []
    
    def add_employee(self, employee):
        self.team.append(employee)
        return f"Добавлен: {employee.name}"
    
    def get_team_info(self):
        return [emp.get_info() for emp in self.team]
    
    def get_info(self):
        return f"Сотрудник: {self.name}, ID: {self.id}, Отдел: {self.department}, Специализация: {self.specialization}"
    
    def manage_project(self):
        return Manager.manage_project(self)
    
    def perform_maintenance(self):
        return f"{self.name} выполняет техобслуживание ({self.specialization})"

# Демонстрация
if __name__ == "__main__":
    # Базовый сотрудник
    emp1 = Employee("Иван Петров", "E001")
    print("1.", emp1.get_info())
    
    # Менеджер
    manager = Manager("Анна Сидорова", "M001", "Разработка")
    print("2.", manager.get_info())
    print("3.", manager.manage_project())
    
    # Техник
    tech = Technician("Алексей Иванов", "T001", "Сети")
    print("4.", tech.get_info())
    print("5.", tech.perform_maintenance())
    
    # TechManager
    tech_manager = TechManager("Алексей Брусилов", "TM001", "ИТ", "Инфраструктура")
    print("6.", tech_manager.get_info())
    
    # Полиморфизм
    employees = [emp1, manager, tech, tech_manager]
    print("\nИнформация о всех сотрудниках:")
    for i, emp in enumerate(employees, 1):
        print(f"{i}. {emp.get_info()}")
    
    # Работа с командой
    tech_manager.add_employee(emp1)
    tech_manager.add_employee(tech)
    
    print("\nКоманда TechManager:")
    for info in tech_manager.get_team_info():
        print(f"- {info}")
    
    # Вызов методов
    print(f"\n{tech_manager.manage_project()}")
    print(tech_manager.perform_maintenance())
