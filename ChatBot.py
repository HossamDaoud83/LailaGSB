import openai
import gradio as gr
import docx2txt


# OpenAI API Key
openai.api_key = "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"

# Read the info file
info = docx2txt.process("info.docx")

# Define the messages
messages = [
    {"role": "system", "content": info},
]


# Define the chatbot function
def chatbot(input):
    if input:
        messages.append({"role": "user", "content": input})
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
        reply = chat.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        return reply


inputs = gr.inputs.Textbox(lines=7, label="Chat with Laila (AI) GSB Virtual Assistant")
outputs = gr.outputs.Textbox(label="Reply")

gr.Interface(fn=chatbot, inputs=inputs, outputs=outputs, title="Laila (AI) GSB Virtual Assistant",
             description="Ask anything you want",
             theme="compact").launch(share=True)
