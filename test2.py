# run.py
from test import DataClass

# Create an instance of DataClass
data_instance = DataClass()

my_list_data = []
print(my_list_data)

# Access the list from the instance
my_list_data = data_instance.get_data()

# Now my_list_data contains [1, 2, 3]
print(my_list_data)
