import matchms
from matchms.importing import load_from_mgf, load_from_msp
from matchms.filtering import default_filters, normalize_intensities, select_by_relative_intensity, require_minimum_number_of_peaks
from matchms import SpectrumProcessor
import os

def create_standard_processor():
    """Define a standard processing pipeline"""
    processor = SpectrumProcessor([
        default_filters,
        normalize_intensities,
        lambda s: select_by_relative_intensity(s, intensity_from=0.01),
        lambda s: require_minimum_number_of_peaks(s, n_required=5)
    ])
    return processor

def process_spectra_file(file_path):
    """Load and process spectra from a file"""
    if file_path.endswith(".mgf"):
        spectra = list(load_from_mgf(file_path))
    elif file_path.endswith(".msp"):
        spectra = list(load_from_msp(file_path))
    else:
        raise ValueError("Unsupported file format. Use .mgf or .msp")
        
    processor = create_standard_processor()
    processed_spectra = [processor(s) for s in spectra]
    # Filter out None results (where filters rejected the spectrum)
    processed_spectra = [s for s in processed_spectra if s is not None]
    
    print(f"Processed {len(processed_spectra)} spectra from {file_path}")
    return processed_spectra

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        try:
            processed = process_spectra_file(sys.argv[1])
            print(f"First spectrum peaks: {len(processed[0].peaks.mz)}")
        except Exception as e:
            print(f"Error: {e}")
    else:
        print("Usage: python matchms_process.py <path_to_spectra_file>")
