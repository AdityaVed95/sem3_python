from car import Car


class Santro(Car):
    def steering(self):
        print("Steering is power steering")

    def braking(self):
        print("Braking is with gas brakes")


s1 = Santro(1002)
s1.open_tank()
s1.steering()
s1.braking()
