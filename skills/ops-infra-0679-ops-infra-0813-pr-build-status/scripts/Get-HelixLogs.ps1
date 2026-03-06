param (
    [Parameter(Mandatory=$true)]
    [string]$BuildId,
    [string]$Platform,
    [switch]$ShowConsoleLog,
    [string]$WorkItem,
    [int]$TailLines = 100
)

# Simulated Helix log retrieval (Helix is a specific Azure DevOps infrastructure)
# We use gh run view as a proxy here or fallback to a known endpoint if applicable.
$logCommand = "gh run view $BuildId --log"
if ($Platform) {
    $logCommand += " | Select-String -Pattern '$Platform'"
}
if ($WorkItem) {
    $logCommand += " | Select-String -Pattern '$WorkItem'"
}
if ($ShowConsoleLog) {
    Invoke-Expression "$logCommand | Select-Object -Last $TailLines"
} else {
    Invoke-Expression $logCommand
}
