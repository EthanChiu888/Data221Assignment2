import requests
from bs4 import BeautifulSoup
import csv

URL = "https://en.wikipedia.org/wiki/Machine_learning"

def clean_text(tag):
    """
    Takes a BeautifulSoup table cell (<td> or <th>) and returns its text
    with extra whitespace removed.
    """
    return "".join(tag.get_text(" ", strip=True).split())


def find_first_table_with_3_data_rows(content_div):
    """
    Searches through all tables inside the main content area and returns
    the first table that contains at least three data rows.
    A data row is defined as a table row (<tr>) that contains at least
    one data cell (<td>).
    """
    for table in content_div.find_all("table"):
        rows = table.find_all("tr")
        data_row_count = 0

        for row in rows:
            if row.find_all("td"):
                data_row_count += 1

        if data_row_count >= 3:
            return table

    return None


def extract_table(table):
    """
    Extracts headers and data rows from a table.

    If header cells (<th>) are present, they are used as column headers.
    Otherwise, default headers (col1, col2, ...) are created.

    Rows with missing columns are padded with empty strings so that
    all rows have the same number of columns.
    """
    rows = table.find_all("tr")

    extracted_rows = []
    max_columns = 0

    for row in rows:
        cells = row.find_all(["th", "td"])
        if not cells:
            continue

        row_data = [clean_text(cell) for cell in cells]
        extracted_rows.append(row_data)
        max_columns = max(max_columns, len(row_data))

    if not extracted_rows:
        return [], []

    header = None
    header_index = None

    for index, row in enumerate(rows):
        th_cells = row.find_all("th")
        td_cells = row.find_all("td")

        if th_cells and not td_cells:
            header = [clean_text(th) for th in th_cells]
            header_index = index
            break

    if header is None:
        header = [f"col{i}" for i in range(1, max_columns + 1)]

    if len(header) < max_columns:
        header += [""] * (max_columns - len(header))

    data_rows = []

    for index, row in enumerate(extracted_rows):
        if header_index is not None and index == header_index:
            continue

        if len(row) < max_columns:
            row += [""] * (max_columns - len(row))
        elif len(row) > max_columns:
            row = row[:max_columns]

        data_rows.append(row)

    return header, data_rows


def main():
    """
    Downloads the Wikipedia page, locates the main content area,
    finds the first valid table, extracts its data, and saves it
    to wiki_table.csv.
    """
    response = requests.get(URL, timeout=30)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    content_div = soup.find("div", id="mw-content-text")
    if content_div is None:
        raise RuntimeError("Main content area not found.")

    table = find_first_table_with_3_data_rows(content_div)
    if table is None:
        raise RuntimeError("No suitable table found.")

    header, data_rows = extract_table(table)

    with open("wiki_table.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data_rows)

    print("wiki_table.csv created successfully.")


if __name__ == "__main__":
    main()
