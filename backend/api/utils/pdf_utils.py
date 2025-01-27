from fpdf import FPDF
import os

def generate_pdf(summary):
    try:
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, summary)
        pdf_file = 'summary.pdf'
        pdf.output(pdf_file)
        return pdf_file
    except Exception as e:
        print(f"Error generating PDF: {e}")
        return None