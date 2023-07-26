from flask import Flask, request
from flask_restful import Resource, Api
from typing import Dict, List
import os
from dotenv import load_dotenv
from chatgpt import get_query_response

load_dotenv()

CHATGPT_KEY: str = os.getenv("CHATGPT_KEY")

app = Flask(__name__)
api = Api(app)

prompts = []  # Database for storing prompts


class ChatGPTBotAPI(Resource):
    def __init__(self, api_key):
        self.api_key = api_key

    def get(self, prompt_index: int):
        if prompt_index < len(prompts):
            prompt: str = prompts[prompt_index]
            query_response: str = get_query_response(prompt, self.api_key)
            return {"prompt": prompt, "response": query_response}, 200
        else:
            return "No prompt found at given index", 404

    def post(self):
        new_prompt = request.get_json()
        prompts.append(new_prompt["prompt"])
        return {"prompt": new_prompt}, 201

    def put(self, prompt_index: int):
        updated_prompt = request.get_json()
        if prompt_index < len(prompts):
            prompts[prompt_index] = updated_prompt["prompt"]
            return {"prompt": updated_prompt}, 200
        else:
            return "No prompt found at given index", 404

    def delete(self, prompt_index: int):
        if prompt_index < len(prompts):
            deleted_prompt = prompts.pop(prompt_index)
            return {"prompt": deleted_prompt}, 200
        else:
            return "No prompt found at given index", 404


api.add_resource(
    ChatGPTBotAPI,
    "/create_prompt",
    "/get_prompt/<int:prompt_index>",
    "/update_prompt/<int:prompt_index>",
    "/delete_prompt/<int:prompt_index>",
    resource_class_kwargs={"api_key": CHATGPT_KEY},
)

if __name__ == "__main__":
    app.run(debug=True)
