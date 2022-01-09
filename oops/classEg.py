class ExpenseTracker:
    # class Attribute
    version = 0.1

    def __init__(self, date, description, transaction_type, amount,bank="Indian Bank"):
        # Instance/Object Attributes
        # Public attributes
        self.date = date
        self.description = description
        self.transaction_type = transaction_type
        self.amount = amount
        # Private attributes
        self.__bank = bank

    # Instance Method
    # Public Methods
    def get_amount(self):
        return self.amount

    def check_amount(self, value):
        if self.amount > value:
            return True
        return False

    # Private Method
    def __get_banl(self):
        return self.__bank

    # Static Method
    @staticmethod
    def convert_amount(value):
        return float(value)

    # Class Method/Factory Method
    @classmethod
    def get_attr_from_string(cls, entry: str):
        date, description, transaction_type, amount = entry.split(" ")
        return ExpenseTracker(date, description.capitalize(), transaction_type.capitalize(), cls.convert_amount(amount))


obj = ExpenseTracker('1jan', 'price', 'credited', 3000)
print(obj.amount)
#{'date': '1jan', 'description': 'price', 'transaction_type': 'credited', 'amount': 3000}
print(obj.__dict__)
# 1jan
print(getattr(obj, "date"))
# True
print(hasattr(obj, "date"))
# to delete attr
delattr(obj, "date")

ExpenseTracker.version = 455
print(obj.version)
print(ExpenseTracker.version)
# #############

print(obj.convert_amount(25))
print(ExpenseTracker.convert_amount(25))
# #############
classObj=ExpenseTracker.get_attr_from_string("2feb some_descp cash 5000")
print(classObj.__dict__)