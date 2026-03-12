#!/bin/bash
# deploy.sh - Script to deploy frontend and backend to Cloud Run

if [ "$1" == "frontend" ]; then
    echo "Building and deploying frontend..."
    cd frontend && npm run build
    gcloud run deploy frontend --source .
elif [ "$1" == "backend" ]; then
    echo "Building and deploying backend..."
    cd backend
    gcloud run deploy backend --source .
elif [ "$1" == "all" ]; then
    echo "Building and deploying frontend..."
    cd frontend && npm run build
    gcloud run deploy frontend --source .
    cd ..

    echo "Building and deploying backend..."
    cd backend
    gcloud run deploy backend --source .
    cd ..
else
    echo "Usage: $0 {frontend|backend|all}"
    # removed exit 1
fi
