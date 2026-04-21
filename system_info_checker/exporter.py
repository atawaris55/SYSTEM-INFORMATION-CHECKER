from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet

def export_to_pdf(info, filename="system_report.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    content = []

    content.append(Paragraph("System Information Report", styles["Title"]))
    content.append(Spacer(1, 10))

    for key, value in info.items():
        line = f"{key}: {value}"
        content.append(Paragraph(line, styles["Normal"]))
        content.append(Spacer(1, 5))

    doc.build(content)

    print(f"\n✅ PDF created successfully: {filename}")