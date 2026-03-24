import gradio as gr

def demo(exp, skills, edu, projects, internship, communication):
    return f"Candidate with {exp} yrs exp and {skills}% skills evaluated successfully!"

app = gr.Interface(
    fn=demo,
    inputs=[
        gr.Number(label="Years of Experience"),
        gr.Number(label="Skills Match (%)"),
        gr.Dropdown([0,1,2], label="Education (0=UG,1=PG,2=PhD)"),
        gr.Number(label="Projects Completed"),
        gr.Dropdown([0,1], label="Internship (0=No,1=Yes)"),
        gr.Slider(1,10,label="Communication Skills")
    ],
    outputs=gr.Textbox(label="Evaluation Result"),
    title="AI Resume Screening System",
    description="Enter candidate details to evaluate resume"
)

app.launch()