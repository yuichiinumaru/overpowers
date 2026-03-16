import pyopenms as poms
import argparse

def analyze_mzml(mzml_file: str):
    """Load and explore an mzML file using pyopenms."""
    print(f"Loading {mzml_file}...")

    exp = poms.MSExperiment()

    try:
        poms.MzMLFile().load(mzml_file, exp)
        print(f"Loaded {exp.size()} spectra.")

        # Get basic statistics
        ms1_spectra = 0
        ms2_spectra = 0
        min_rt = float('inf')
        max_rt = 0

        for spec in exp:
            ms_level = spec.getMSLevel()
            if ms_level == 1:
                ms1_spectra += 1
            elif ms_level == 2:
                ms2_spectra += 1

            rt = spec.getRT()
            if rt < min_rt:
                min_rt = rt
            if rt > max_rt:
                max_rt = rt

        print(f"\nSummary:")
        print(f"MS1 Spectra: {ms1_spectra}")
        print(f"MS2 Spectra: {ms2_spectra}")
        print(f"Retention Time Range: {min_rt:.2f} to {max_rt:.2f} seconds")

        # Examine first spectrum
        if exp.size() > 0:
            first_spec = exp[0]
            print(f"\nFirst Spectrum:")
            print(f"  MS Level: {first_spec.getMSLevel()}")
            print(f"  Retention Time: {first_spec.getRT()}s")
            print(f"  Precursor m/z: {first_spec.getPrecursors()[0].getMZ() if first_spec.getPrecursors() else 'N/A'}")
            print(f"  Number of peaks: {first_spec.size()}")

        return True
    except Exception as e:
        print(f"Error analyzing {mzml_file}: {e}")
        return False

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Explore mzML files using pyopenms")
    parser.add_argument("mzml", help="Path to the mzML file")

    args = parser.parse_args()

    analyze_mzml(args.mzml)
