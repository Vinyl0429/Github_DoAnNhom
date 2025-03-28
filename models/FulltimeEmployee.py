from models.Employee import Employee


class FullTimeEmployee(Employee):
    PHA_CHE_SALARY = 10000000 #10tr
    PHUC_VU_SALARY = 9000000 #9tr
    THU_NGAN_SALARY = 8000000 #8tr

    def __init__(self, id=None, name=None, date_of_birth=None, phone_number=None, position=None, start_working_date=None, day_absence=None):
        super().__init__(id, name, date_of_birth, phone_number, position,start_working_date, "Full-time")
        self.day_absence=day_absence
    def calculate_salary(self):
        base_salary = 0
        if self.position == "Pha chế":
            base_salary = self.PHA_CHE_SALARY
        elif self.position == "Phục vụ":
            base_salary = self.PHUC_VU_SALARY
        elif self.position == "Thu ngân":
            base_salary = self.THU_NGAN_SALARY

        return base_salary - (base_salary / 30) * (self.day_absence if self.day_absence else 0)

    '''def to_dict(self):
        data = super().to_dict()
        data["day_absence"] = self.day_absence
        return data
    '''

    def __str__(self):
        return super().__str__() + f" Type: {self.employee_type}| Days Absence: {self.day_absence} | Salary: {self.calculate_salary():,.0f} VND"
