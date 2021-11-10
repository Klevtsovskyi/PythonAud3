from docx import Document
import re


DATE1 = r"\b\d{1,4}/\d{1,2}/\d{1,2}"  # 1999/3/12
DATE2 = r"\b\d{1,2}\.\d{1,2}\.\d{1,4}"  # 12.3.1999
DATE = DATE1 + "|" + DATE2


def _change_date(match):
    date = match.group()
    if "/" in date:
        y, m, d = date.split("/")
    else:
        d, m, y = date.split(".")
    while len(y) != 4:
        y = "0" + y
    if len(m) != 2:
        m = "0" + m
    if len(d) != 2:
        d = "0" + d
    date = ".".join((d, m, y))
    return date


def change_dates(string):
    return re.sub(DATE, _change_date, string)


def change_dates_docx(inp, out):
    doc = Document(inp)

    for paragraph in doc.paragraphs:
        paragraph.text = change_dates(paragraph.text)

    doc.save(out)


if __name__ == "__main__":
    change_dates_docx("input.docx", "output.docx")
