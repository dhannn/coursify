import os
import pdfkit

def save_as_pdf(title: str, html):
    # config = pdfkit.configuration(wkhtmltopdf=f'{ os.getenv("NIXPACKS_PKG") }/wkhtmltopdf.exe')
    filename = '_'.join(title.split(' ')) + '.pdf'
    pdfkit.from_string(html, filename, css='static/style.css')

    return filename
