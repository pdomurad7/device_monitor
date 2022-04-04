from abc import abstractmethod

class Device:
    def __init__(self, config=None) -> None:
        self._id = config.get('ID')
        self._measures = config.get('measures')

    @abstractmethod
    def get_results(self):
        pass
    

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self, val):
        if isinstance(val, str):
            self._id = val
        else:
            raise ValueError(f"Invalid type of ID, received {type(val)} instead of string")
    
    @property
    def measures(self):
        return self._measures

    @measures.setter
    def measures(self, val):
        if isinstance(val, dict):
            self._measures = val
        else:
            raise ValueError(f"Invalid type of measures, received {type(val)} instead of dictionary")
