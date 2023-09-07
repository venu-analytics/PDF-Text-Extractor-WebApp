 ## PDF Text Extractor

This is a simple Flask application that allows users to upload a PDF file and extract the text from it.

### Prerequisites

To run this application, you will need the following:

* Python 3.6 or later
* Flask
* Fitz

You can install Flask and Fitz using pip:

```
pip install Flask
pip install fitz
```

### Setup

Once you have installed the required dependencies, you can clone this repository and install the dependencies:

```
git clone https://github.com/venu-gopal-k/pdf-text-extractor.git
cd pdf-text-extractor
pip install -r requirements.txt
```

### Usage

To run the application, simply run the following command:

```
python app.py
```

The application will be available at http://localhost:5000.

### Features

The application has the following features:

* Users can upload a PDF file and extract the text from it.
* The extracted text is displayed on the screen.
* The extracted text can be saved to a file.

### Code Explanation

The application consists of the following files:

* `app.py`: The main Flask application file.
* `templates/index.html`: The HTML template for the application.

The `app.py` file contains the following code:

```python
from flask import Flask, request, jsonify, render_template, redirect, url_for
import fitz
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def Extract_text_from_pdf(pdf_path):
    try:
        doc = fitz.open(pdf_path)
        text = " "
        for page_no in range(doc.page_count):
            page = doc.load_page(page_no)
            text += page.get_text()
        return text
    except Exception as e:
        return str(e)
    

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)