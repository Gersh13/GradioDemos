import gradio as gr

def combine(a, b):
    return a + " " + b

# Define the interface
demo = gr.Interface(
    fn=combine, 
    inputs=[gr.Textbox(label="Input1"), gr.Textbox(label="Input2")], # Two text box inputs
    outputs=gr.Textbox() # Create textbox output field
)

# Launch the interface
demo.launch(server_name="127.0.0.1", server_port= 7860)
