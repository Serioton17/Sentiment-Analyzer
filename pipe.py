from transformers import pipeline

classifier = pipeline("sentiment-analysis")

result = classifier("I love this product! It's amazing and works perfectly. ")

print(result)