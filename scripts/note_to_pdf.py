from pathlib import Path
from textwrap import wrap
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def markdown_to_lines(md_text: str, width: int = 95):
    lines = []
    for raw_line in md_text.splitlines():
        line = raw_line.rstrip()
        if not line:
            lines.append('')
            continue
        if line.startswith('#'):
            heading = line.lstrip('#').strip()
            lines.append(heading.upper())
            lines.append('')
        elif line.startswith('* '):
            wrapped = wrap(line[2:], width - 2)
            if not wrapped:
                lines.append('•')
            else:
                lines.append('• ' + wrapped[0])
                for continuation in wrapped[1:]:
                    lines.append('  ' + continuation)
        elif line[0].isdigit() and line.lstrip().startswith(tuple(str(i) for i in range(10))):
            # basic handling for ordered lists like "1. text"
            parts = line.split('.', 1)
            if len(parts) == 2:
                prefix, rest = parts
                wrapped = wrap(rest.strip(), width - len(prefix) - 2)
                if wrapped:
                    lines.append(f"{prefix.strip()}. {wrapped[0]}")
                    for continuation in wrapped[1:]:
                        lines.append(' ' * (len(prefix) + 2) + continuation)
                else:
                    lines.append(prefix.strip() + '.')
            else:
                lines.append(line)
        else:
            for wrapped in wrap(line, width):
                lines.append(wrapped)
    return lines


def render_pdf(markdown_path: Path, output_path: Path):
    text = markdown_path.read_text(encoding='utf-8')
    lines = markdown_to_lines(text)

    c = canvas.Canvas(str(output_path), pagesize=letter)
    width, height = letter
    margin = 72  # 1 inch
    y = height - margin
    line_height = 16

    for line in lines:
        if y <= margin:
            c.showPage()
            y = height - margin
        if line == '':
            y -= line_height
            continue
        c.drawString(margin, y, line)
        y -= line_height

    c.save()


if __name__ == '__main__':
    render_pdf(Path('reports/yoruba_registry_note.md'), Path('reports/yoruba_registry_note.pdf'))
    print('Created reports/yoruba_registry_note.pdf')
