class TV:
    def turn_on(self):
        print("TV turned on.")

    def turn_off(self):
        print("TV turned off.")

class Lights:
    def turn_on(self):
        print("Lights turned on.")

    def turn_off(self):
        print("Lights turned off.")

class Heating:
    def turn_on(self):
        print("Heating turned on.")

    def turn_off(self):
        print("Heating turned off.")

class HomeFacade:
    def __init__(self):
        self.tv = TV()
        self.lights = Lights()
        self.heating = Heating()

    def come_home(self):
        self.tv.turn_on()
        self.lights.turn_on()
        self.heating.turn_on()

    def go_out(self):
        self.tv.turn_off()
        self.lights.turn_off()
        self.heating.turn_off()


home = HomeFacade()
home.come_home()
# Output:
# TV +
# Lights +
# Heating +

home.go_out()
# Output:
# TV -
# Lights -
# Heating -
