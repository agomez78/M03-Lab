
# This program allows the user to input information about their vehicle, store the information, and print it 

# Define a superclass called Vehicle
class Vehicle:
    def __init__(self):
        self.vehicle_type = ""

    # Method to set the vehicle type
    def set_vehicle_type(self, vehicle_type):
        self.vehicle_type = vehicle_type

# Define a subclass called Automobile that inherits from Vehicle
class Automobile(Vehicle):
    def __init__(self):
        super().__init__()  # Call the superclass constructor to initialize the vehicle_type attribute
        # Initialize attributes specific to an automobile
        self.year = ""
        self.make = ""
        self.model = ""
        self.doors = ""
        self.roof = ""

    # Method to set attributes for the automobile
    def set_attributes(self, year, make, model, doors, roof):
        self.year = year
        self.make = make
        self.model = model
        self.doors = doors
        self.roof = roof

    # Method to display car information in a readable format
    def display_info(self):
        print("Vehicle type:", self.vehicle_type)
        print("Year:", self.year)
        print("Make:", self.make)
        print("Model:", self.model)
        print("Number of doors:", self.doors)
        print("Type of roof:", self.roof)

# Main function for user interaction
def main():
    # Create an instance of the Automobile class
    car = Automobile()

    # Prompt the user to enter the vehicle type
    vehicle_type = input("Enter the vehicle type: ")
    car.set_vehicle_type(vehicle_type)

    # Prompt the user to enter details about the car
    year = input("Enter the year: ")
    make = input("Enter the make: ")
    model = input("Enter the model: ")
    doors = input("Enter the number of doors (2 or 4): ")
    roof = input("Enter the type of roof (solid or sun roof): ")

    # Set the car's attributes with user input
    car.set_attributes(year, make, model, doors, roof)

    # Display the car's information
    print("\nCar Information:")
    car.display_info()

# Execute the main function if the script is run directly
if __name__ == "__main__":
    main()
