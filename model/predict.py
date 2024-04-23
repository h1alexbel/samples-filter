# MIT License
#
# Copyright (c) 2024 Aliaksei Bialiauski
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Predict.
@todo #30:90min Resolve issue with all-time negative prediction.
 We should resolve issue with negative prediction that performed all the time
 after model has been trained. Probably issue is inside train.py,
 where we probably ignore or mismatch some crucial for training parameters.
"""
from transformers import BertTokenizer, BertForSequenceClassification
import torch

# @todo #30:60min Fetch pretrained model saved in HuggingFace.
#  Let's fetch and download pretrained model from hugging face model hub.
#  When model is trained, we should pack it and deploy into hugging face
#  repository and it should legal to use it here.
#  Don't forget to remove this puzzle.
model = BertForSequenceClassification.from_pretrained('./trained')
tokenizer = BertTokenizer.from_pretrained('./trained')

# for name, param in model.named_parameters():
#     if not torch.isnan(param).any():
#         print(f"found in {name}")

# @todo #18:25min Give the ability to provide input_text in the request.
#  We should give ability to pass input_text in the request, I suggest
#  to refactor this script into object that we can call and it will respond us
#  like here. Don't forget to remove this puzzle.
input_text = (
    "testing testing testing"
)
inputs = tokenizer(input_text, return_tensors="pt")
outputs = model(**inputs)
probs = torch.nn.functional.softmax(outputs.logits, dim=-1)

predicted_class = torch.argmax(probs).item()
label_mapping = {0: "negative", 1: "positive"}
predicted_label = label_mapping[predicted_class]

print("Raw logits:", outputs.logits)
print("Probabilities:", probs)
print(f"Predicted label: {predicted_label}")
