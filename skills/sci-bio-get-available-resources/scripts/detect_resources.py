import os
import sys
import json
import platform
import subprocess
import datetime
from pathlib import Path

try:
    import psutil
except ImportError:
    print("Error: psutil is required. Install with: pip install psutil")
    sys.exit(1)

def get_cpu_info():
    return {
        "physical_cores": psutil.cpu_count(logical=False),
        "logical_cores": psutil.cpu_count(logical=True),
        "architecture": platform.machine()
    }

def get_memory_info():
    mem = psutil.virtual_memory()
    return {
        "total_gb": round(mem.total / (1024 ** 3), 2),
        "available_gb": round(mem.available / (1024 ** 3), 2),
        "percent_used": mem.percent
    }

def get_disk_info():
    disk = psutil.disk_usage(os.getcwd())
    return {
        "total_gb": round(disk.total / (1024 ** 3), 2),
        "available_gb": round(disk.free / (1024 ** 3), 2),
        "percent_used": disk.percent
    }

def get_gpu_info():
    gpu_info = {
        "nvidia_gpus": [],
        "amd_gpus": [],
        "apple_silicon": None,
        "total_gpus": 0,
        "available_backends": []
    }

    # Check NVIDIA
    try:
        result = subprocess.run(['nvidia-smi', '--query-gpu=name,memory.total', '--format=csv,noheader'], 
                                capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            for line in result.stdout.strip().split('\n'):
                parts = line.split(',')
                gpu_info["nvidia_gpus"].append({
                    "name": parts[0].strip(),
                    "vram": parts[1].strip() if len(parts) > 1 else "Unknown"
                })
            gpu_info["available_backends"].append("CUDA")
            gpu_info["total_gpus"] += len(gpu_info["nvidia_gpus"])
    except FileNotFoundError:
        pass

    # Check AMD
    try:
        result = subprocess.run(['rocm-smi', '--showproductname'], capture_output=True, text=True)
        if result.returncode == 0 and result.stdout.strip():
            # Simplistic parsing for rocm-smi
            lines = [l for l in result.stdout.split('\n') if 'GPU' in l and 'Name' in l]
            for line in lines:
                gpu_info["amd_gpus"].append({"name": line.strip()})
            if lines:
                gpu_info["available_backends"].append("ROCm")
                gpu_info["total_gpus"] += len(lines)
    except FileNotFoundError:
        pass

    # Check Apple Silicon
    if platform.system() == "Darwin" and platform.machine() == "arm64":
        gpu_info["apple_silicon"] = {
            "name": "Apple Silicon",
            "type": "Apple Silicon",
            "backend": "Metal",
            "unified_memory": True
        }
        gpu_info["available_backends"].append("Metal")
        gpu_info["total_gpus"] += 1

    return gpu_info

def generate_recommendations(cpu, mem, disk, gpu):
    recs = {}
    
    # Parallel processing
    if cpu['logical_cores'] >= 8:
        recs['parallel_processing'] = {
            "strategy": "high_parallelism",
            "suggested_workers": max(1, cpu['logical_cores'] - 2),
            "libraries": ["joblib", "multiprocessing", "dask"]
        }
    elif cpu['logical_cores'] >= 4:
        recs['parallel_processing'] = {
            "strategy": "moderate_parallelism",
            "suggested_workers": max(1, cpu['logical_cores'] - 1),
            "libraries": ["joblib", "multiprocessing"]
        }
    else:
        recs['parallel_processing'] = {
            "strategy": "sequential",
            "suggested_workers": 1,
            "libraries": []
        }

    # Memory
    if mem['available_gb'] < 4:
        recs['memory_strategy'] = {
            "strategy": "memory_constrained",
            "libraries": ["dask", "zarr", "h5py"],
            "note": "Use out-of-core processing for large datasets"
        }
    elif mem['available_gb'] < 16:
        recs['memory_strategy'] = {
            "strategy": "moderate_memory",
            "libraries": ["dask", "zarr", "pandas"],
            "note": "Consider chunking for datasets > 2GB"
        }
    else:
        recs['memory_strategy'] = {
            "strategy": "memory_abundant",
            "libraries": ["pandas", "numpy"],
            "note": "Can load most datasets into memory directly"
        }

    # GPU
    if gpu['total_gpus'] > 0:
        recs['gpu_acceleration'] = {
            "available": True,
            "backends": gpu['available_backends'],
            "suggested_libraries": []
        }
        if "CUDA" in gpu['available_backends']:
            recs['gpu_acceleration']['suggested_libraries'].extend(["pytorch", "tensorflow", "cupy", "rapids"])
        if "Metal" in gpu['available_backends']:
            recs['gpu_acceleration']['suggested_libraries'].extend(["pytorch-mps", "tensorflow-metal", "jax-metal"])
        if "ROCm" in gpu['available_backends']:
            recs['gpu_acceleration']['suggested_libraries'].extend(["pytorch-rocm", "tensorflow-rocm"])
    else:
        recs['gpu_acceleration'] = {
            "available": False,
            "backends": [],
            "suggested_libraries": ["cpu-optimized versions"]
        }

    # Disk
    if disk['available_gb'] < 10:
        recs['large_data_handling'] = {
            "strategy": "disk_constrained",
            "note": "Use streaming or compression strategies. Clear space if possible."
        }
    elif disk['available_gb'] < 100:
        recs['large_data_handling'] = {
            "strategy": "moderate_disk",
            "note": "Use Zarr, H5py, or Parquet formats to optimize space."
        }
    else:
        recs['large_data_handling'] = {
            "strategy": "disk_abundant",
            "note": "Sufficient space for large intermediate files."
        }
        
    return recs

def main():
    import argparse
    parser = argparse.ArgumentParser(description="Detect system resources for scientific computing")
    parser.add_argument("-o", "--output", default=".claude_resources.json", help="Output JSON path")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print verbose output")
    args = parser.parse_args()

    cpu = get_cpu_info()
    mem = get_memory_info()
    disk = get_disk_info()
    gpu = get_gpu_info()
    recs = generate_recommendations(cpu, mem, disk, gpu)

    data = {
        "timestamp": datetime.datetime.now().isoformat(),
        "os": {
            "system": platform.system(),
            "release": platform.release(),
            "machine": platform.machine()
        },
        "cpu": cpu,
        "memory": mem,
        "disk": disk,
        "gpu": gpu,
        "recommendations": recs
    }

    with open(args.output, 'w') as f:
        json.dump(data, f, indent=2)

    if args.verbose:
        print(json.dumps(data, indent=2))
    print(f"✅ Resource detection complete. Data saved to: {args.output}")

if __name__ == "__main__":
    main()
