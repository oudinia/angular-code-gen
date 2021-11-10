# This is a sample Python script.
import pandas as pd
import generate_html_form
import generate_table


def generate():
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_json('data/employees.json')

    generate_table.generate_table_header(df)

    generate_table.generate_form(df)

    # gen_table.generate_content(df)

    generate_html_form.generate_html_form(df)


if __name__ == '__main__':
    generate()
