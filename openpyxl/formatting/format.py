from openpyxl.styles import Font, colors, Color, Alignment, PatternFill, GradientFill, Border, Side
from openpyxl.styles import NamedStyle
from openpyxl.workbook import Workbook

wb = Workbook()
ws = wb.active

# From row 1 to 20: Write 0 to 299
for i in range(1,7):
    ws.append(range(3))

ws.merge_cells(start_row=2, start_column=2, end_row=5, end_column=5)

#Upper leftmost cell of the merge.
cell = ws['B2']
cell.font = Font(color=colors.BLUE, size=20, italic=True)
cell.value = 'God has a path for me.'
cell.alignment = Alignment(horizontal='right', vertical='bottom')
cell.fill = GradientFill(stop=("F9FF09","FFFFFF"))
wb.save('test.xlsx')

# Try a named style
highlight = NamedStyle(name='highlight')
highlight.font = Font(bold=True)
# border styling
bd = Side(style='thick', color='000000')
highlight.border= Border(left=bd, right=bd, top=bd, bottom=bd)
highlight.fill = PatternFill('solid', fgColor='FFFF00')

# apply the highlighting
count = 0
for col in ws.iter_cols(min_col=4, min_row=1, max_col=10, max_row=10):
    col[count].style = highlight
    count = count + 1
wb.save('highlight.xlsx')