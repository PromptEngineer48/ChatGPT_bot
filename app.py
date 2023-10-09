import openai

openai.api_key = "Your OpenAI API Key Here"

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model = "gpt-4-0613",
        messages = [{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == "__main__":
    while True:
        humna_input = input("Human: ")
        if humna_input.lower() in ["quit", "exit", "bye"]:
            break
        response = chat_with_gpt(humna_input)
        print("Chatbot: ", response)
