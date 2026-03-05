param (
    [Parameter(Mandatory=$true)] [int]$PRNumber,
    [Parameter(Mandatory=$false)] [string]$ReportFile,
    [switch]$DryRun
)
Write-Host "Posting Verify-Tests comment for PR #$PRNumber"
if ($DryRun) { Write-Host "[DryRun Mode]" }
