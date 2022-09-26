from car import Car


class Maruti(Car):
    def steering(self):
        print("Steering is manual steering")

    def braking(self):
        print("Braking is with hydraulic brakes")


# in java : the following lines should be a part of the main method :
m1 = Maruti(1001)
m1.open_tank()
m1.steering()
m1.braking()
# whenever we create an instance of sub class and the sub class doesnt contain a constructor then
# the constructor of the super class is executed and for that we need to provide the parameters
# accordingly
# here Maruti is a subclass but it doesnt have constructor
# thus constructor of Car class is executed , for that we provide the arguments which will get
# passed to the constructor of the Car class
