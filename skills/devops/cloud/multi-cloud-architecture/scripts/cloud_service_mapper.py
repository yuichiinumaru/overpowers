import sys

SERVICES = {
    "compute_vms": {"aws": "EC2", "azure": "Virtual Machines", "gcp": "Compute Engine"},
    "containers": {"aws": "ECS", "azure": "Container Instances", "gcp": "Cloud Run"},
    "kubernetes": {"aws": "EKS", "azure": "AKS", "gcp": "GKE"},
    "serverless_functions": {"aws": "Lambda", "azure": "Functions", "gcp": "Cloud Functions"},
    "object_storage": {"aws": "S3", "azure": "Blob Storage", "gcp": "Cloud Storage"},
    "block_storage": {"aws": "EBS", "azure": "Managed Disks", "gcp": "Persistent Disk"},
    "file_storage": {"aws": "EFS", "azure": "Azure Files", "gcp": "Filestore"},
    "managed_sql": {"aws": "RDS", "azure": "SQL Database", "gcp": "Cloud SQL"},
    "nosql_document": {"aws": "DynamoDB", "azure": "Cosmos DB", "gcp": "Firestore"},
    "distributed_sql": {"aws": "Aurora", "azure": "PostgreSQL/MySQL", "gcp": "Cloud Spanner"},
    "caching": {"aws": "ElastiCache", "azure": "Azure Cache for Redis", "gcp": "Memorystore"},
}

def map_service(service_type):
    if service_type not in SERVICES:
        # Try finding by name
        found = False
        for s_type, cloud_map in SERVICES.items():
            for cloud, name in cloud_map.items():
                if service_type in name.lower() or service_type in cloud.lower():
                    print(f"Matches found in {s_type}:")
                    for c, n in cloud_map.items():
                        print(f"  {c.upper()}: {n}")
                    found = True
                    break
        if not found:
            print(f"Unknown service type: {service_type}. Available keys: {', '.join(SERVICES.keys())}")
        return
    
    mapping = SERVICES[service_type]
    print(f"--- Multi-Cloud Mapping for {service_type.replace('_', ' ').title()} ---")
    for cloud, service in mapping.items():
        print(f"{cloud.upper()}: {service}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python cloud_service_mapper.py <service_type_or_name>")
        print(f"Available type keys: {', '.join(SERVICES.keys())}")
    else:
        map_service(sys.argv[1].lower())
