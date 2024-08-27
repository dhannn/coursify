import os
from flask import Flask, render_template, request, send_file

from pdf_saver import save_as_pdf
from model import AIGenModel
from markdown import markdown
from markupsafe import Markup

app = Flask(__name__)
model = AIGenModel()

@app.route('/', methods=['POST', 'GET'])
def index():

    print(f'{ os.getenv('NIXPACKS_PKG')}')

    if request.method == 'POST':
        # Retrieve form data
        course_title = request.form.get('course-title', '')
        objectives = request.form.get('objectives', '')
        target_audience = request.form.get('target-audience', '')
        weekly_commitment = request.form.get('weekly-commitment', '')
        duration = request.form.get('duration', '')
        other_comments = request.form.get('other-comments', '')

        # Create course syllabus
        course_syllabus = model.create_course(
            course_title,
            objectives,
            target_audience,
            weekly_commitment,
            duration,
            other_comments
        )
        
        result_markdown = course_syllabus.replace('\n', '\\n').replace('"', "\\\"").replace('“', "\\\"").replace('\'', '\\\'')
        result_html = Markup(markdown(course_syllabus))
        print(result_html)

        # print(result_html.replace('\n', '\\n').replace('\n', '\\t').replace('"', "\\\"").replace('“', "\"").replace('\'', '\\\''))

        return render_template(
            'form.html', result_markdown=result_markdown, 
                result_html=result_html,
                result_pdf=markdown(course_syllabus).replace('\n', '\\n').replace('\n', '\\t').replace('"', "\\\"").replace('\'', '\\\''),
                title=course_title)
    
    return render_template('form.html')

@app.route('/save_pdf', methods=['POST'])
def save_pdf():
    if request.method == 'POST':
        course_title = request.get_json()['title']
        html = request.get_json()['html']

        filename = save_as_pdf(course_title, html)
        return send_file(filename, as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)
    