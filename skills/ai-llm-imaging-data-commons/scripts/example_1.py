from idc_index import IDCClient
client = IDCClient()

# Join index with collections_index to get cancer types
client.fetch_index("collections_index")
result = client.sql_query("""
    SELECT i.SeriesInstanceUID, i.Modality, c.CancerTypes, c.TumorLocations
    FROM index i
    JOIN collections_index c ON i.collection_id = c.collection_id
    WHERE i.Modality = 'MR'
    LIMIT 10
""")

# Join index with sm_index for slide microscopy details
client.fetch_index("sm_index")
result = client.sql_query("""
    SELECT i.collection_id, i.PatientID, s.ObjectiveLensPower, s.min_PixelSpacing_2sf
    FROM index i
    JOIN sm_index s ON i.SeriesInstanceUID = s.SeriesInstanceUID
    LIMIT 10
""")

# Join seg_index with index to find segmentations and their source images
client.fetch_index("seg_index")
result = client.sql_query("""
    SELECT
        s.SeriesInstanceUID as seg_series,
        s.AlgorithmName,
        s.total_segments,
        src.collection_id,
        src.Modality as source_modality,
        src.BodyPartExamined
    FROM seg_index s
    JOIN index src ON s.segmented_SeriesInstanceUID = src.SeriesInstanceUID
    WHERE s.AlgorithmType = 'AUTOMATIC'
    LIMIT 10
""")
