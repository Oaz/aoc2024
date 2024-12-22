from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from src.day21 import *

pdf_filename = "/tmp/day21.pdf"
doc = SimpleDocTemplate(
  pdf_filename,
  pagesize=(65 * cm, 45 * cm),
  rightMargin=30,
  leftMargin=30,
  topMargin=30,
  bottomMargin=18
)

pairs_header_row = {
  Robot.indexes[token]: '\n'.join([
    a + '➔' + b for ((a, b), t) in Robot.sequences.items() if t == token
  ])
  for token in Robot.sequences.values()
}

num_rows, num_cols = Robot.matrix.shape

table_data = [
               ['', ''] + [pairs_header_row.get(i, '') for i in range(num_cols)],
               ['', ''] + [Robot.tokens[i] for i in range(num_cols)],
               ['', ''] + list(map(str, range(num_cols))),
             ] + [
               [Robot.tokens[i], str(i)] + Robot.matrix[i].tolist()
               for i in range(num_rows)
             ]


def make_table(data, header_rows: int, header_columns: int):
  table = Table(data)
  table.setStyle(TableStyle([
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('BACKGROUND', (0, header_rows), (-1, -1), colors.beige),
    ('GRID', (0, 0), (-1, -1), 1, colors.black),
    # row headers
    ('BACKGROUND', (0, 0), (-1, header_rows - 1), colors.grey),
    ('TEXTCOLOR', (0, 0), (-1, header_rows - 1), colors.whitesmoke),
    ('FONTNAME', (0, 0), (-1, header_rows - 1), 'Helvetica-Bold'),
    # column headers
    ('BACKGROUND', (0, header_rows), (header_columns - 1, -1), colors.lightblue),
    ('TEXTCOLOR', (0, header_rows), (header_columns - 1, -1), colors.black),
    ('FONTNAME', (0, header_rows), (header_columns - 1, -1), 'Helvetica-Bold'),
  ]))
  for row_idx in range(num_rows):
    for col_idx in range(num_cols):
      if Robot.matrix[row_idx, col_idx] != 0:
        table.setStyle(TableStyle([(
          'BACKGROUND',
          (col_idx + header_columns, row_idx + header_rows),
          (col_idx + header_columns, row_idx + header_rows),
          colors.lightgreen
        ), ]))
  return table


doc.build([
  Paragraph("Advent of Code 2024 - Day 21", getSampleStyleSheet()['Heading1']),
  make_table(table_data, 3, 2)
])

print(f"PDF '{pdf_filename}' created successfully!")
