param (
    [Parameter(Mandatory=$false)] [int]$PRNumber,
    [Parameter(Mandatory=$false)] [string]$StateFile,
    [Parameter(Mandatory=$false)] [string]$Content,
    [switch]$DryRun
)
Write-Host "Posting AI Summary for PR #$PRNumber"
if ($DryRun) { Write-Host "[DryRun Mode]" }
