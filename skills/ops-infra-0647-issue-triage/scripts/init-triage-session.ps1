#!/usr/bin/env pwsh
# init-triage-session.ps1
# Fetches current milestones and labels from GitHub for triage
param()

$ErrorActionPreference = "Stop"

if (!(Get-Command gh -ErrorAction SilentlyContinue)) {
    Write-Host "Error: GitHub CLI (gh) not found."
    Write-Host "Please install it from https://cli.github.com/ and run 'gh auth login'"
    Return
}

Write-Host "Fetching current milestones for dotnet/maui..."
$milestonesJson = gh api repos/dotnet/maui/milestones --jq '.[] | {title: .title, open_issues: .open_issues}' | ConvertFrom-Json

Write-Host "`nServicing Releases:"
foreach ($m in $milestonesJson) {
    if ($m.title -match "Servicing|SR") {
        Write-Host "  - $($m.title) [$($m.open_issues) open]"
    }
}

Write-Host "`nOther:"
foreach ($m in $milestonesJson) {
    if ($m.title -notmatch "Servicing|SR" -and $m.title -ne "Backlog") {
        Write-Host "  - $($m.title) [$($m.open_issues) open]"
    }
}

Write-Host "`nBacklog:"
foreach ($m in $milestonesJson) {
    if ($m.title -eq "Backlog") {
        Write-Host "  - $($m.title) [$($m.open_issues) open]"
    }
}

Write-Host "`nSession initialized successfully."
