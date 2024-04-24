# The MIT License (MIT)
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
# The above copyright notice and this permission notice shall be included
# in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Model training.
Run it with 'python3 train.py'.
"""
from datasets import load_dataset, DatasetDict
from transformers import Trainer, TrainingArguments, AutoTokenizer, \
    AutoModelForSequenceClassification

from metrics import metrics

model = AutoModelForSequenceClassification.from_pretrained(
    "distilbert/distilbert-base-uncased",
    num_labels=2,
    id2label={0: "NEGATIVE", 1: "POSITIVE"},
    label2id={"NEGATIVE": 0, "POSITIVE": 1}
)
tokenizer = AutoTokenizer.from_pretrained("distilbert/distilbert-base-uncased")
dataset = load_dataset("h1alexbel/github-samples")


def preprocess(examples):
    # @todo #45:60min Train model on target columns instead just full_name.
    #  We should re-train model probably on description, topics and readme too.
    #  Let's try to standardize the input: first go full_name and description,
    #  than topics. README's content can be very big and can break the model.
    #  For readme we can use some summarization model that would provide
    #  limited-type response.
    return tokenizer(
        examples["full_name"],
        truncation=True,
        padding='max_length',
        max_length=512
    )


tokenized = dataset.map(preprocess, batched=True)
dictionary = DatasetDict(
    {
        'train': tokenized['train'],
    }
)
split = dictionary["train"].train_test_split(test_size=0.2)
dictionary["train"] = split["train"]
dictionary["validation"] = split["test"]
training_args = TrainingArguments(
    output_dir="github-samples-classifier",
    num_train_epochs=3,
    per_device_train_batch_size=8,
    per_device_eval_batch_size=32,
    warmup_steps=500,
    weight_decay=0.01,
    learning_rate=2e-5,
    logging_dir='./logs',
    push_to_hub=True
)
trainer = Trainer(
    model=model,
    tokenizer=tokenizer,
    args=training_args,
    train_dataset=dictionary["train"],
    eval_dataset=dictionary["validation"],
    compute_metrics=metrics
)
trainer.train()
trainer.evaluate()
model.save_pretrained('./trained')
tokenizer.save_pretrained('./trained')
