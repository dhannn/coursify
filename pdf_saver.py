import os
import pdfkit

def save_as_pdf(title: str, html):

    environment = os.environ.get('ENVIRONMENT', 'dev')

    filename = '_'.join(title.split(' ')) + '.pdf'
    if environment == 'dev':
        config = pdfkit.configuration(wkhtmltopdf=f'bin/wkhtmltopdf.exe')
        pdfkit.from_string(html, filename, configuration=config, css='static/style.css')
    else:
        pdfkit.from_string(html, filename, css='static/style.css')
        

    return filename
