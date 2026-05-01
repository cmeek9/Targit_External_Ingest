import pandas as pd
import re

def to_pascal_case(s):
    s = re.sub(r'[^a-zA-Z0-9 ]', '', s)  # Remove non-alphanumeric except space
    parts = s.strip().split()
    return ''.join(word.capitalize() for word in parts) if parts else ''

def pascal_case_columns(df):
    df.columns = [to_pascal_case(col.replace('_', ' ')) for col in df.columns]
    return df

def transform_otif_data(df_otif_stage):
    print("Starting OTIF transform...")
    print("Original columns:", df_otif_stage.columns.tolist())
    
    #Rename columns to match the target schema
    df_otif_stage = df_otif_stage.rename(columns=lambda col: str(col).strip())
    column_map = {
        'Report Date': 'Rpt Dt',
        'Main Dealer Cd': 'Main Dlr Cd',
        'Inventory Store': 'Inv Str No',
        'Document Store': 'Str No',
        'Sales Channel': 'Sls Chan',
        'End Customer Number': 'End Cust No',
        'End Customer Name': 'End Cust Nm',
        'End Customer Order': 'End Cust Ord No',
        'Order Entry Date': 'Ord Ent Dt',
        'Customer Need By Date': 'Cust Reqd By Dt',
        'Order Complete Fill Date': 'Ord Cmplt Fill Dt',
        'Order Available for Delivery Date': 'Ord Del Avl Dt',
        'Days To Fill': 'Days To Fill',
        'OTIF Indicator': 'Otif Ind',
        'Cost Center': 'Cost Center',
    }
    df_otif_stage = df_otif_stage.rename(columns=column_map)

    df_otif_stage = pascal_case_columns(df_otif_stage)
    print("After PascalCase columns:", df_otif_stage.columns.tolist())

    # Pad invStrNo and strNo with leading zeros if single digit
    if 'InvStrNo' in df_otif_stage.columns:
        df_otif_stage['InvStrNo'] = df_otif_stage['InvStrNo'].astype(str).str.zfill(2)
        print("Padded InvStrNo")
    if 'StrNo' in df_otif_stage.columns:
        df_otif_stage['StrNo'] = df_otif_stage['StrNo'].astype(str).str.zfill(2)
        print("Padded StrNo")

    columns_to_keep = [
        'CostCenter',
        'CostReqdByDt',
        'CustReqdByDt',
        'DaysToFill',
        'EndCustNm',
        'EndCustNo',
        'EndCustOrdNo',
        'InvStrNo',
        'MainDlrCd',
        'OrdCmpltFillDt',
        'OrdCmpltFillInd',
        'OrdDelAvlDt',
        'OrdDelAvlInd',
        'OrdEntDt',
        'OtifInd',
        'RptDt',
        'SlsChan',
        'StrNo',
        'Otif',
        'OtifY'
    ]
    print("Columns to keep:", columns_to_keep)
    df_otif_stage = df_otif_stage[[col for col in columns_to_keep if col in df_otif_stage.columns]]
    print("Columns after filtering:", df_otif_stage.columns.tolist())
    print("DataFrame shape after filtering:", df_otif_stage.shape)

    df_result = df_otif_stage

    if 'DlrCdEmer' in df_result.columns:
        df_result['DlrCdEmer'] = df_result['DlrCdEmer'].astype(str)
        print("Converted DlrCdEmer to string")

    print("Finished OTIF transform.\n")
    return df_result

def transform_otil_data(df_otil_stage):
    print("Starting OTIL transform...")
    print("Original columns:", df_otil_stage.columns.tolist())
    df_otil_stage = pascal_case_columns(df_otil_stage)
    print("After camelCase columns:", df_otil_stage.columns.tolist())

    # Pad srcFac, documentStore, inventoryStore with leading zeros if single digit
    for col in ['srcFac', 'documentStore', 'inventoryStore']:
        if col in df_otil_stage.columns:
            df_otil_stage[col] = df_otil_stage[col].astype(str).str.zfill(2)
            print(f"Padded {col}")

    columns_to_keep = [
        'OtilLines',
        'Otil',
        'Lines',
        'CustReqdByDt',
        'DaysToFillSp',
        'EndCustNm',
        'EndCustNo',
        'EndCustOrdNo',
        'EquipmentManufacturer',
        'EquipmentModel',
        'EquipmentSerial',
        'InventoryStore',
        'OrdEntDt',
        'OrdQty',
        'PartDesc',
        'PartNumber',
        'ReportDt',
        'SalesChannel',
        'SourcedPart',
        'SrcFac',
        'StockingInd',
        'Pso'
    ]
    print("Columns to keep:", columns_to_keep)
    df_otil_stage = df_otil_stage[[col for col in columns_to_keep if col in df_otil_stage.columns]]
    print("Columns after filtering:", df_otil_stage.columns.tolist())
    print("DataFrame shape after filtering:", df_otil_stage.shape)

    df_result = df_otil_stage

    if 'dlrCdEmer' in df_result.columns:
        df_result['dlrCdEmer'] = df_result['dlrCdEmer'].astype(str)
        print("Converted dlrCdEmer to string")

    print("Finished OTIL transform.\n")
    return df_result

def transform_CMIS_data(df_CMIS_stage):
    df_CMIS_stage = pascal_case_columns(df_CMIS_stage)

    # Rename store to storeNumber if present
    if 'store' in df_CMIS_stage.columns:
        df_CMIS_stage.rename(columns={'store': 'storeNumber'}, inplace=True)

    # Pad storeNumber with leading zeros if single digit
    if 'storeNumber' in df_CMIS_stage.columns:
        df_CMIS_stage['storeNumber'] = df_CMIS_stage['storeNumber'].astype(str).str.zfill(2)

    df_result = df_CMIS_stage

    return df_result