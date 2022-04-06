from cgi import test
from typing import List
import pytest

from device_config.device_monitor import DeviceMonitor
from device_config.device import Device

good_config = {
    'ID' : '1',
    'measurements': ['voltage', 'current'],
    'file_path': 'simulation_assets/resources/device1.json'
}

test_device = Device(good_config)

class TestMonitorDevice():
    def test_empty_api(self):
        test_api = DeviceMonitor()
        assert isinstance(test_api.devices, List)
        assert len(test_api.devices) == 0
        assert test_api.thread.daemon
        assert not test_api.thread.is_alive()

    
    def test_thread(self):
        test_api = DeviceMonitor()
        test_api.start()
        assert test_api.thread.is_alive()
        test_api.stop()
        assert not test_api.thread.is_alive()

    def test_setters_and_getters(self):
        test_api = DeviceMonitor()
        with pytest.raises(Exception):
            test_api.addDevice("string")
        with pytest.raises(Exception):
            test_api.devices=[1,2,3]            
        test_api.devices = [test_device]
        assert len(test_api.devices) == 1
        test_api.addDevice(test_device)
        assert len(test_api.devices) == 2
        assert isinstance(test_api.status, dict)


        
            

