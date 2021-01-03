import time

from rpi_rf import RFDevice


class Receiver:
    def __init__(self, pin: int):
        self.pin = pin
        self.device = RFDevice(pin)

        self.device.enable_rx()
        print(f"Initialize receiver on pin {self.pin}")

    def start(self):
        print("Enter Ctrl-C to stop")
        try:
            self.__listen()
        except KeyboardInterrupt:
            print("Stopping...")

    def __listen(self):
        timestamp = None
        
        while True:
            if self.device.rx_code_timestamp != timestamp:
                timestamp = self.device.rx_code_timestamp
                print(f"[CODE]: {self.device.rx_code}\
                        [LENGTH]: {self.device.rx_pulselength} \
                        [PROTOCOL]: {self.device.rx_proto}")

            time.sleep(0.01)
