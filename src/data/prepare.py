from pathlib import Path

import pandas as pd


def read_texts(path):
    data_path = Path(path)
    texts = []
    for file_path in data_path.glob("*.txt"):
        with open(file_path, 'rt') as file:
            texts.append(file.read())
    return texts

def make_text_dataframe(true_path, fake_path, output_path):
    true_texts = read_texts(true_path)
    fake_texts = read_texts(fake_path)
    text_df = pd.DataFrame({
        'text': true_texts + fake_texts,
        'label': len(true_texts) * ['true'] + len(fake_texts) * ['fake']
    })
    text_df.to_csv(output_path, index=False, mode='w')