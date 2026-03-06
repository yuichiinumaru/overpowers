# Find breast MRI scans (use actual values from exploration above)
results = client.sql_query("""
    SELECT
      collection_id,
      PatientID,
      SeriesInstanceUID,
      Modality,
      SeriesDescription,
      license_short_name
    FROM index
    WHERE Modality = 'MR'
      AND BodyPartExamined = 'BREAST'
    LIMIT 20
""")

# Access results as pandas DataFrame
for idx, row in results.iterrows():
    print(f"Patient: {row['PatientID']}, Series: {row['SeriesInstanceUID']}")
