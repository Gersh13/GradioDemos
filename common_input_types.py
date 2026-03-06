import gradio as gr

def sentence_builder(quantity, tech_worker_type, countries, place, activity_list, morning):
    return f"""The {quantity} {tech_worker_type}s from {" and ".join(countries)} went to the {place} where they {" and ".join(activity_list)} until the {"morning" if morning else "night"}."""

demo = gr.Interface(
    fn=sentence_builder,
    inputs=[
        gr.Slider(3, 20, value=4, step=1, label="Count", info="Choose between 3 and 20"),
        gr.Dropdown(
            ["Data Scientist", "Software Developer", "Software Engineer"], 
			label="Type of Role", 
			info="Will add more tech roles later!"
        ),
        gr.CheckboxGroup(["United States", "Colombia", "Mexico", "Czechia", "Italy"], label="Countries", info="Where are they from?"),
        gr.Radio(["office", "restaurant", "meeting room"], label="Location", info="Where did they go?"),
        gr.Dropdown(
            ["sprint planned", "code reviewed", "brainstormed", "talked"], 
			value=["sprint planned", "brainstormed"], 
			multiselect=True, 
			label="Activities", 
			info="Which activities did they perform?"
        ),
        gr.Checkbox(label="Morning", info="Did they do it into the morning?"),
    ],
    outputs="text",
    examples=[
        [3, "Software Developer", ["United States", "Mexico"], "restaurant", ["code reviewed", "talked"], True],
        [4, "Data Scientist", ["Czechia"], "office", ["brainstormed", "talked"], False],
        [10, "Software Engineer", ["Colombia", "Mexico"], "meeting room", ["brainstormed"], False],
        [8, "Data Scientist", ["United States"], "restaurant", ["sprint planned"], True],
    ]
)

demo.launch(server_name="127.0.0.1", server_port= 7860)
