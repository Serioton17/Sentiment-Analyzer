import gradio as gr
from transformers import pipeline

classifier = pipeline("sentiment-analysis")

def analyze(text):
    result = classifier(text)[0]
    return f"{result['label']} ({result['score']:.1%} confident)"

gr.Interface(
    fn=analyze,
    inputs=gr.Textbox(label="Paste a comment"),
    outputs="text",
    title="Comment Sentiment Analyzer",
    theme = gr.themes.Glass()
).launch()