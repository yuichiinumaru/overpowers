import dxpy

def run_upload_and_analyze(file_path, project_id, applet_id):
    # Upload input file
    print(f"Uploading {file_path} to project {project_id}...")
    input_file = dxpy.upload_local_file(file_path, project=project_id)

    # Run analysis
    print(f"Running applet {applet_id}...")
    job = dxpy.DXApplet(applet_id).run({
        "reads": dxpy.dxlink(input_file.get_id())
    })

    # Wait for completion
    print("Waiting for job to complete...")
    job.wait_on_done()

    # Download results
    output_id = job.describe()["output"]["aligned_reads"]["$dnanexus_link"]
    print(f"Downloading results to aligned.bam...")
    dxpy.download_dxfile(output_id, "aligned.bam")
    print("Done!")

if __name__ == "__main__":
    # Example usage (commented out)
    # run_upload_and_analyze("sample.fastq", "project-xxxx", "applet-xxxx")
    pass
