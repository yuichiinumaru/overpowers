param (
    [Parameter(Mandatory=$false)] [string]$TryFixDir,
    [Parameter(Mandatory=$false)] [int]$IssueNumber,
    [switch]$DryRun
)
Write-Host "Posting Try-Fix comment for Issue/PR #$IssueNumber"
if ($DryRun) { Write-Host "[DryRun Mode]" }
