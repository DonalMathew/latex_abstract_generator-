document.getElementById('abstract-form').addEventListener('submit', function(event) {
    event.preventDefault();
    
    const heading = document.getElementById('heading').value;
    const body = document.getElementById('body').value;
    const studentName = document.getElementById('student-name').value;
    const facultyName = document.getElementById('faculty-name').value;
    
    let latexTemplate = `
    \\documentclass{article}
    \\begin{document}

    \\title{\\textbf{${heading}}}
    \\author{}
    \\date{}

    \\maketitle

    \\section*{Abstract}
    ${body}

    \\vspace{10pt}

    \\begin{tabular}{|l|l|}
    \\hline
    Student Name & ${studentName} \\\\
    Faculty Name & ${facultyName} \\\\
    \\hline
    \\end{tabular}

    \\end{document}
    `;
    
    console.log(latexTemplate);  // For testing purposes
});
