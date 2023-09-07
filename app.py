from flask import Flask, request, jsonify, render_template, redirect, url_for
import fitz
import os

app = Flask(__name__)

UPLOAD_FOLDER = '/Users/venu/Library/Mobile Documents/com~apple~CloudDocs/Downloads/Documents /Resume/'
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
        
        file = request.files["file"]

        if file.filename == '':
            return redirect(request.url)
        
        if file:
            filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filename)
            extracted_text = Extract_text_from_pdf(pdf_path=filename)
            return render_template('index.html', extracted_text=extracted_text)
        
    return render_template('index.html', extracted_text=None)


if __name__=="__main__":
    app.run(debug=True)