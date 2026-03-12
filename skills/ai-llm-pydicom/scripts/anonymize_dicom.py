import sys
import pydicom
from datetime import datetime

def anonymize(input_path, output_path):
    try:
        ds = pydicom.dcmread(input_path)
        
        # Tags commonly containing PHI (Protected Health Information)
        tags_to_anonymize = [
            'PatientName', 'PatientID', 'PatientBirthDate',
            'PatientSex', 'PatientAge', 'PatientAddress',
            'InstitutionName', 'InstitutionAddress',
            'ReferringPhysicianName', 'PerformingPhysicianName',
            'OperatorsName', 'StudyDescription', 'SeriesDescription',
        ]

        # Remove or replace sensitive data
        for tag in tags_to_anonymize:
            if hasattr(ds, tag):
                if tag in ['PatientName', 'PatientID']:
                    setattr(ds, tag, 'ANONYMOUS')
                elif tag == 'PatientBirthDate':
                    setattr(ds, tag, '19000101')
                else:
                    delattr(ds, tag)

        # Update dates to maintain temporal relationships (simple version)
        if hasattr(ds, 'StudyDate'):
            ds.StudyDate = '20000101'

        ds.save_as(output_path)
        print(f"Anonymized DICOM saved to: {output_path}")
        
    except Exception as e:
        print(f"Error during anonymization: {e}")
        sys.exit(1)

def main():
    if len(sys.argv) < 3:
        print("Usage: python anonymize_dicom.py <input.dcm> <output.dcm>")
        sys.exit(1)
        
    anonymize(sys.argv[1], sys.argv[2])

if __name__ == "__main__":
    main()
