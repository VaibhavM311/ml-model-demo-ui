import gradio as gr
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(exp, skills, edu, projects, internship, communication):
    input_data = np.array([[exp, skills, edu, projects, internship, communication]])
    prediction = model.predict(input_data)[0]

    labels = {
        2: "✅ Selected",
        1: "🟡 Maybe",
        0: "❌ Rejected"
    }

    return labels.get(prediction, "Unknown")

app = gr.Interface(
    fn=predict,
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