''' docstring '''
class MyClass:
    ''' docstring '''
    def __init__(self):
        # Initialize a dictionary attribute
        self.my_dict = {'key1': 'value1', 'key2': 'value2'}

    def update_dict(self, new_data):
        ''' docstring '''
        # Method to update the dictionary
        self.my_dict.update(new_data)

    def print_dict(self):
        ''' docstring '''
        # Method to print the dictionary
        print(self.my_dict)

# Create an instance of the class
my_instance = MyClass()

# Print the initial dictionary
my_instance.print_dict()

# Update the dictionary
my_instance.update_dict({'key3': 'value3', 'key4': 'value4'})

# Print the updated dictionary
my_instance.print_dict()
