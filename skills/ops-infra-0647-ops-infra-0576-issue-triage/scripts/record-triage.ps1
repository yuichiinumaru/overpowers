param (
    [int]$IssueNumber,
    [string]$Milestone
)

Write-Host "Recording triage decision for issue $IssueNumber: Assigned to $Milestone"

$record = @{
    IssueNumber = $IssueNumber
    Milestone = $Milestone
    Timestamp = (Get-Date).ToString("yyyy-MM-ddTHH:mm:ssZ")
}

$recordJson = $record | ConvertTo-Json -Compress
$logDir = "CustomAgentLogsTmp/Triage"
if (!(Test-Path $logDir)) {
    New-Item -ItemType Directory -Force -Path $logDir | Out-Null
}

$sessionFile = "$logDir/triage-session.json"
if (Test-Path $sessionFile) {
    $session = Get-Content $sessionFile | ConvertFrom-Json
} else {
    $session = @{
        Stats = @{
            Triaged = 0
            Skipped = 0
        }
        History = @()
    }
}

$session.Stats.Triaged++
$session.History += $record

$session | ConvertTo-Json -Depth 5 | Out-File -FilePath $sessionFile -Force

Write-Host "Record saved to $sessionFile"
