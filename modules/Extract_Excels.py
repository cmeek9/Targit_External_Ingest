import pandas as pd
import os


def find_sheet_containing_keyword(file_path, keyword):
    """Finds and returns the name of the sheet that contains the specified keyword."""
    with pd.ExcelFile(file_path) as xls:
        for sheet_name in xls.sheet_names:
            if keyword.lower() in sheet_name.lower():
                return sheet_name
    return None


def find_other_sheet(file_path, excluded_sheet_name):
    """Finds and returns the name of the sheet that does not contain the keyword."""
    with pd.ExcelFile(file_path) as xls:
        for sheet_name in xls.sheet_names:
            if sheet_name != excluded_sheet_name:
                return sheet_name
    return None


def load_excel_data(folder_path):
    df_otil_stage = pd.DataFrame()
    df_otif_stage = pd.DataFrame()
    df_CMIS_stage = pd.DataFrame()

    source_files = {
        "otil": None,
        "otif": None,
        "cmis": None,
    }

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)

            otil_sheet_name = find_sheet_containing_keyword(file_path, 'Line')
            if otil_sheet_name:
                df_otil_stage = pd.read_excel(file_path, sheet_name=otil_sheet_name)
                source_files["otil"] = file_path

            otif_sheet_name = find_sheet_containing_keyword(file_path, 'Order')
            if otif_sheet_name:
                df_otif_stage = pd.read_excel(file_path, sheet_name=otif_sheet_name, skiprows=1)
                source_files["otif"] = file_path

            if 'CMIS Grief' in file_name:
                sheet_name = find_sheet_containing_keyword(file_path, 'CMIS')
                if not sheet_name:
                    sheet_name = 'Sheet1'
                if sheet_name:
                    df_CMIS_stage = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=3)
                    source_files["cmis"] = file_path

    return df_otil_stage, df_otif_stage, df_CMIS_stage, source_files