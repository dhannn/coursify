from flask import Flask, render_template, request
from api.model import AIGenModel
from markdown import markdown
from markupsafe import Markup

app = Flask(__name__)
model = AIGenModel()

@app.route('/', methods=['POST', 'GET'])
def home():

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
        
        result_markdown = course_syllabus.replace('\n', '\\n').replace('"', "\"").replace('“', "\"").replace('\'', '\\\'')
        result_html = Markup(markdown(course_syllabus))

        return render_template(
            'form.html', result_markdown=course_syllabus
                .replace('\n', '\\n')
                .replace('"', "\\\"")
                # .replace('“', "\"")
                .replace('\'', '\\\''), 
                result_html=result_html)
    
    return render_template('form.html')


if __name__ == '__main__':
    app.run(debug=True)
    