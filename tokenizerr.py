from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "distilbert-base-uncased-finetuned-sst-2-english"

tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

text = "This video was boring"

# 1. Tokenizer: text -> numbers
inputs = tokenizer(text, return_tensors="pt")
print(inputs)

# 2. Model: numbers -> raw scores (logits)
outputs = model(**inputs)
print(outputs.logits)

# 3. Softmax: raw scores -> probabilities
probs = torch.softmax(outputs.logits, dim=1)
print(probs)
print(model.config.id2label)