
# Introduction

If you are not interested in a comprehensive introduction follow this link to quickly get started with typedAPI.

## What is HTTP

HTTP is essentially a text-based protocol that enables communication between clients (e.g., web browsers) and servers. This communication is done through *standardized text messages* exchanged between the two parties. Here's an example of a simple HTTP request and response:

HTTP Request:

```
GET /example.txt HTTP/1.1
Host: www.example.com
```

HTTP Response:

```
HTTP/1.1 200 OK
Content-Type: text/plain

Hello, World!
```

In this example, the client sends a GET request for the "/example.txt" resource. The request consists of the request line and the "Host" header, which is required in HTTP/1.1 to identify the target server. No other headers are provided in this simple example.

The server responds with a status line (HTTP/1.1 200 OK) and a "Content-Type" header, which specifies that the response body contains plain text. After a blank line, the response body contains the text "Hello, World!".

HTTP was created by Tim Berners-Lee in 1989 while working at CERN, alongside the creation of HTML and the World Wide Web. The first documented version of HTTP was HTTP/0.9, which was a simple protocol designed to transfer hypertext documents over the internet. 

Over the years, HTTP has evolved through multiple versions, with HTTP/1.0 and HTTP/1.1 adding features such as additional request methods, response status codes, and headers to improve communication between clients and servers. The most recent version is HTTP/2, which was standardized in 2015, offering significant performance improvements and support for multiplexing and server push.

## HTTP Request

An HTTP request is a message sent by a client (typically a web browser) to a server, asking for a specific action to be performed on a particular resource. An HTTP request consists of three main parts: the request line, request headers, and an optional request body.

Here's a more comprehensive example of an HTTP request:

```
POST /api/data HTTP/1.1
Host: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
Content-Type: application/json
Content-Length: 81
Accept: application/json
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br
Connection: keep-alive
Cookie: session_id=12345; theme=dark

{
  "title": "Example Item",
  "description": "This is an example item.",
  "price": 9.99
}
```

In an HTTP request, the first line is known as the request line, which contains vital information such as the HTTP method, resource path, and protocol version. Following the request line, there are one or more header lines that provide additional context and metadata about the request. Headers can include information about the client, desired content types, and more. After the header lines, there is a blank line, followed by the optional request body. The request body is used to transmit data to the server when necessary, such as when submitting a form or updating a resource. The combination of the request line, header lines, and request body enables clients and servers to communicate effectively and exchange information over the web.

### Request line


```Python
import typedAPI
server = typedAPI.Server()
v1 = typedAPI.ResourcePath("/api/v1")

@server.append(protocol='http')
async def get(resource_path: v1 / "posts" / "{some_id:int}"):
    pass

```
