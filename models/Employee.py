class Employee:
    def __init__(self, id=None, name=None, date_of_birth=None, phone_number=None, position=None, start_working_date=None,employee_type=None):
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.phone_number = phone_number
        self.position = position
        self.employee_type = employee_type
        self.start_working_date = start_working_date

    '''def to_dict(self):
        """Chuyển đổi đối tượng Employee thành dictionary để lưu vào JSON"""
        return {
            "id": self.id,
            "name": self.name,
            "date_of_birth": self.date_of_birth,
            "phone_number": self.phone_number,
            "position": self.position,
            "employee_type": self.employee_type,
            "start_working_date": self.start_working_date,
        }
    '''
    def __str__(self):
        return f" ID: {self.id} | Name: {self.name}| Phone: {self.phone_number} | Position: {self.position}, Start: {self.start_working_date}"