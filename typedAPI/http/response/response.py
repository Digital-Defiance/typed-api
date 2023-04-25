
import typing

def isheaders(possible_headers):
    return isinstance(possible_headers, dict) or possible_headers == ...

def isstatus(possible_status):
    return isinstance(possible_status, int) or possible_status == ...


def normalise_response(possible_response):

    if isinstance(possible_response, int):
        return True, (possible_response, ..., ...)

    if not isinstance(possible_response, tuple):
        return False, None

    size = len(possible_response)

    if size == 1:
        possible_status = possible_response[0]

        if not isstatus(possible_status):
            return False, None

        return True, (possible_status, ..., ...)
    
    elif size == 2:
        possible_status, possible_headers = possible_response
        
        if not isstatus(possible_status):
            return False, None

        if not isheaders(possible_headers):
            return False, None

        possible_headers: dict

        return True, (possible_status, possible_headers, ...)

    elif size == 3:
        possible_status, possible_headers, possible_body = possible_response

        if not isstatus(possible_status):
            return False, None

        if not isheaders(possible_headers):
            return False, None
        
        possible_headers: dict
        
        if possible_body == ...:
            return False, None
        
        return True, (possible_status, possible_headers, possible_body)
    
    return False, None
        


