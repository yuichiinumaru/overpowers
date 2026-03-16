param (
    [Parameter(Mandatory=$false)] [string]$TestDir,
    [Parameter(Mandatory=$false)] [int]$IssueNumber,
    [switch]$DryRun
)
Write-Host "Posting Write-Tests comment for Issue/PR #$IssueNumber"
if ($DryRun) { Write-Host "[DryRun Mode]" }
