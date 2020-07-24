This directory contains a simple FastAPI app with a middleware function
that rewrites the internal path based on the prefix environment variable or headers.

Feel free to copy-paste the middleware function into your app.

Example usage
=============

* Run the app: `uvicorn --debug --reload app:app`
* Make a request: `curl "http://127.0.0.1:8000/predict?name=Foo"`
* Make a request passing in a prefix in a header (as done by Valohai's deployment machinery):  
  `curl -H "X-VH-Prefix: /example/" "http://127.0.0.1:8000/example/predict?name=Foo"`

