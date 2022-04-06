from abc import abstractmethod
from tokenize import String
from typing import List

class Device:
    def __init__(self, config=None) -> None:
        '''
        args: config -> dict {device_id: str id, measurements: List[measurements]}
        return: None
        '''
        if isinstance(config, dict):
            if 'ID' in config:
                if isinstance(config['ID'], str):
                    self._id = config.get('ID')
                else:
                    raise TypeError("ID should by type string")
            else:
                raise ValueError("config file doesnt have ID")
            if 'measurements' in config:
                if all(isinstance(measurement, str) for measurement in config['measurements']):
                    self._measurements = config.get('measurements')
                else:
                    raise TypeError("measurements should by strings")
            else:
                raise ValueError("config file doesnt have measurements")
        else:
            raise TypeError(f"Invalid type of config, received {type(config)} instead of dictionary")

    @abstractmethod
    def get_results(self):
        '''
        abstract method that have to be override depending on the device
        method should use config file to determine how to get results
        '''
        pass

    @property
    def id(self):
        '''
        args: None
        return: str
        '''        
        return self._id
    
    @id.setter
    def id(self, val):
        '''
        args: val -> str
        return: None
        '''       
        if isinstance(val, str):
            self._id = val
        else:
            raise TypeError(f"Invalid type of ID, received {type(val)} instead of string")
    
    @property
    def measurements(self):
        '''
        args: None
        return: List
        '''       
        return self._measurements

    @measurements.setter
    def measurements(self, val):
        '''
        args: val -> List[str]
        return: None
        '''       
        if isinstance(val, List):
            if all(isinstance(measurement, str) for measurement in val):
                self._measurements = val
            else:
                raise TypeError("measurements should by strings")
        else:
            raise TypeError(f"Invalid type of measurements, received {type(val)} instead of list")
