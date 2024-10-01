# HTTP Methods

1. CONNECT[^c]
1. DELETE[^d] - intentionally no footnote below
1. GET [^g]
1. HEAD [^h]
1. OPTIONS[^o]
1. PATCH[^pa]
1. POST [^po]
1. PUT [^pu]
1. TRACE[^t]

credit[^cr] where it's due, Thank you Mozilla

[^t]: performs a message loop-back test along the path to the target resource
[^o]: requests permitted communication options for a given URL or server
[^g]: requests a representation of the specified resource
[^c]: requests a proxy server establish a HTTP tunnel to a destination server
[^cr]: https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
[^oops]: ooops, did I add a footnote that doesn't exist in the inline text?
[^pa]: applies partial modifications to a resource
[^po]: sends data to the server
[^pu]: creates a new resource or replaces a representation of the target resource with the request content
[^h]: requests the metadata of a resource in the form of headers that the server would have sent if GET was used instead
