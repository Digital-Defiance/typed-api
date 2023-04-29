

import typing
import starlette.applications
import starlette.responses
import uvicorn

import typedAPI
import typedAPI.server.data

import typedAPI.main
import typedAPI.endpoint.service




class Server(starlette.applications.Starlette):


    def __init__(self, *args, **kwargs):
        super().__init__()

    def listen(self, *args, **kwargs):
        uvicorn.run(self, *args, **kwargs)

    def _handler_wrapper_definition(self):
        pass

    def _http_endpoint_register(self, raw_executor: typing.Callable) -> typing.Callable:
        executor, spec = typedAPI.endpoint.service.generate_full_executor(raw_executor)
        resource_path_string = str(spec.resource_path)
        self.add_route(resource_path_string, executor, methods=[spec.http_method])
        return executor


    def append(self, protocol='http'):
        if protocol == 'http':
            return self._http_endpoint_register

        raise NotImplementedError(f'Unknown protocol: {protocol}')

