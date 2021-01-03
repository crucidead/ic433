from rpi_rf import RFDevice


class Reciever:
    def __init__(self, pin: int):
        self.pin = pin
        self.device = RFDevice(pin)

        self.device.enable_rx()
        print(f"Initialize reciever on pin {self.pin}")

    def __del__(self):
        device.cleanup()

    def set_session_file(self, filename: str):
        pass

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
                timestamp = device.rx_code_timestamp
                print(f"[CODE]: {device.rx_code} [LENGHT]: {device.rx_pulselength} [PROTOCOL]: {device.rx_proto}")

