 🎭 Comment Sentiment Analyzer

A small beginner project to find out if a comment is **positive** or **negative**.

You paste a comment (like a YouTube comment), click a button, and the app tells you the mood of the comment and how confident it is.

---

📌 What This Project Does

- Takes a sentence or comment as input
- Uses an AI model from Hugging Face to read it
- Shows the result: **POSITIVE** or **NEGATIVE**, with a confidence score
- Runs as a simple web app in your browser

**Example**

| Input | Output |
|---|---|
| "I loved this sketch, so funny!" | POSITIVE (99.9% confident) |
| "This video was boring" | NEGATIVE (99.8% confident) |

---

 🎯 Why I Built This

I made this project to understand how Hugging Face actually works. It is small, runs on a normal laptop, and teaches the main ideas:

- **Model**: the trained AI "brain" that we download and use
- **Hugging Face Hub**: a website where people share AI models (think of it as GitHub for AI)
- **Pipeline**: a ready-made shortcut that does everything in a few lines
- **Tokenizer**: turns words into numbers, because AI models only understand numbers
- **Gradio**: a tool that turns Python code into a web page

---

🧠 How It Works (Simple Explanation)

```
Your text  →  Tokenizer  →  Model  →  Scores  →  Final label
"Great!"      [101, 2307]    (AI)      [0.01, 0.99]   POSITIVE
```

1. **Tokenizer** changes your text into numbers
2. **Model** reads those numbers and gives raw scores
3. **Softmax** changes the scores into percentages
4. The highest percentage becomes the **label**

The model used here is `distilbert-base-uncased-finetuned-sst-2-english`. It is small, fast, and already trained to detect positive and negative sentences in English.

---

 🛠️ Technologies Used

| Tool | What it is used for |
|---|---|
| Python | The programming language |
| Transformers | Hugging Face library to load and use models |
| PyTorch (torch) | The engine that runs the model |
| Gradio | Builds the web interface |

---

 📁 Project Structure

```
hf-project/
│
├── step1.py     # First try: sentiment analysis using pipeline (5 lines)
├── step2.py     # Looks inside the pipeline: tokenizer + model + softmax
├── app.py       # The final web app built with Gradio
└── README.md    # This file
```

🎨 Change the Look

- **Theme**: try `gr.themes.Soft()`, `gr.themes.Glass()`, `gr.themes.Monochrome()` or `gr.themes.Ocean()`
- **Color**: change `primary_hue="purple"` to another color like `"blue"` or `"green"`
- **Layout**: use `gr.Blocks()` with `gr.Row()` and `gr.Column()` for full control

---

 🧪 Things to Try

1. Type tricky sentences like "Not bad at all" or "Yeah right, great video 🙄" and see where the model gets confused
2. Swap the model for another one from [huggingface.co/models](https://huggingface.co/models)
3. Try other tasks with the same style of code: `summarization`, `translation_en_to_fr`, `zero-shot-classification`
4. Send a list of comments at once and count how many are positive and negative

---

## ⚠️ Limitations

- Works best with **English** text
- Only gives **positive** or **negative** (no neutral)
- Can be fooled by sarcasm and slang
- Needs internet only the first time, to download the model

---

## 🚀 Future Ideas

- Add a **neutral** result using another model
- Upload many comments from a file and see a summary
- Add a chart showing how many comments are positive vs negative
- Fine-tune the model on my own data
- Publish the app for free on **Hugging Face Spaces**

---

## 📚 What I Learned

- How to load and use a model from the Hugging Face Hub
- What a pipeline, tokenizer, and model each do
- How to build a simple web app with Gradio
- That AI models are not perfect, and testing them is important

---

## 👤 Author

Made by **Yourname** as a beginner learning project.
