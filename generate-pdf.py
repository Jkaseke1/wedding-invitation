from weasyprint import HTML
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
html_file = os.path.join(script_dir, 'invitation-print.html')
pdf_file = os.path.join(script_dir, 'wedding-invitation.pdf')

print(f"Generating PDF from {html_file}...")
HTML(filename=html_file).write_pdf(pdf_file)
print(f"PDF created successfully: {pdf_file}")
