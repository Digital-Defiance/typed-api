import mimetypes
import json
import json
import gzip
from io import BytesIO

from typedAPI.http.response.schema import HttpContentType




http_status_codes = {
    100: "Continue",
    101: "Switching Protocols",
    102: "Processing",
    103: "Early Hints",
    200: "OK",
    201: "Created",
    202: "Accepted",
    203: "Non-Authoritative Information",
    204: "No Content",
    205: "Reset Content",
    206: "Partial Content",
    207: "Multi-Status",
    208: "Already Reported",
    226: "IM Used",
    300: "Multiple Choices",
    301: "Moved Permanently",
    302: "Found",
    303: "See Other",
    304: "Not Modified",
    305: "Use Proxy",
    307: "Temporary Redirect",
    308: "Permanent Redirect",
    400: "Bad Request",
    401: "Unauthorized",
    402: "Payment Required",
    403: "Forbidden",
    404: "Not Found",
    405: "Method Not Allowed",
    406: "Not Acceptable",
    407: "Proxy Authentication Required",
    408: "Request Timeout",
    409: "Conflict",
    410: "Gone",
    411: "Length Required",
    412: "Precondition Failed",
    413: "Payload Too Large",
    414: "URI Too Long",
    415: "Unsupported Media Type",
    416: "Range Not Satisfiable",
    417: "Expectation Failed",
    418: "I'm a teapot",
    421: "Misdirected Request",
    422: "Unprocessable Entity",
    423: "Locked",
    424: "Failed Dependency",
    425: "Too Early",
    426: "Upgrade Required",
    428: "Precondition Required",
    429: "Too Many Requests",
    431: "Request Header Fields Too Large",
    451: "Unavailable For Legal Reasons",
    500: "Internal Server Error",
    501: "Not Implemented",
    502: "Bad Gateway",
    503: "Service Unavailable",
    504: "Gateway Timeout",
    505: "HTTP Version Not Supported",
    506: "Variant Also Negotiates",
    507: "Insufficient Storage",
    508: "Loop Detected",
    510: "Not Extended",
    511: "Network Authentication Required"
}



def guess_content_type_from_body(body) -> HttpContentType:

    if isinstance(body, dict) or isinstance(body, list):
        return "application/json"


    if isinstance(body, str):

        if body.startswith("<") and body.endswith(">"):
            return "text/html"

        if body.startswith("<?xml"):
            return "application/xml"

        if body.startswith("{") and body.endswith("}") or body.startswith("[") and body.endswith("]"):
            try:
                json.loads(body)
                return "application/json"
            except json.JSONDecodeError:
                pass

        return "text/plain"

    if isinstance(body, bytes):
        try:
            decoded_body = body.decode("utf-8")
            return guess_content_type_from_body(decoded_body)
        except UnicodeDecodeError:
            pass

        mime_type, encoding = mimetypes.guess_type("", strict=False)

        if mime_type:
            return mime_type # type: ignore

        return "application/octet-stream"

    return "text/plain"



def cast_from_content_type(body, content_type: HttpContentType) -> bytes:

    if content_type in {'application/json', 'application/javascript', 'application/xml', 'application/xhtml+xml'}:
        body_str = json.dumps(body) if isinstance(body, (dict, list)) else str(body)
        return body_str.encode('utf-8')
    
    
    if content_type == 'application/octet-stream':
        if isinstance(body, bytes):
            return body
        return str(body).encode('utf-8')


    if content_type == 'application/zip' or content_type == 'application/gzip':
        compressed_data = BytesIO()
        with gzip.GzipFile(fileobj=compressed_data, mode='wb') as gz_file:
            if isinstance(body, bytes):
                gz_file.write(body)
            else:
                gz_file.write(str(body).encode('utf-8'))
        return compressed_data.getvalue()

    return str(body).encode('utf-8')







