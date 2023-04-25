
import pathlib
import typing

import pydantic

class ResourcePath(pathlib.PosixPath):

    def dict(self) -> typing.Dict[str, str]:
        
        as_dict = {}
        
        for part in self.parts:
            stripped_part = part.strip()
            if stripped_part.startswith("{") and stripped_part.endswith("}"):
                spec = stripped_part[1:-1]
                name, type = spec.split(":")
                as_dict[name] = type
        
        return as_dict

    
class ResourcePathValues(pydantic.BaseModel):
    parameters: typing.Any
    queries: typing.Any
