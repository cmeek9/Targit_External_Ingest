import pandas as pd
import os


 
def find_sheet_containing_keyword(file_path, keyword):
    """Finds and returns the name of the sheet that contains the specified keyword."""
    with pd.ExcelFile(file_path) as xls:
        for sheet_name in xls.sheet_names:
            if keyword.lower() in sheet_name.lower():
                return sheet_name
    return None


# would only need if the naming convention is going to change, it seems CAT keeps changing their naming convention
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

    for file_name in os.listdir(folder_path):
        if file_name.endswith('.xlsx'):
            file_path = os.path.join(folder_path, file_name)

            # Check for 'OTIL' keyword
            otil_sheet_name = find_sheet_containing_keyword(file_path, 'OTIL')
            if otil_sheet_name:
                other_sheet_name = find_other_sheet(file_path, otil_sheet_name)
                if other_sheet_name:
                    df_otil_stage = pd.read_excel(file_path, sheet_name=other_sheet_name)

            # Check for 'OTIF' keyword
            otif_sheet_name = find_sheet_containing_keyword(file_path, 'OTIF')
            if otif_sheet_name:
                other_sheet_name = find_other_sheet(file_path, otif_sheet_name)
                if other_sheet_name:
                    df_otif_stage = pd.read_excel(file_path, sheet_name=other_sheet_name)

            # CMIS Grief part remains unchanged
            if 'CMIS Grief' in file_name:
                sheet_name = find_sheet_containing_keyword(file_path, 'CMIS Grief')
                if sheet_name:
                    df_CMIS_stage = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=3)

    return df_otil_stage, df_otif_stage, df_CMIS_stage



## use this if you need to go back currently the key word is in the tab we don't need, but it might change.
 
# def load_excel_data(folder_path):
#     df_otil_stage = pd.DataFrame()
#     df_otif_stage = pd.DataFrame()
#     df_CMIS_stage = pd.DataFrame()
 
#     for file_name in os.listdir(folder_path):
#         if file_name.endswith('.xlsx'):
#             if 'CCPA Line Detail' in file_name:
#                 sheet_name = find_sheet_containing_keyword(os.path.join(folder_path, file_name), 'CCPA Line Detail')
#                 if sheet_name:
#                     df_otil_stage = pd.read_excel(os.path.join(folder_path, file_name), sheet_name=sheet_name)
#             elif 'CCPA Order Detail' in file_name:
#                 sheet_name = find_sheet_containing_keyword(os.path.join(folder_path, file_name), 'CCPA Order Detail')
#                 if sheet_name:
#                     df_otif_stage = pd.read_excel(os.path.join(folder_path, file_name), sheet_name=sheet_name)
#             elif 'CMIS Grief' in file_name:
#                 sheet_name = find_sheet_containing_keyword(os.path.join(folder_path, file_name), 'CMIS Grief')
#                 if sheet_name:
#                     df_CMIS_stage = pd.read_excel(os.path.join(folder_path, file_name), sheet_name=sheet_name, skiprows=3)
 
#     return df_otil_stage, df_otif_stage, df_CMIS_stage