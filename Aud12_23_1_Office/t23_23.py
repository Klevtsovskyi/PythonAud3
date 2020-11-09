

from docx import Document
from docx.shared import RGBColor


def change_colors(input, output, oldcolor, newcolor):
    doc = Document(input)

    r = int(newcolor[:2], 16)
    g = int(newcolor[2:4], 16)
    b = int(newcolor[4:], 16)

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            if str(run.font.color.rgb) == oldcolor:
                # print(run.text)
                run.font.color.rgb = RGBColor(r, g, b)

    doc.save(output)


if __name__ == '__main__':
    change_colors("input.docx", "output.docx", "FF0000", "FF00FF")
