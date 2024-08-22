import pdfkit

def save_as_pdf(title: str, html):
    config = pdfkit.configuration(wkhtmltopdf='api/bin/wkhtmltopdf.exe')
    filename = 'api/' + '_'.join(title.split(' ')) + '.pdf'
    pdfkit.from_string(html, filename, configuration=config, css='api/static/style.css')

    return filename
