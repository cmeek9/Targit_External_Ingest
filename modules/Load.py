import pandas as pd
from sqlalchemy import create_engine
from bcpandas import SqlCreds, to_sql
import bcpandas
import configparser


config = configparser.ConfigParser()
config.read('config.ini')


def create_engine_instance(engine):
    return create_engine(engine, echo=False, fast_executemany=True)



def load_otil_data(df_result, config):
    # Create SqlCreds object
    creds = SqlCreds(
        config['Server'],
        config['Database'],
        config['TrustedConnection']
    )
    
    # Use bcpandas to load data into SQL
    bcpandas.to_sql(df_result, 'OTIL', creds, index=False, if_exists='replace')
    
    return "Data loaded successfully"
    


def load_otif_data(df_result, engine):
    df_result.to_sql('OTIF', con=engine, index=False, if_exists='replace', schema='dbo', method = 'multi', chunksize=60)
    return "Data loaded successfully"


def load_CMIS_data(df_result, engine):
    df_result.to_sql('CMIS_Grief', con=engine, index=False, if_exists='replace', schema='dbo')
    return "Data loaded successfully"


# unless code perhaps
# def convert_df_to_sql(df, table_name, engine, schema='dbo', if_exists='replace', index=False):
#     dtype_mapping = {
#         'Dlr Cd Emer': VARCHAR,
#         'Y': INTEGER,
#         'Grand Total': INTEGER,
#         'Percentage': FLOAT,
#     }
    
#     df.to_sql(table_name, con=engine, index=index, if_exists=if_exists, schema=schema, dtype=dtype_mapping)

# def convert_CMIS_to_sql(df, engine):
#     df.to_sql('CMIS_Grief', con=engine, index=False, if_exists='replace', schema='dbo')


# def execute_sql_query(engine, sql_query):
#     try:
#         with engine.connect() as connection:
#             connection.execute(text(sql_query))
#             connection.commit()
#     except Exception as e:
#         print(f"Error executing SQL query: {str(e)}")