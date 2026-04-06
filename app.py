import gradio as gr
import pickle
import numpy as np

# Load trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

def predict(exp, skills, edu, projects, internship, communication):
    # Prevent None values
    exp = exp or 0
    skills = skills or 0
    edu = edu if edu is not None else 0
    projects = projects or 0
    internship = internship if internship is not None else 0
    communication = communication or 1

    input_data = np.array([[exp, skills, edu, projects, internship, communication]])
    prediction = model.predict(input_data)[0]

    score = min(
        100,
        int(
            skills * 0.4
            + exp * 5
            + projects * 3
            + internship * 10
            + communication * 2
            + edu * 5
        )
    )

    labels = {
        2: "✅ Strong Hire",
        1: "🟡 Consider",
        0: "❌ Reject"
    }

    return labels[prediction], score


# Corporate Tech CSS
custom_css = """
.gradio-container {
    background: linear-gradient(135deg, #0b1120, #111827);
}

h1, h2, h3, p, label {
    color: #e5e7eb !important;
    font-family: Arial, sans-serif;
}

.gr-button {
    background: linear-gradient(90deg, #2563eb, #1d4ed8) !important;
    color: white !important;
    border-radius: 12px !important;
    font-weight: bold !important;
    border: none !important;
    box-shadow: 0 4px 12px rgba(37, 99, 235, 0.35);
}
"""

with gr.Blocks(
    theme=gr.themes.Soft(
        primary_hue="blue",
        secondary_hue="slate",
        neutral_hue="slate"
    ),
    css=custom_css
) as app:

    gr.Markdown("# 📊 Enterprise Resume Screening Dashboard")
    gr.Markdown("Evaluate candidate suitability with AI-powered analytics")

    with gr.Tab("📝 Candidate Input"):
        with gr.Row():
            with gr.Column():
                exp = gr.Slider(0, 10, step=1, label="Years of Experience")
                skills = gr.Slider(0, 100, step=1, label="Skills Match (%)")
                edu = gr.Radio(
                    [0, 1, 2],
                    value=0,
                    label="Education Level (0=UG, 1=PG, 2=PhD)"
                )
                projects = gr.Slider(0, 10, step=1, label="Projects Completed")
                internship = gr.Radio(
                    [0, 1],
                    value=0,
                    label="Internship (0=No, 1=Yes)"
                )
                communication = gr.Slider(1, 10, step=1, label="Communication Skills")

                submit_btn = gr.Button("🔍 Evaluate Candidate")

            with gr.Column():
                result_label = gr.Textbox(
                    label="🎯 Hiring Decision",
                    lines=2
                )

                score_output = gr.Slider(
                    minimum=0,
                    maximum=100,
                    label="📊 Candidate Score",
                    interactive=False
                )

        # Week 6 main linking task
        submit_btn.click(
            fn=predict,
            inputs=[
                exp,
                skills,
                edu,
                projects,
                internship,
                communication
            ],
            outputs=[
                result_label,
                score_output
            ]
        )

    with gr.Tab("ℹ️ About Inputs"):
        gr.Markdown("""
        ### 📌 Input Components Used
        - **Slider** → Numerical values
        - **Radio Buttons** → Education & Internship
        - **Textbox + Score Bar** → Output
        
        Designed with a **Corporate ATS Dashboard Theme**.
        """)

app.launch()