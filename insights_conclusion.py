from fpdf import FPDF

class PDFReport(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.cell(0, 10, 'Unemployment Analysis Report', ln=True, align='C')

    def chapter_title(self, title):
        self.set_font('Arial', 'B', 14)
        self.cell(0, 10, title, ln=True)
        self.ln(5)

    def chapter_body(self, body):
        self.set_font('Arial', '', 12)
        self.multi_cell(0, 10, body)
        self.ln()

# Creating PDF report
pdf = PDFReport()
pdf.add_page()

pdf.chapter_title('Key Insights')
pdf.chapter_body(
    "1. The unemployment rate in India showed a significant spike during the COVID-19 pandemic period.\n"
    "2. States like Delhi, Haryana, and Rajasthan experienced the highest unemployment rates.\n"
    "3. Rural areas displayed more stable unemployment trends compared to urban regions.\n"
    "4. The unemployment rate peaked in April 2020, followed by gradual stabilization.\n"
)

pdf.chapter_title('Conclusion')
pdf.chapter_body(
    "The analysis highlights the impact of economic disruptions on India's employment landscape. "
    "Recommendations include promoting digital skill programs and expanding employment initiatives to support job recovery."
)

pdf.output("../output/insights_report.pdf")
print("Report successfully generated!")
