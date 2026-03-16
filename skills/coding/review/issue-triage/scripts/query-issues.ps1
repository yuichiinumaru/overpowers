#!/usr/bin/env pwsh
# query-issues.ps1
# Queries open issues in dotnet/maui for triage
param(
    [string]$Platform = "all",
    [string]$Area = "",
    [int]$Limit = 50,
    [int]$Skip = 0,
    [string]$OutputFormat = "table",
    [switch]$RequireAreaLabel,
    [switch]$SkipDetails
)

$ErrorActionPreference = "Stop"

if (!(Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "Error: GitHub CLI (gh) not found."
    Return
}

$query = "repo:dotnet/maui is:issue is:open no:milestone"
$query += " -label:s/needs-info -label:s/needs-repro -label:area-blazor -label:s/try-latest-version -label:s/move-to-vs-feedback"

if ($Platform -ne "all") {
    $query += " label:platform/$Platform"
}

if ($Area) {
    $query += " label:$Area"
}

if ($RequireAreaLabel) {
    $query += " label:area-*"
}

Write-Host "Running query: $query"
$results = gh issue list --repo dotnet/maui --search $query --limit $Limit --json number,title,url,author,labels,comments

if ($OutputFormat -eq "triage") {
    $issues = $results | ConvertFrom-Json
    foreach ($i in $issues) {
        $labels = ($i.labels | ForEach-Object { $_.name }) -join ", "
        Write-Host "## Issue #$($i.number)`n"
        Write-Host "**$($i.title)**`n"
        Write-Host "🔗 $($i.url)`n"
        Write-Host "| Field | Value |"
        Write-Host "|-------|-------|"
        Write-Host "| **Author** | $($i.author.login) |"
        Write-Host "| **Labels** | $labels |"
        Write-Host "| **Comments** | $($i.comments.Count) |`n"
        Write-Host "What would you like to do with this issue?`n---"
    }
} else {
    Write-Host $results
}
