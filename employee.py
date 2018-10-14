class Employee:
    """ A sample Employee class"""

    raise_ratio = 1.05

    def __init__(self, first, last, pay):
        self._first = first
        self._last = last
        self._pay = pay

    @property
    def email(self):
        if self._last != "":
            return "{}.{}@company.com".format(self._first.lower(), self._last.lower())
        else:
            return "{}@company.com".format(self._first.lower())

    @property
    def fullname(self):
        if self._last != "":
            return "{} {}".format(self._first, self._last)
        else:
            return "{}".format(self._first)

    @property
    def salary(self):
        return self._pay

    def apply_raise(self):
        self._pay = int(self._pay * Employee.raise_ratio)
