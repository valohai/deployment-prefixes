This directory contains a simple Flask app and a generic WSGI middleware
that rewrites the internal request path based on the prefix environment variable or headers.

Feel free to copy-paste the middleware module into your WSGI app.

Example usage
=============

* Run the app: `python app.py`
* Make a request: `curl "http://127.0.0.1:8000/predict?name=Foo"`
* Make a request passing in a prefix in a header (as done by Valohai's deployment machinery):  
  `curl -H "X-VH-Prefix: /example/" "http://127.0.0.1:8000/example/predict?name=Foo"`

