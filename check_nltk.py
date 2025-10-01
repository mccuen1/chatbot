"""Small script to check and download required NLTK resources.
Run this in PowerShell: python check_nltk.py
"""
import nltk

REQUIRED = {
    'punkt': 'tokenizers/punkt',
    'wordnet': 'corpora/wordnet',
    'omw-1.4': 'corpora/omw-1.4',
}

def main():
    for res, path in REQUIRED.items():
        try:
            nltk.data.find(path)
            print(f"NLTK resource '{res}' is already available.")
        except LookupError:
            print(f"NLTK resource '{res}' not found — downloading...")
            nltk.download(res)
    print("All done. If downloads succeeded, you can run train_chatbot.py now.")

if __name__ == '__main__':
    main()
