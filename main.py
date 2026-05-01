from modules import Extract_Excels, Transform, Load, MoveToArchive
from config import EXTRACT, LOAD, DATABASE


def main():
    df_OTIL_Stage, df_OTIF_Stage, df_CMIS_Stage, source_files = Extract_Excels.load_excel_data(
        EXTRACT["folder_path"]
    )

    if not df_OTIL_Stage.empty:
        df_result_otil = Transform.transform_otil_data(df_OTIL_Stage)
        otil_status = Load.load_otil_data(df_result_otil, DATABASE, LOAD["tables"]["otil"])
        if otil_status == "Data loaded successfully":
            MoveToArchive.move_file_to_archive(source_files["otil"], EXTRACT["archive_folder"])

    if not df_OTIF_Stage.empty:
        df_result_otif = Transform.transform_otif_data(df_OTIF_Stage)
        otif_status = Load.load_otif_data(df_result_otif, LOAD["engine"], LOAD["tables"]["otif"])
        if otif_status == "Data loaded successfully":
            MoveToArchive.move_file_to_archive(source_files["otif"], EXTRACT["archive_folder"])

    if not df_CMIS_Stage.empty:
        df_result_cmis = Transform.transform_CMIS_data(df_CMIS_Stage)
        cmis_status = Load.load_CMIS_data(df_result_cmis, LOAD["engine"], LOAD["tables"]["cmis"])
        if cmis_status == "Data loaded successfully":
            MoveToArchive.move_file_to_archive(source_files["cmis"], EXTRACT["archive_folder"])


if __name__ == "__main__":
    main()
