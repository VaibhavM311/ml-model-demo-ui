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

.gr-button:hover {
    filter: brightness(1.1);
}

.gr-box, .gradio-group {
    border-radius: 16px !important;
    box-shadow: 0 6px 18px rgba(0,0,0,0.25);
    border: 1px solid rgba(255,255,255,0.08);
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
                    label="Education Level (0=UG, 1=PG, 2=PhD)"
                )
                projects = gr.Slider(0, 10, step=1, label="Projects Completed")
                internship = gr.Radio(
                    [0, 1],
                    label="Internship (0=No, 1=Yes)"
                )
                communication = gr.Slider(1, 10, step=1, label="Communication Skills")

                submit_btn = gr.Button("🔍 Evaluate Candidate")

            with gr.Column():
                output = gr.Textbox(
                    label="🎯 Prediction Result",
                    lines=2
                )

        submit_btn.click(
            predict,
            inputs=[exp, skills, edu, projects, internship, communication],
            outputs=output
        )

    with gr.Tab("ℹ️ About Inputs"):
        gr.Markdown("""
        ### 📌 Input Components Used
        - **Slider** → Numerical values
        - **Radio Buttons** → Education & Internship
        - **Textbox Output** → Prediction result
        
        Designed with a **Corporate ATS Dashboard Theme** for a professional user experience.
        """)

app.launch()