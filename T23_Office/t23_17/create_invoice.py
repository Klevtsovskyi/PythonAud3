import openpyxl
from docx import Document
import re


INVOICE = r"(Рахунок\s+?№\s+?)(_+)\b"
DATE = r"(Дата:?\s+?)(__.__.____)\b"
CUSTOMER = r"(Покупець:?\s+?)(_+)\b"
TOTAL = r"(Всього:?\s+?)(_+)\b"

rgxINVOICE = re.compile(INVOICE)
rgxDATE = re.compile(DATE)
rgxCUSTOMER = re.compile(CUSTOMER)
rgxTOTAL = re.compile(TOTAL)


def create_invoice(invoice_no, data, template):
    wb = openpyxl.load_workbook(data)

    ws = wb["invoices"]
    for row in ws.rows:
        if row[1].value == invoice_no:
            invoice_id, no, date, customer_id = [c.value for c in row]
            # print(invoice_id, no, date, customer_id)
            break
    else:
        return

    ws = wb["customers"]
    for row in ws.rows:
        if row[0].value == customer_id:
            customer_id, customer_name, address = [c.value for c in row]
            # print(customer_id, customer_name, address)
            break
    else:
        return

    products = {}
    ws = wb["items"]
    for row in ws.rows:
        if row[0].value == invoice_id:
            invoice_id, product_id, quantity = [c.value for c in row]
            # print(invoice_id, product_id, quantity)
            products[product_id] = {"quantity": quantity}

    # print(products)

    ws = wb["products"]
    for row in ws.rows:
        product_id = row[0].value
        if product_id in products:
            product_id, name, unit, price = [c.value for c in row]
            # print(product_id, name, unit, price)
            products[product_id]["name"] = name
            products[product_id]["unit"] = unit
            products[product_id]["price"] = price

    # print(products)

    doc = Document(template)

    total = 0
    table = doc.tables[0]
    for i, product in enumerate(products, 1):
        full_price = (
            float(products[product]["quantity"]) *
            float(products[product]["price"])
        )
        total += full_price
        values = (
            i,
            products[product]["name"],
            products[product]["unit"],
            products[product]["quantity"],
            products[product]["price"],
            full_price
        )
        row = table.add_row()
        for cell, value in zip(row.cells, values):
            cell.text = str(value)

    def substitute_invoice_no(match):
        count = match.group(2).count("_")
        s = "{:_>%d}" % count
        return match.group(1) + s.format(invoice_no)

    def substitute_date(match):
        return match.group(1) + str(date)

    def substitute_customer(match):
        return match.group(1) + customer_name + " " + address

    def substitute_total(match):
        return match.group(1) + str(total)

    for paragraph in doc.paragraphs:
        for run in paragraph.runs:
            run.text = re.sub(INVOICE, substitute_invoice_no, run.text)
            run.text = re.sub(DATE, substitute_date, run.text)
            run.text = re.sub(CUSTOMER, substitute_customer, run.text)
            run.text = re.sub(TOTAL, substitute_total, run.text)

    doc.save(f"invoice_{customer_name}_{''.join(date.split('.'))}.docx")


if __name__ == "__main__":
    create_invoice(253, "data.xlsx", "template.docx")
