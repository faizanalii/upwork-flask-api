# Flask CRUD Application
This application is a simple Flask API server that performs Create, Read, Update and Delete (CRUD) operations. It manages a list of prompts.

## Installation
To install the necessary libraries, run this command in your terminal/command line:

`pip install -r requirements.txt`

## Environment Variables
- Sensitive data like the OpenAI key is stored in environment variables. We use the python-dotenv library to manage these.
- Create a .env file in the root directory of your project. Add your OpenAI key like so: `CHATGPT_KEY = YourChatGPTKey`

## Running the App
You can start the app by running:

`python main.py`

## Endpoints
The server has the following endpoints:

- POST /create_prompt: Accepts a JSON body with a prompt field and appends it to the list of prompts.
- GET /get_prompt/<int:prompt_index>: Returns the prompt at the specified index and the ChatGPT response.
- PUT /update_prompt/<int:prompt_index>: Accepts a JSON body with a prompt field and replaces the prompt at the specified index.
- DELETE /delete_prompt/<int:prompt_index>: Deletes the prompt at the specified index.
