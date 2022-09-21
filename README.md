# flask gpt3 chatbot
A general purpose chatbot using GPT3 implemented on flask.

<img src="demo/chatbot.gif" />

# setup

- Create a virtual environment
```
python -m venv venv
```
- Switch to the virtual environment
```
venv\Scripts\activate
```
- Install the dependencies
```
pip install -r requirements.txt
```
- Add the openai key in the test.py file
```
openai.api_key = "" # provide your openai key here
```
- Run the server
```
python app.py
```
- Load the url (http://localhost:5000/) on your browser
