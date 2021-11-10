import pandas as pd
import code_snippets as code


def generate_html_form(df: pd.DataFrame):
    form_inputs = []
    for c in df.columns:
        html = code.get_form_control(c)
        form_inputs.append(html)
    print("\n".join(form_inputs))
