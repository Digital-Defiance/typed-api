# type: ignore

import pathlib
import pydantic
import typing


type_map = {
    'int': int,
    'float': float,
    'complex': complex,
    'bool': bool,
    'str': str,
    'bytes': bytes,
    'bytearray': bytearray,
    'list': list,
    'tuple': tuple,
    'set': set,
    'frozenset': frozenset,
    'dict': dict,
}


class Config:
    extra="allow"

class ResourcePathValue(pydantic.BaseModel):
    parameters: typing.Any
    queries: typing.Any

class ResourcePath(pathlib.PosixPath):

    parameters: pydantic.BaseModel
    queries: pydantic.BaseModel

    def __init__(self, *args, **kwargs):
        self.is_validated = False

        super().__init__()
        
        self._parameters = {}

        for key in self._parts:
            self._parse_key(key)
                
        self.create_models()


    def set_parameters(self, parameters):
        self._parameters = parameters

    def create_models(self):
        value = str(self)
        self.parameters = pydantic.create_model(f"parameters:{value}", **self._parameters, __config__=Config)
        self.queries = pydantic.create_model(f"queries:{value}", __config__=Config)


    def _parse_key(self, key: str):
        
        _key = key.strip()
        
        if not (_key.startswith("{") and _key.endswith("}")):
            return
        
        parameter_spec = _key[1:-1]

        if not ":" in parameter_spec:
            return


        _parameter_spec = parameter_spec.split(":")

        if not len(_parameter_spec) == 2:
            return

        parameter_name, parameter_type = _parameter_spec
        
        parameter_name = parameter_name.strip()
        parameter_type = parameter_type.strip()

        if parameter_type not in type_map:
            raise TypeError(parameter_type)

        self._parameters[parameter_name] = (type_map[parameter_type], ...)

    
    def __truediv__(self, key: str):
        
        if not isinstance(key, str):
            return NotImplemented

        try:
            child = self._make_child((key,))
        except TypeError:
            return NotImplemented

        self._parse_key(key)
        child.set_parameters(self._parameters)
        child.create_models()
        return child


    def validate(self, parameter_values, query_values):
        parameters = self.parameters(**parameter_values)
        queries = self.queries(**query_values)
        return ResourcePathValue(parameters=parameters, queries=queries)
