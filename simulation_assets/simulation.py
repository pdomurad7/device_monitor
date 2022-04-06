from device_config.device_monitor import DeviceMonitor
from device_config.device import Device
import json
from time import sleep

class FakeDevice(Device):
    def __init__(self, config) -> None:
        super().__init__(config)
        self.file_path = config['file_path']
    
    def get_results(self):
        with open(self.file_path) as f:
            return json.load(f)

config1 = {
    'ID' : '1',
    'measurements': ['voltage', 'current'],
    'file_path': 'simulation_assets/resources/device1.json'
}
config2 = {
    'ID' : '2',
    'measurements': ['voltage', 'current'],
    'file_path': 'simulation_assets/resources/device2.json'
}

def simulation():
    device_api = DeviceMonitor()
    device_api.start()
    
    fake_device1 = FakeDevice(config1)
    fake_device2 = FakeDevice(config2)

    device_api.addDevice(fake_device1)
    device_api.addDevice(fake_device2)
    

    try:
        while True:
            print("Current status: ", device_api.getStatus())
            sleep(1)
    except KeyboardInterrupt:
        device_api.stop()
        print("simulation is finished")
        
    if device_api.thread.is_alive():
        device_api.stop()
