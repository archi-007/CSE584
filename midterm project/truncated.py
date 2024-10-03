'''truncated.py produces the xi in the problem statement. use different datasets as per use case. an example is given'''

from datasets import load_dataset
import re
import pandas as pd


# dataset = load_dataset("openwebtext")
dataset = load_dataset("wikitext", "wikitext-2-v1")

def truncate_sentences(text, num_words=5):
    sentences = re.split(r'(?<=[.!?]) +', text)    
    truncated_texts = []
    for sentence in sentences:
        words = sentence.split()[:num_words]
        truncated_text = ' '.join(words)
        if truncated_text:
            truncated_texts.append(truncated_text)
    
    return truncated_texts

truncated_dataset = []


for text in dataset['train']['text'][:1000]:
    truncated_dataset.extend(truncate_sentences(text))


df = pd.DataFrame(truncated_dataset, columns=["truncated_text"])

df.to_csv("xi.csv", index=False)


