param (
    [Parameter(Mandatory=$true)]
    [string]$BuildId,
    [switch]$FailedOnly
)

# Actual script to fetch AzDO build info for Helix/PRs using GitHub CLI / APIs
if ($FailedOnly) {
    gh run view $BuildId --log-failed
} else {
    gh run view $BuildId
}
