from device_config.device import Device
import pytest

good_config = {
    'ID' : '1',
    'measurements': ['voltage', 'current'],
    'file_path': 'simulation_assets/resources/device1.json'
}
wrong_id_config = {
    'ID' : 2,
    'measurements': ['voltage', 'current'],
    'file_path': 'simulation_assets/resources/device2.json'
}
wrong_measurements_config = {
    'ID' : '2',
    'measurements': ['voltage', True],
    'file_path': 'simulation_assets/resources/device2.json'
}

class TestDevice:
    def test_initialization(self):
        with pytest.raises(Exception):
            bad = Device(wrong_id_config)
        with pytest.raises(Exception):
            bad = Device(wrong_measurements_config)

    def test_setters_and_getters(self):
        test_device = Device(good_config)
        assert test_device.measurements == good_config['measurements']
        with pytest.raises(Exception):
            test_device.id = 1
        with pytest.raises(Exception):
            test_device.measurements = 1
        with pytest.raises(Exception):
            test_device.measurements = [1, 2 ,3]
        test_device.measurements = ['measurement1', 'measurement2']
        assert len(test_device.measurements) == 2