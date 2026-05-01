EXTRACT = {
    "folder_path": "Files/",
    "archive_folder": "Archived files/",
}

LOAD = {
    "engine": "mssql+pyodbc://WagnerProdAGL1/Targit_DM?driver=ODBC+Driver+17+for+SQL+Server",
    "tables": {
        "otil": "OTIL_History",
        "otif": "OTIF_History",
        "cmis": "CMIS_Grief",
    },
}

DATABASE = {
    "server": "WagnerProdAGL1",
    "database": "Targit_DM",
    "trustedConnection": "True",
}