class Car:

    def __init__(self, carBrand, speedLimit):
        self.carBrand = carBrand
        self.speedLimit = speedLimit
        self.currentSpeed = 0
        self.isStarted = False

    def dashboard(self):
        print(f"\n--> You are in {self.carBrand} <--")
        print(f"--> Speed limit = {self.speedLimit} km/h <--")
        print(f"--> Current speed = {self.currentSpeed} km/h <--")

    def start(self):
        if self.isStarted:
            print(f"{self.carBrand} is already started.")
        else:
            self.isStarted = True
            print(f"{self.carBrand} is started!")

        self.dashboard()

    def showSpeed(self):
        print(f"Current speed: {self.currentSpeed} km/h")

    def speedUp(self):
        if not self.isStarted:
            print(f"Start {self.carBrand} first!")
            return

        # Increase speed by 10 km/h
        self.currentSpeed += 10

        # Do not allow the speed to cross the limit
        if self.currentSpeed > self.speedLimit:
            self.currentSpeed -= 10
            print("You are already at maximum speed.")
        else:
            print("Speed increased by 10 km/h.")

        self.dashboard()

    def speedDown(self):
        if not self.isStarted:
            print(f"Start {self.carBrand} first!")
            return

        # Decrease speed by 10 km/h
        self.currentSpeed -= 10

        # Do not allow the speed to become negative
        if self.currentSpeed < 0:
            self.currentSpeed += 10
            print("You are already at minimum speed.")
        else:
            print("Speed decreased by 10 km/h.")

        self.dashboard()

    def stop(self):
        if not self.isStarted:
            print(f"{self.carBrand} is already stopped.")
        else:
            self.currentSpeed = 0
            self.isStarted = False
            print(f"{self.carBrand} is stopped!")

        self.dashboard()


# Creating a new car object
car = Car("Hyundai", 100)

while True:
    print("\n---------------")
    print("1. Start")
    print("2. Show Speed")
    print("3. Speed Up by +10")
    print("4. Speed Down by -10")
    print("5. Stop")
    print("6. Exit")
    print("---------------")

    choice = int(input("Choose an option: "))

    if choice == 1:
        car.start()

    elif choice == 2:
        car.showSpeed()

    elif choice == 3:
        car.speedUp()

    elif choice == 4:
        car.speedDown()

    elif choice == 5:
        car.stop()

    elif choice == 6:
        print("Exiting the program.")
        break
    else:
        print("Invalid choice. Please try again.")





