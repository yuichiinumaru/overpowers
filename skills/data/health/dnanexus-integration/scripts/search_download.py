import dxpy

def run_search_and_download(project_id, file_pattern, property_dict):
    print(f"Searching for {file_pattern} in project {project_id}...")
    files = dxpy.find_data_objects(
        classname="file",
        name=file_pattern,
        properties=property_dict,
        project=project_id
    )

    count = 0
    for file_result in files:
        file_obj = dxpy.DXFile(file_result["id"])
        filename = file_obj.describe()["name"]
        print(f"Downloading {filename}...")
        dxpy.download_dxfile(file_result["id"], filename)
        count += 1

    print(f"Downloaded {count} files.")

if __name__ == "__main__":
    # Example usage (commented out)
    # run_search_and_download("project-xxxx", "*.bam", {"experiment": "exp001"})
    pass
