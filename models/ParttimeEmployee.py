from models.Employee import Employee


class PartTimeEmployee(Employee):
    PHA_CHE_HOURLY_WAGE = 25000
    PHUC_VU_HOURLY_WAGE = 24000
    THU_NGAN_HOURLY_WAGE= 23000

    def __init__(self, id=None, name=None, date_of_birth=None, phone_number=None, position=None, start_working_date=None,shifts_week=None):
        super().__init__(id, name, date_of_birth, phone_number, position, start_working_date,"Part-time")
        self.shifts_week=shifts_week
    def calculate_salary_week(self):
        if self.position == "Pha chế":
            hourly_wage = self.PHA_CHE_HOURLY_WAGE
        elif self.position == "Thu ngân":
            hourly_wage = self.THU_NGAN_HOURLY_WAGE
        else:
            hourly_wage = self.PHUC_VU_HOURLY_WAGE
        return self.shifts_week*4*hourly_wage

    def calculate_salary(self):
        return self.calculate_salary_week() *4

    '''def to_dict(self):
        data = super().to_dict()
        data["shifts_week"] = self.shifts_week
        return data
    '''

    def __str__(self):
        return super().__str__() + f" Type: {self.employee_type} | Salary: {self.calculate_salary():,.0f} VND"