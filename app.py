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

def generate_html_content(article_text):
    """
    Generates HTML content based on the provided article text using the OpenAI API. 
    Structures the content with appropriate HTML tags and adds placeholders for images with captions.
    
    Args:
        article_text (str): The content of the article to be converted into HTML.
    
    Returns:
        str: HTML content with embedded image placeholders and captions, if successful.
        None: If an error occurs during the API request, the function prints an error message and returns None.
    
    Error Handling:
        If there is an exception during the API call (e.g., network issues or API errors), 
        an error message is printed, and the function returns None.
    """

    prompt = """
    Create HTML for the following article. Use appropriate HTML tags to structure the content. Insert placeholders for images using <img src='image_placeholder.jpg'> with an alt attribute and captions for the images in the appropriate places. The image should ideally be placed next to large headings. It can also open or conclude the text.
    Generate the code to be inserted between the <body> and </body> tags, so without CSS, JS, and without the body tags themselves. \n\n
    Article: \n
    """ + article_text


    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
            {"role": "system", "content": "You are an intriguing article writer."},
            {"role": "user", "content": prompt}
        ]
            max_tokens=1500,
            temperature=0.7
        )
        generated_html = response['choices'][0]['message']['content']
        return generated_html

    except Exception as e:
        print("An error occurred:", e)
        return None



def main():
    article_path = "TrescArtykulu.txt"
    article_text = import_article(article_path)
    print("Imported Article Text:\n", article_text)
    html_content = generate_html_content(article_text)
    print("\nGenerated HTML Content:\n", html_content)

if __name__ == "__main__":
    main()
