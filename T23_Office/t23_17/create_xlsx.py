import openpyxl


def create_xlsx(filename, *sheets):
    wb = openpyxl.Workbook()
    wb.remove(wb.active)

    for name, table in sheets:
        ws = wb.create_sheet(name)
        for row in table:
            ws.append(row)

    wb.save(filename)


if __name__ == "__main__":
    customers = (
        "customers", (
            ("id", "Name", "Address"),
            ("C01", "Доміно", "domino@com.ua"),
            ("C02", "Кондор", "condor@com.ua")
        )
    )

    products = (
        "products", (
            ("id", "Name", "Unit", "Price"),
            ("P01", "Олівець", "шт.", 2.5),
            ("P02", "Ручка кулькова", "шт.", 2.4)
        )
    )

    invoices = (
        "invoices", (
            ("id", "No", "Date", "Customer"),
            ("I01", 253, "18.07.2016", "C01"),
            ("I02", 255, "19.07.2016", "C02")
        )
    )

    items = (
        "items", (
            ("I_id", "P_id", "Quantity"),
            ("I01", "P01", 200),
            ("I01", "P02", 100)
        )
    )

    create_xlsx("data.xlsx", customers, products, invoices, items)
