param (
    [switch]$Force
)

Write-Host "Initializing Triage Session..."
Write-Host "Fetching milestones from GitHub..."

# Fetch milestones via gh
$milestonesJson = gh api repos/dotnet/maui/milestones --jq '.[] | {title: .title, open_issues: .open_issues}' | ConvertFrom-Json

$output = @()
$output += "Servicing Releases:"
$milestonesJson | Where-Object { $_.title -match "Servicing|SR" } | ForEach-Object {
    $output += "  - $($_.title) [$($_.open_issues) open]"
}

$output += ""
$output += "Other:"
$milestonesJson | Where-Object { $_.title -notmatch "Servicing|SR|Backlog" } | ForEach-Object {
    $output += "  - $($_.title) [$($_.open_issues) open]"
}

$output += ""
$output += "Backlog:"
$milestonesJson | Where-Object { $_.title -match "Backlog" } | ForEach-Object {
    $output += "  - $($_.title) [$($_.open_issues) open]"
}

$outputStr = $output -join "`n"
Write-Host ""
Write-Host $outputStr
Write-Host ""

$sessionFile = "triage-session.txt"
$outputStr | Out-File -FilePath $sessionFile -Force

Write-Host "Session details saved to $sessionFile"
