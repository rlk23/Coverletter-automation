import os
from flask import Flask, request, render_template, send_file
from create_coverletter import generate_cover_letter

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    job_link = request.form['job_link']
    resume_file = request.files['resume']
    openai_api_key = request.form['openai_api_key']

    # Save uploaded resume file
    resume_path = os.path.join(app.config['UPLOAD_FOLDER'], resume_file.filename)
    resume_file.save(resume_path)

    # Generate cover letter
    output_path = generate_cover_letter(job_link, resume_path, openai_api_key)

    return send_file(output_path, as_attachment=True)

if __name__ == "__main__":
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    app.run(debug=True)
