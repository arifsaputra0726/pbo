import json

class Employee:
    def __init__(self, emp_id, name, base_salary, is_permanent):
        self.emp_id = emp_id
        self.name = name
        self.base_salary = base_salary
        self.is_permanent = is_permanent

    def calculate_total_salary(self):
        return self.base_salary

    def display_info(self):
        status = "Permanent" if self.is_permanent else "Contract"
        print(f"ID: {self.emp_id} | Name: {self.name} | Status: {status} | Salary: Rp {self.calculate_total_salary():,.2f}")

class PermanentEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, is_permanent, bonus_code):
        super().__init__(emp_id, name, base_salary, is_permanent)
        self.bonus_code = bonus_code

    def calculate_total_salary(self):
        bonus = 0
        if self.bonus_code == "PERF2026":
            bonus = 1000000.0
        elif self.bonus_code == "SENIOR10":
            bonus = self.base_salary * 0.10
        elif self.bonus_code == "LEAD2026":
            bonus = 2500000.0
            
        return self.base_salary + bonus

class ContractEmployee(Employee):
    def __init__(self, emp_id, name, base_salary, is_permanent):
        super().__init__(emp_id, name, base_salary, is_permanent)

    def calculate_total_salary(self):
        tunjangan_makan = 300000.0
        return self.base_salary + tunjangan_makan

class SensorLog:
    def __init__(self, sensor_id, location, temperature, operator_id):
        self.sensor_id = sensor_id
        self.location = location
        self.temperature = temperature
        self.operator_id = operator_id if operator_id is not None else "Unknown"

    def analyze_status(self):
        pass 

    def display_log(self):
        print(f"Sensor: {self.sensor_id} | Loc: {self.location} | Temp: {self.temperature}°C | Status: {self.analyze_status()} | Operator: {self.operator_id}")

class NormalSensor(SensorLog):
    def analyze_status(self):
        return "NORMAL (Aman)"

class AlertSensor(SensorLog):
    def __init__(self, sensor_id, location, temperature, status, operator_id):
        super().__init__(sensor_id, location, temperature, operator_id)
        self.status = status

    def analyze_status(self):
        if self.status == "DANGER":
            return "DANGER (Evakuasi/Tindakan Segera!)"
        return "WARNING (Perlu Pengecekan)"

def main():
    print("=== DATA KARYAWAN (OOP) ===")
    try:
        with open('employee.json', 'r') as file:
            emp_data = json.load(file)
            
            for emp in emp_data['employees']:
                if emp['is_permanent']:
                    obj = PermanentEmployee(emp['emp_id'], emp['name'], emp['base_salary'], emp['is_permanent'], emp['bonus_code'])
                else:
                    obj = ContractEmployee(emp['emp_id'], emp['name'], emp['base_salary'], emp['is_permanent'])
                
                obj.display_info()
    except FileNotFoundError:
        print("File employee.json tidak ditemukan.")

    print("\n=== LOG SENSOR (OOP) ===")
    
    try:
        with open('sensor_logs.json', 'r') as file:
            sensor_data = json.load(file)
            
            for log in sensor_data['readings']:
                if log['status'] == "NORMAL":
                    obj = NormalSensor(log['sensor_id'], log['location'], log['temperature'], log['operator_id'])
                else:
                    obj = AlertSensor(log['sensor_id'], log['location'], log['temperature'], log['status'], log['operator_id'])
                
                obj.display_log()
    except FileNotFoundError:
        print("File sensor_logs.json tidak ditemukan.")

if __name__ == "__main__":
    main()