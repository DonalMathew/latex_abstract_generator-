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
    student_name = request.form['student_name']
    student_class = request.form['student_class']
    student_rollno = request.form['student_rollno']
    faculty_name = request.form['faculty_name']
    body = request.form['body']
    ref1 = request.form['ref1']
    ref2 = request.form['ref2']
    ref3 = request.form['ref3']
    ref4 = request.form['ref4']
    ref5 = request.form['ref5']
    ref6 = request.form['ref6']
    




    #check whether form-field is null
    if not ref1:
        new_ref1=ref1
    else:
        new_ref1 = f"""\\item {ref1}"""
    if not ref2:
        new_ref2=ref2
    else:
        new_ref2 = f"""\\item {ref2}"""
    if not ref3:
        new_ref3=ref3
    else:
        new_ref3 = f"""\\item {ref3}"""
    if not ref4:
        new_ref4=ref4
    else:
        new_ref4 = f"""\\item {ref4}"""
    if not ref5:
        new_ref5=ref5
    else:
        new_ref5 = f"""\\item {ref5}"""
    if not ref6:
        new_ref6=ref6
    else:
        new_ref6 = f"""\\item {ref6}"""
    






    # Updated LaTeX template
    latex_template = f"""
    \\documentclass{{article}}
    \\usepackage{{geometry}}
    \\usepackage{{array}}
    \\geometry{{a4paper, margin=1in}}

    \\title{{{heading}}}

    \\date{{}}

    \\begin{{document}}

    \\maketitle

    \\begin{{table}}[h!]
    \\centering
    \\begin{{tabular}}{{|p{{4cm}}|p{{10cm}}|}}
        \\hline
        \\textbf{{Student Name}} & {student_name} \\\\ \\hline
        \\textbf{{Class}} & {student_class} \\\\ \\hline
        \\textbf{{Roll no.}} & {student_rollno} \\\\ \\hline
        \\textbf{{Faculty Name}} & {faculty_name} \\\\ \\hline
    \\end{{tabular}}
    \\label{{tab:faculty_student_details}}
    \\end{{table}}

    \\begin{{abstract}}
    {body}
    \\end{{abstract}}

    \\section*{{References}}

    \\begin{{enumerate}}
        {new_ref1}
        {new_ref2}
        {new_ref3}
        {new_ref4}
        {new_ref5}
        {new_ref6} 
    \\end{{enumerate}}

    \\end{{document}}
    """
    
    # Write to a .tex file
    tex_file = 'abstracts/abstract.tex'
    with open(tex_file, 'w') as f:
        f.write(latex_template)
    
    # Compile the .tex file into a PDF
    subprocess.run(['pdflatex', '-output-directory=abstracts', tex_file])
    
    pdf_file = 'abstracts/abstract.pdf'
    if os.path.exists(pdf_file):
        return send_file(pdf_file, as_attachment=True)
    else:
        return "Error in generating PDF", 500

if __name__ == '__main__':
    if not os.path.exists('abstracts'):
        os.makedirs('abstracts')
    app.run(debug=True)
