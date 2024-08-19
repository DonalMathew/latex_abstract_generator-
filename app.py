from flask import Flask, render_template, request, send_file
import subprocess
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    heading = request.form['heading']
    body = request.form['body']
    student_name = request.form['student_name']
    faculty_name = request.form['faculty_name']
    
    # LaTeX template
    latex_template = f"""
    \\documentclass{{article}}
    \\begin{{document}}

    \\title{{\\textbf{{{heading}}}}}
    \\author{{}}
    \\date{{}}

    \\maketitle

    \\section*{{Abstract}}
    {body}

    \\vspace{{10pt}}

    \\begin{{tabular}}{{|l|l|}}
    \\hline
    Student Name & {student_name} \\\\
    Faculty Name & {faculty_name} \\\\
    \\hline
    \\end{{tabular}}

    \\end{{document}}
    """
    
    # Write to a .tex file
    tex_file = 'abstracts/abstract.tex'
    with open(tex_file, 'w') as f:
        f.write(latex_template)
    
    # Compile the .tex file into a PDF
    #subprocess.run(['pdflatex', '-output-directory=abstracts', tex_file])
    
    #pdf_file = 'abstracts/abstract.pdf'
    #if os.path.exists(pdf_file):
    #    return send_file(pdf_file, as_attachment=True)
    #else:
    #   return "Error in generating PDF", 500

if __name__ == '__main__':
    if not os.path.exists('abstracts'):
        os.makedirs('abstracts')
    app.run(debug=True)
