from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate_cover_letter', methods=['POST'])
def generate_cover_letter():
    name = request.form.get('name', '')
    position = request.form.get('position', '')
    company = request.form.get('company', '')
    experience = request.form.get('experience', '')
    skills = request.form.get('skills', '')
    additional_info = request.form.get('additional_info', '')

    # Generate the cover letter content
    cover_letter = f"""
    {name}<br><br>
    {company}<br><br>
    Dear Hiring Manager,<br><br>
    I am writing to express my interest in the {position} position at {company}. With {experience} years of experience in the industry and skills in {skills}, I believe I am a strong candidate for this role.<br><br>
    {additional_info}<br><br>
    Thank you for considering my application. I look forward to the opportunity to discuss my qualifications further.<br><br>
    Sincerely,<br><br>
    {name}
    """

    return render_template('cover_letter.html', cover_letter=cover_letter)

if __name__ == '__main__':
    app.run(debug=True)
