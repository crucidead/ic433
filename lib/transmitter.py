from rpi_rf import RFDevice


class Transmitter:
     def __init__(self, pin: int, 
                code: int, 
                plength: int,
                protocol: int,
                length: int = 24,
                repeat: int = 1):
        self.pin = pin
        self.code = code
        self.plength = plength  
        self.protocol = protocol
        self.length = length,

        self.device = RFDevice(pin)
        self.device.enable_tx()
        self.device.tx_repeat = repeat
        print(f"Initialize transmitter on pin {self.pin}")

    def __del__(self):
        device.cleanup()

    def start():
        try:
            self.device.tx_code(self.code, self.protocol, self.plength, self.length)
        except KeyboardInterrupt:
            print("Stopping...")
