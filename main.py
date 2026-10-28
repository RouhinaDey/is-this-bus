class VehicleQuiz:
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def check(self):
        answer = input(f"Is this a {self.vehicle}? (yes/no): ")

        if answer.lower() == "yes" and self.vehicle.lower() == "bus":
            print("Correct! It is a bus.")
        elif answer.lower() == "no" and self.vehicle.lower() != "bus":
            print("Correct! It is not a bus.")
        else:
            print("Wrong answer!")


# Create objects
bus = VehicleQuiz("bus")
car = VehicleQuiz("car")

bus.check()
car.check()