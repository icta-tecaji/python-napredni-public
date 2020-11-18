import os
from typing import List

import docx
import pandas as pd
import typer


app = typer.Typer()


def read_docx_table_to_list(document_path: str) -> List:
    doc = docx.Document(document_path)
    tables = doc.tables
    final_tables = []
    for table in tables:
        data = []
        keys = None
        for i, row in enumerate(table.rows):
            text = (cell.text for cell in row.cells)
            if i == 0:
                keys = tuple(text)
                continue
            row_data = dict(zip(keys, text))
            data.append(row_data)
        final_tables.append(data)
    return final_tables


def read_docx_table_to_df(document_path: str) -> List[pd.DataFrame]:
    tables = read_docx_table_to_list(document_path)
    tables_df = [pd.DataFrame.from_dict(table) for table in tables]
    return tables_df


def convert_docx_tables_to_xlsx_simple(document_path: str, output_folder: str):
    tables = read_docx_table_to_df(document_path)
    for count, table in enumerate(tables):
        if not output_folder:
            converted_file_name = (
                f"{os.path.splitext(document_path)[0]}-table-{count}.xlsx"
            )
        else:
            try:
                os.makedirs(output_folder)
            except FileExistsError:
                pass
            converted_file_name = f"{output_folder}/{os.path.splitext(document_path)[0].split('/')[-1]}-table-{count}.xlsx"
            print(converted_file_name)
        typer.echo(f"Converting file {converted_file_name}...")
        table.to_excel(converted_file_name)


@app.command()
def remove_tables(path: str):
    pass


@app.command()
def convert(
    docx_file_path: str,
    output_folder: str = "",
    complex_table: bool = False,
):
    """
    Convert all tables from docx document to excel tables.

    If --complex-table is used, the script will pares a teble in complex mode.
    """

    if complex_table:
        typer.secho("Not implemented", fg=typer.colors.YELLOW, bold=True)

    else:
        typer.echo(f"Converting file {docx_file_path}...")
        convert_docx_tables_to_xlsx_simple(docx_file_path, output_folder)
        typer.secho("Completed.", fg=typer.colors.GREEN, bold=True)


if __name__ == "__main__":
    app()
