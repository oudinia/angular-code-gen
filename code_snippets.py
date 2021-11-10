def get_form_control(c: str) -> str:
    control = f"""<div class="row">
                       <mat-form-field appearance="fill">
                       <mat-label>{c}</mat-label>
                       <input matInput formControlName="{c}">
                       </mat-form-field>
                       </div>"""
    return control


def get_form_control_def(c: str) -> str:
    control_def = f"{c}: ['', [Validators.required]],\n"
    return control_def


def get_form_group_def():
    form_builder = "this.mainFormGroup = this.fb.group({\n"
    return form_builder


def get_ngfor(entity_name: str):
    ngfor = f"<tr *ngFor='let e of {entity_name} | async'>\n"
    return ngfor


def get_column_cell(c):
    data_cell = "<td>{{e." + c + "}}</td>\n"
    return data_cell


def get_column_header(c):
    column_header = f"<th scope='col'>{c}</th>"
    return column_header


def get_table_header():
    table_header = "<table class='table'><thead><tr>"
    return table_header


def get_table_header_end():
    return "</tr></thead>"


def get_data_cell(c, df):
    data_cell = f"<td>{df[c][ind]}</td>"
    return data_cell
