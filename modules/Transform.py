import pandas as pd


def transform_otif_data(df_otif_stage):
    # replace sapces with underscores in the columns
    df_otif_stage.columns = df_otif_stage.columns.str.replace(' ','_')

    df_otif_stage['Inv_Str_No'] = df_otif_stage['Inv_Str_No'].astype(str).str.zfill(2)
    df_otif_stage['Str_No'] = df_otif_stage['Str_No'].astype(str).str.zfill(2)

    df_result = df_otif_stage

    # Convert 'Dlr_Cd_Emer' to string explicitly
    df_result['Dlr_Cd_Emer'] = df_result['Dlr_Cd_Emer'].astype(str)

    return df_result


def transform_otil_data(df_otil_stage):
    # replace sapces with underscores in the columns
    df_otil_stage.columns = df_otil_stage.columns.str.replace(' ','_')

    # Pad Store_Number with leading zeros if single digit
    df_otil_stage['Src_Fac'] = df_otil_stage['Src_Fac'].astype(str).str.zfill(2)
    df_otil_stage['Document_Store'] = df_otil_stage['Document_Store'].astype(str).str.zfill(2)
    df_otil_stage['Inventory_Store'] = df_otil_stage['Inventory_Store'].astype(str).str.zfill(2)


    df_result = df_otil_stage

    # Convert 'Dlr_Cd_Emer' to string explicitly
    df_result['Dlr_Cd_Emer'] = df_result['Dlr_Cd_Emer'].astype(str)

    return df_result


def transform_CMIS_data(df_CMIS_stage):
    # replace sapces with underscores in the columns
    df_CMIS_stage.columns = df_CMIS_stage.columns.str.replace(' ','_')

    # Rename column 'Store' to 'Store_Number'
    df_CMIS_stage.rename(columns={'Store': 'Store_Number'}, inplace=True)

    # Pad Store_Number with leading zeros if single digit
    df_CMIS_stage['Store_Number'] = df_CMIS_stage['Store_Number'].astype(str).str.zfill(2)

    df_result = df_CMIS_stage
    
    return df_result