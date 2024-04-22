from transformers import BertTokenizer, BertForSequenceClassification
import torch

# Load the trained model and tokenizer
model = BertForSequenceClassification.from_pretrained('./trained')
tokenizer = BertTokenizer.from_pretrained('./trained')

# for name, param in model.named_parameters():
#     if torch.isnan(param).any():
#         print(f"NaN found in {name}")

input_text = (
    "This repository is no longer actively updated.  Please see https://github.com/openjdk for a much better "
    "mirror of OpenJDK!"
)
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model(**inputs)
probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

# The model's output is a tensor of probabilities for each class.
# You can get the predicted class by finding the index of the maximum probability.
predicted_class = torch.argmax(probs).item()

# Map the predicted class index back to the label
label_mapping = {0: "negative", 1: "positive"}
predicted_label = label_mapping[predicted_class]

print("Raw logits:", outputs.logits)
print("Probabilities:", probs)
print(f"Predicted label: {predicted_label}")
