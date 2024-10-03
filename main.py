from modules import Extract_Excels, Transform, Load
import configparser

def main():
    # Load configuration from config.ini
    config = configparser.ConfigParser()
    config.read('config.ini')

    # Extract OTIL, OTIF, and CMIS
    df_OTIL_Stage, df_OTIF_Stage, df_CMIS_Stage = Extract_Excels.load_excel_data(config['EXTRACT']['FolderPath'])

    # Transform and Load OTIL if data is present
    if not df_OTIL_Stage.empty:
        df_result_otil = Transform.transform_otil_data(df_OTIL_Stage)
        Load.load_otil_data(df_result_otil, config['DATABASE'])

    # Transform and Load OTIF if data is present
    if not df_OTIF_Stage.empty:
        df_result_otif = Transform.transform_otif_data(df_OTIF_Stage)
        Load.load_otif_data(df_result_otif, config['LOAD']['engine'])

    # Transform and Load CMIS if data is present
    if not df_CMIS_Stage.empty:
        df_result_cmis = Transform.transform_CMIS_data(df_CMIS_Stage)
        Load.load_CMIS_data(df_result_cmis, config['LOAD']['engine'])

if __name__ == "__main__":
    main()
