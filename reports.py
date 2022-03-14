#!/usr/bin/env python3

from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors

def generate_report(filename, title, additional_info):
  styles = getSampleStyleSheet()
  report = SimpleDocTemplate(filename)
  report_title = Paragraph(title, styles["h1"])
  content = [report_title]

  for item in additional_info:
    name = Paragraph(item["name"], styles["Normal"])
    weight = Paragraph(str(item["weight"]), styles["Normal"])
    empty_line = Spacer(1,20)
    content.extend([name, weight, empty_line])

  report.build(content)
