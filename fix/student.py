import datetime


class Student:
    def __init__(self, name, dob, branch, credit):
        self.name = name
        self.dob = dob
        self.branch = branch
        self.credit = credit

    def get_age(self):
        return (datetime.datetime.now() - self.dob).days // 365

    def get_credit(self):
        return self.credit


def is_eligible_for_degree(student):
    return student.get_credit() >= 20




