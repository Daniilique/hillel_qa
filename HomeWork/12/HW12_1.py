from abc import ABC, abstractmethod

class AbstractDevice(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

class ConcreteDevice(AbstractDevice):
    def turn_on(self):
        print("Device turned on.")

    def turn_off(self):
        print("Device turned off.")

# Examples
device = ConcreteDevice()
device.turn_on()
device.turn_off()
