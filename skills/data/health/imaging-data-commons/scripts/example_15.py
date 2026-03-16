# Simplified hierarchy (omit StudyInstanceUID level)
client.download_from_selection(
    collection_id="tcga_luad",
    downloadDir="./data",
    dirTemplate="%collection_id/%PatientID/%Modality"
)
# Results in: ./data/tcga_luad/TCGA-05-4244/CT/

# Flat structure (all files in one directory)
client.download_from_selection(
    seriesInstanceUID=list(series_df['SeriesInstanceUID'].values),
    downloadDir="./data/flat",
    dirTemplate=""
)
# Results in: ./data/flat/*.dcm
