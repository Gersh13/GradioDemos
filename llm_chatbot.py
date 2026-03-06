from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai import Credentials
from langchain_ibm import WatsonxLLM
import gradio as gr

# Model Options
model_id = 'mistralai/mistral-small-3-1-24b-instruct-2503' # Specify the Mixtral 8x7B model
#model_id = 'ibm/granite-3-8b-instruct' # Specify IBM's Granite 3.3 8B model

# Set the necessary parameters
parameters = {
    GenParams.MAX_NEW_TOKENS: 256,  # Specify the max tokens
    GenParams.TEMPERATURE: 0.5, #  Randomness or creativity of the model's responses
}

# skills-network project_id allowed for learning and free IBM cloud IDE environment
# for personal/local environment, see: https://medium.com/the-power-of-ai/ibm-watsonx-ai-the-interface-and-api-e8e1c7227358
project_id = "skills-network"

# Wrap model into WatsonxLLM inference
watsonx_llm = WatsonxLLM(
    model_id=model_id,
    url="https://us-south.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters,
)

# Function to generate a response from the model
def generate_response(prompt_txt):
    generated_response = watsonx_llm.invoke(prompt_txt)
    return generated_response

# Create Gradio interface
chat_application = gr.Interface(
    fn=generate_response,
	allow_flagging="never",
    inputs=gr.Textbox(label="Input", lines=2, placeholder="Type your question here..."),
    outputs=gr.Textbox(label="Output"),
    title="Watsonx.ai Chatbot",
    description="Ask any question and the chatbot will try to answer."
)

# Launch the app
chat_application.launch(server_name="127.0.0.1", server_port= 7860)
