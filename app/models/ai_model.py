from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class AIModel:
    def __init__(self):
        self.model_name = "mistralai/Codestral-7B-Instruct-v0.1"  # Example model
        self.tokenizer = AutoTokenizer.from_pretrained(self.model_name)
        self.model = AutoModelForCausalLM.from_pretrained(self.model_name)

    def generate_response(self, user_input):
        inputs = self.tokenizer(user_input, return_tensors="pt")
        outputs = self.model.generate(**inputs)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response
