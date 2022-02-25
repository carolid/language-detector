## AnyLanguage Detector

AnyLanguage Detector is a simple and fun Command Line Interface app. Simple clone this repo, and run 
`python3 language-detector.py` to run the language detector microservice, then `python3 language-detector-app.py` to
begin the application as an interactive console.

### If you just want to run the language detector microservice:
- Clone this repo
- `cd` to the project directory
- Run `python3 language-detector.py`, and send a POST request to `http://localhost:3000`, or change the port in the 
  detector code.
  
The format of the POST request (`Content-type` = `application/json`):
```json
    {"text": "word"}
```

The `"word"` can be any String containing a valid word or sentence in (almost) any language. The response contains just 
the body of the response - `b"Response"`, if you're using Python, you can use `response.text` to get a pretty string 
containing the language. In Express, I believe a comparable method would be `res.body`