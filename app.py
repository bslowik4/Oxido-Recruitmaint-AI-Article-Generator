import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

def import_article(file_path):
    """ 
    Function importing artilce contnent from text file.

    Args:
    file_path (str): path to article content file saved as txt

    Returns:
    str: content of the article
    
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    article_path = "TrescArtykulu.txt"
    article_text = import_article(article_path)
    print("Imported Article Text:\n", article_text)

if __name__ == "__main__":
    main()
