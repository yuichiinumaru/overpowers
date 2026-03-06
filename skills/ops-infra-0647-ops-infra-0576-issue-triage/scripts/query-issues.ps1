param (
    [string]$Platform = "all",
    [string]$Area = "",
    [int]$Limit = 50,
    [int]$Skip = 0,
    [string]$OutputFormat = "table",
    [switch]$RequireAreaLabel = $false,
    [switch]$SkipDetails = $false
)

Write-Host "Querying issues with Limit=$Limit, Skip=$Skip..."

$query = "repo:dotnet/maui is:issue is:open no:milestone -label:s/needs-info -label:s/needs-repro -label:area-blazor -label:s/try-latest-version -label:s/move-to-vs-feedback"

if ($Platform -ne "all") {
    $query += " label:platform/$Platform"
}

if ($Area -ne "") {
    $query += " label:$Area"
}

if ($RequireAreaLabel) {
    # It's hard to express "has area-*" in github search simply, so skipping for now or adding some dummy if needed
}

# Add skip/limit (Note: GitHub search API natively supports pages, `gh issue list` might be simpler)
$ghArgs = @("issue", "list", "--repo", "dotnet/maui", "--limit", $Limit, "--search", $query, "--json", "number,title,url,author,labels,comments")

$results = gh @ghArgs | ConvertFrom-Json

# Simple skip handling since gh doesn't directly support --skip in search
$results = $results | Select-Object -Skip $Skip

if ($OutputFormat -eq "triage") {
    foreach ($issue in $results) {
        $labels = ($issue.labels | Select-Object -ExpandProperty name) -join ", "
        $regression = if ($labels -match "i/regression") { "Yes" } else { "No" }

        Write-Host "## Issue #$($issue.number)"
        Write-Host ""
        Write-Host "**$($issue.title)**"
        Write-Host ""
        Write-Host "🔗 $($issue.url)"
        Write-Host ""
        Write-Host "| Field | Value |"
        Write-Host "|-------|-------|"
        Write-Host "| **Author** | $($issue.author.login) |"
        Write-Host "| **Platform** | $Platform |"
        Write-Host "| **Area** | $Area |"
        Write-Host "| **Labels** | $labels |"
        Write-Host "| **Regression** | $regression |"
        Write-Host "| **Comments** | $($issue.comments.count) |"
        Write-Host ""
        Write-Host "What would you like to do with this issue?"
        Write-Host "---"
    }
} else {
    $results | Format-Table number,title,author
}
