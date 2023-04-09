
# type: ignore
from re import L
import pydantic

import typedAPI


class Config:
    extra="allow"



class CustomValidator:
    pass

class Headers:
    def __init__(self, headers):
        self.validation_of_customs = {}

        if headers == ...:
            self.validation_of_builtins = pydantic.create_model('Headers', __config__=Config,)
            return

        validation_of_builtins = {}

        for key, value in headers.items():

            if callable(value):
                self.validation_of_customs[key] = value
                continue

            validation_of_builtins[key] = (value, ...)

        self.validation_of_builtins = pydantic.create_model(
            'Headers',
            __config__=Config,
            **validation_of_builtins
        )
        

    def validate(self, headers):

        headers = {**headers}
        validated_customs = {}
        
        for key, validator in self.validation_of_customs.items():
            header = headers.pop(key)
            
            validation = validator(header)

            not_ok, data = typedAPI.response.normalise_response(validation)
            
            if not_ok:
                return False, data

            validated_customs[key] = data

        validated_builtins = self.validation_of_builtins(**headers).dict()

        return True, {
            **validated_customs,
            **validated_builtins
        }


        

        