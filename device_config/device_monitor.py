from typing import List
from device_config.device import Device
import threading as th
from time import sleep

class Singleton(type):
    '''Singleton metaclass that protects against creating multiple different objects of DeviceMonitor.
    DeviceMonitor is a class that is responsible for communication, so we don't need multiple instations'''
    _instances = {}
    def __call__(cls):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__()
        return cls._instances[cls]

class DeviceMonitor(metaclass=Singleton):
    def __init__(self) -> None:
        '''
        args: None
        return: None
        '''
        self._devices = []
        self.thread = th.Thread(target=self.status)
        # thread.daemon provide that every thread using while loop will be killed after main thread will end.
        self.thread.daemon = True
        self._status = None
        self.lock = th.Lock()
        self.stop_thread = False

    @property
    def devices(self):
        '''
        args: None
        return:  List[Devices]
        '''
        return self._devices
    
    @devices.setter
    def devices(self, val):
        '''
        args: val -> List[Devices]
        return: None
        '''
        if isinstance(val, List):
            if all(isinstance(devices, Device) for devices in val):
                self._devices = val
            else:
                raise TypeError(f"List of devices should contain devices")
        else:
            raise TypeError(f"Invalid type of Device, received {type(val)} instead of List")

    def addDevice(self, val):
        '''
        method responsible for adding device to monitor
        args: val -> Device
        return: None
        '''
        if isinstance(val, Device):
            self._devices.append(val)
        else:
            raise TypeError(f"Invalid type of Device, received {type(val)} instead of Device")

    def start(self):
        '''
        args: None
        return: None
        '''
        self.thread.start()

    def stop(self):
        '''
        args: None
        return: None
        '''        
        self.stop_thread = True
        self.thread.join()

    def getStatus(self):
        '''
        args: None
        return: dict {device_id: measurements}
        '''
        with self.lock:
            return self.status

    def status(self):
        '''
        method that run in another thread and update status every second
        args: None
        return: None
        '''
        while not self.stop_thread:
            dict = {}
            for device in self._devices:
                dict[device.id] = device.get_results()
            with self.lock:
                self.status = dict
            sleep(1)

