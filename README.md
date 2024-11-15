# HTML Article Generator

This project generates structured HTML content from a given article text file using the OpenAI API. The generated HTML includes appropriate tags, image placeholders, and captions to make the article ready for web display.

## Features
- Reads an article from a text file.
- Sends the article content to OpenAI's API to generate HTML.
- Saves the generated HTML to a file (`artykul.html`) automatically.
- Includes placeholders for images and captions in the HTML.

## Setup

### Prerequisites
- Python 3.6 or higher
- An [OpenAI API key](https://platform.openai.com/signup)

### Installation
1. **Clone this repository**:
   ```bash
   git clone https://github.com/bslowik4/Oxido-Recruitmaint-AI-Article-Generator
   cd Oxido-Recruitmaint-AI-Article-Generator
   ```

2. **Install the required Python packages**:
   ```bash
   pip install openai python-dotenv
   ```

3. **Set up your API key**:
   - Create a `.env` file in the project root and add your OpenAI API key:
     ```bash
     echo "OPENAI_API_KEY=your_actual_openai_key" > .env
     ```

4. **Prepare your article**:
   - Place the article content you want to convert into HTML in a file named `article.txt` in the project directory.

### Running
Run the project with:
```bash
python app.py
```