from rpi_rf import RFDevice


class Reciever:
    def __init__(self, pin: int):
        self.pin = pin
        self.device = RFDevice(pin)

        self.device.enable_rx()
        print(f"Initialize reciever on pin {self.pin}")

    def start(self):
        print("Enter Ctrl-C to stop")
        try:
            __listen()
        except KeyboardInterrupt:
            print("Stopping...")

    def __listen():
        timestamp = None
        
        while True:
            if self.device.rx_code_timestamp != timestamp:
                timestamp = self.device.rx_code_timestamp
                print(f"[CODE]: {device.rx_code} [LENGHT]: {self.device.rx_pulselength} [PROTOCOL]: {self.device.rx_proto}")

    def __del__(self):
        self.device.cleanup()

