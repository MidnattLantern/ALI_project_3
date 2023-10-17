class MyObject:
    def __init__(self, name):
        self.name = name

    def update_name(self, new_name):
        self.name = new_name

# Create an instance of the class
my_instance = MyObject("John")

# Print the initial name
print(f"Initial Name: {my_instance.name}")

# Update the name using the method
my_instance.update_name("Jane")

# Print the updated name
print(f"Updated Name: {my_instance.name}")
