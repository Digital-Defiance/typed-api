

class Headers(dict):
    def __init__(self, headers: dict[str, object]):
        
        
        for header_name, value in headers.items():
            header_name = header_name.lower()

            if value == ...:
                self[header_name] = guess_processor_from_header_name(header_name)

            if is_type(value):
                self[header_name] = generate_processor_from_type(value)

            if not isinstance(value, callable):
                self[header_name] = lambda : value
            
            self[header_name] = value

    

        

    
    


    
    

    