from device import Device
import threading as th


class DeviceMonitor:
    def __init__(self) -> None:
        self._devices = []
        self.thread = th.Thread(target=self.status)
        self.stop_thread = False
        self._status = None

    @property
    def devices(self):
        return self._devices
    
    @devices.setter
    def devices(self, val):
        if isinstance(val, Device):
            self._devices = val
        else:
            raise ValueError(f"Invalid type of Device, received {type(val)} instead of Device")

    def start(self):
        self.thread.start()

    def stop(self):
        self.stop_thread = True
        self.thread.join()

    def getStatus(self):
        pass

    def status(self):
        while True:
            dict = {}
            for device in self._devices:
                dict[device.id] = device.get_results()
            self.status = dict
            if self.stop_thread:
                break
