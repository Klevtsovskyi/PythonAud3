from docx import Document
import os
import re


PARAGRAPH = r".*({}).*"


def find_paragraphs(directory, subrgx):
    pattern = PARAGRAPH.format(subrgx)
    rgx = re.compile(pattern, flags=re.DOTALL | re.IGNORECASE)

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".docx"):
                path = os.path.join(root, file)
                doc = Document(path)
                for i, paragraph in enumerate(doc.paragraphs, 1):
                    m = rgx.match(paragraph.text)
                    if m is not None:
                        print(path, i, paragraph.text)


if __name__ == "__main__":
    subrgx = input("Введіть регулярний вираз: ")
    find_paragraphs("phil", subrgx)
