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
        \\item Horst Possegger, Thomas Mauthner, and Horst Bischof. \\textit{{In Defense of Color-based Model-free Tracking}}. In Proc. CVPR 2015.
        \\item Ahmad Ali, Abdul Jaleel. \\textit{{Visual Object Tracking, Classical and Contemporary Approaches}}. In Frontiers of Computer Science. Higher Education Press and Springer-Verlag Berlin Heidelberg, 2015.
        \\item Xi Li, Weiming Hu, Chunhua Shen, Zhongfei Zhang, Anthony Dick, Anton vanden Hengel. \\textit{{A Survey of Appearance Models in Visual Object Tracking}}. ACM Transactions on Intelligent Systems and Technology, 2013.
        \\item 
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
