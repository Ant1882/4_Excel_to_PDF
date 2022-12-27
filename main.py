import pandas as pd
from fpdf import FPDF
import glob
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")

for filepath in filepaths:
    # Read in excel data
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    
    # Create the PDF and add a page
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Get info from the filename
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    # Invoice number cell at top of page
    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Invoice no.{invoice_nr}", ln=1)

    pdf.set_font(family="Times", size=16, style="B")
    pdf.cell(w=50, h=8, txt=f"Date: {date}")


    pdf.output(f"PDFs/{filename}.pdf")
