import pandas as pd
from sqlalchemy import create_engine
from bcpandas import SqlCreds, to_sql
import bcpandas


def create_engine_instance(engine):
    return create_engine(engine, echo=False, fast_executemany=True)


def load_otil_data(df_result, config, table_name):
    print("Starting OTIL data load...")
    try:
        creds = SqlCreds(
            config['server'],
            config['database'],
            config['trustedConnection']
        )
        print("Created SQL credentials for OTIL.")
        print(f"DataFrame shape: {df_result.shape}")
        bcpandas.to_sql(df_result, table_name, creds, index=False, if_exists='append')
        print("OTIL data loaded successfully.")
        return "Data loaded successfully"
    except Exception as e:
        print(f"Error loading OTIL data: {e}")
        return "Data load failed"


def load_otif_data(df_result, engine, table_name):
    print("Starting OTIF data load...")
    try:
        print(f"DataFrame shape: {df_result.shape}")
        df_result.to_sql(table_name, con=engine, index=False, if_exists='append', schema='dbo', method='multi', chunksize=60)
        print("OTIF data loaded successfully.")
        return "Data loaded successfully"
    except Exception as e:
        print(f"Error loading OTIF data: {e}")
        return "Data load failed"


def load_CMIS_data(df_result, engine, table_name):
    print("Starting CMIS data load...")
    try:
        print(f"DataFrame shape: {df_result.shape}")
        df_result.to_sql(table_name, con=engine, index=False, if_exists='replace', schema='dbo')
        print("CMIS data loaded successfully.")
        return "Data loaded successfully"
    except Exception as e:
        print(f"Error loading CMIS data: {e}")
        return "Data load failed"