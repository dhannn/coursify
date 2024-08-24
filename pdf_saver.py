import pdfkit

def save_as_pdf(title: str, html):
    config = pdfkit.configuration(wkhtmltopdf='bin/wkhtmltopdf.exe')
    filename = '_'.join(title.split(' ')) + '.pdf'
    pdfkit.from_string(html, filename, configuration=config, css='static/style.css')

    return filename
