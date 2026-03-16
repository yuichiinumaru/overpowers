# Find ALL segmentations and structure sets by DICOM Modality
# SEG = DICOM Segmentation, RTSTRUCT = Radiotherapy Structure Set
client.sql_query("""
    SELECT collection_id, Modality, COUNT(*) as series_count
    FROM index
    WHERE Modality IN ('SEG', 'RTSTRUCT')
    GROUP BY collection_id, Modality
    ORDER BY series_count DESC
""")

# Find segmentations for a specific collection (includes non-analysis-result items)
client.sql_query("""
    SELECT SeriesInstanceUID, SeriesDescription, analysis_result_id
    FROM index
    WHERE collection_id = 'tcga_luad' AND Modality = 'SEG'
""")

# List analysis result collections (curated derived datasets)
client.fetch_index("analysis_results_index")
client.sql_query("""
    SELECT analysis_result_id, analysis_result_title, Collections, Modalities
    FROM analysis_results_index
""")

# Find analysis results for a specific source collection
client.sql_query("""
    SELECT analysis_result_id, analysis_result_title
    FROM analysis_results_index
    WHERE Collections LIKE '%tcga_luad%'
""")

# Use seg_index for detailed DICOM Segmentation metadata
client.fetch_index("seg_index")

# Get segmentation statistics by algorithm
client.sql_query("""
    SELECT AlgorithmName, AlgorithmType, COUNT(*) as seg_count
    FROM seg_index
    WHERE AlgorithmName IS NOT NULL
    GROUP BY AlgorithmName, AlgorithmType
    ORDER BY seg_count DESC
    LIMIT 10
""")

# Find segmentations for specific source images (e.g., chest CT)
client.sql_query("""
    SELECT
        s.SeriesInstanceUID as seg_series,
        s.AlgorithmName,
        s.total_segments,
        s.segmented_SeriesInstanceUID as source_series
    FROM seg_index s
    JOIN index src ON s.segmented_SeriesInstanceUID = src.SeriesInstanceUID
    WHERE src.Modality = 'CT' AND src.BodyPartExamined = 'CHEST'
    LIMIT 10
""")

# Find TotalSegmentator results with source image context
client.sql_query("""
    SELECT
        seg_info.collection_id,
        COUNT(DISTINCT s.SeriesInstanceUID) as seg_count,
        SUM(s.total_segments) as total_segments
    FROM seg_index s
    JOIN index seg_info ON s.SeriesInstanceUID = seg_info.SeriesInstanceUID
    WHERE s.AlgorithmName LIKE '%TotalSegmentator%'
    GROUP BY seg_info.collection_id
    ORDER BY seg_count DESC
""")
