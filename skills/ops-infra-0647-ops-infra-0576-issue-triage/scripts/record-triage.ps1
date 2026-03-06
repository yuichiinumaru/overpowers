#!/usr/bin/env pwsh
# record-triage.ps1
# Records triaged issue actions
param(
    [Parameter(Mandatory=$true)]
    [int]$IssueNumber,
    [Parameter(Mandatory=$true)]
    [string]$Milestone
)

$ErrorActionPreference = "Stop"

Write-Host "Recording triage for issue #$IssueNumber -> Milestone: $Milestone"
# This would append to CustomAgentLogsTmp/Triage/triage-*.json
# For simplicity, just output for now
$record = @{
    IssueNumber = $IssueNumber
    Milestone = $Milestone
    Timestamp = (Get-Date).ToString("o")
}
$json = $record | ConvertTo-Json -Compress
Write-Host "Recorded: $json"
