import pandas as pd
import code_snippets as code


def generate_table_header(df: pd.DataFrame):
    entity_name = "employees"
    html_header = code.get_table_header()
    row_header = code.get_ngfor(entity_name)
    html = ''
    table_body = ''
    header_cols = []
    for c in df.columns:
        html = html + code.get_column_header(c)
    header_cols.append(html)
    html_header_end = code.get_table_header_end()
    print(f"{html_header}{','.join(header_cols)}{html_header_end}")

    for c in df.columns:
        table_body = table_body + code.get_column_cell(c)
    print(row_header + table_body + "</tr>")


def generate_form(df: pd.DataFrame):
    form_controls = []
    form = code.get_form_group_def()
    end_form = "});"
    for c in df.columns:
        form_control = code.get_form_control_def(c)
        form_controls.append(form_control)
    for fc in form_controls:
        form = form + fc
    form = form + end_form
    print(form)


def generate_content(df: pd.DataFrame):
    # read_df_data(df)
    row_data = ''
    end_row = '</tr>'
    row = '<tr>'
    rows = []
    for ind in df.index:
        for c in df.columns:
            row_data = row_data + code.get_data_cell(c, df)
        rows.append(f"{row}{row_data}{end_row}")
        row_data = ''
    print(','.join(rows))
