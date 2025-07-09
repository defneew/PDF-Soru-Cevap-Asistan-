from flask import Flask, render_template, request, jsonify
import fitz  # PyMuPDF
import os
import google.generativeai as genai
from dotenv import load_dotenv
import time

load_dotenv()

# Flask app
app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Gemini API key 
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Model v1'e göre doğru tanımlandı
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")

# PDF metni çıkar
def extract_text_from_pdf(filepath):
    text = ""
    with fitz.open(filepath) as doc:
        for page in doc:
            text += page.get_text()
    return text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_pdf():
    file = request.files['pdf']
    question = request.form['question']
    
    if file and question:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        # PDF içeriğini oku
        pdf_text = extract_text_from_pdf(filepath)

        # PDF içeriği çıkarıldıktan sonra silebilirsin:
        time.sleep(1)
        os.remove(filepath)
        
        # İstemciye gönderilecek prompt
        prompt = f"""
        Aşağıda bir PDF dosyasının içeriği verilmiştir. Buna göre soruyu yanıtla.
        PDF içeriği:
        {pdf_text}

        Soru: {question}
        """

        try:
            response = model.generate_content([prompt])
            return jsonify({'answer': response.text})
        except Exception as e:
            print("Gemini HATASI:", e)
            return jsonify({'error': f"Hata oluştu: {str(e)}"}), 500

    return jsonify({'error': 'Dosya ya da soru eksik'}), 400

if __name__ == '__main__':
    app.run(debug=True)
