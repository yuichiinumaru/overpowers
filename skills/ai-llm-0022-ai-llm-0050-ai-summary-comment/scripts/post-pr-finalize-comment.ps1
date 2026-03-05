param (
    [Parameter(Mandatory=$true)] [int]$PRNumber,
    [Parameter(Mandatory=$false)] [string]$SummaryFile,
    [string]$TitleStatus,
    [string]$DescriptionStatus,
    [switch]$DryRun
)
Write-Host "Posting PR Finalization comment for PR #$PRNumber"
if ($DryRun) { Write-Host "[DryRun Mode]" }
