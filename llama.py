from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

# Load Llama model and tokenizer
model_name = "facebook/llama-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(model_name)

# Generate response from user input
def generate_response(user_input):
    input_ids = tokenizer.encode(user_input, return_tensors="pt")
    output = model.generate(input_ids, max_length=100, pad_token_id=tokenizer.eos_token_id)
    response = tokenizer.decode(output[:, input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

# Chatbot function
def chatbot():
    while True:
        user_input = input("User: ")

        if user_input.lower() == "bye":
            print("Chatbot: Goodbye!")
            break

        response = generate_response(user_input)
        print("Chatbot:", response)

# Run the chatbot
print("Chatbot: Hello! I'm the Llama Chatbot. How can I assist you?")
chatbot()
