param (
    [Parameter(Mandatory=$true)]
    [string]$BuildId,
    [switch]$ErrorsOnly,
    [switch]$TestsOnly
)

# Fetching build errors for Build ID
if ($ErrorsOnly) {
    gh run view $BuildId --log-failed | Select-String -Pattern "error" -Context 2,2
} elseif ($TestsOnly) {
    gh run view $BuildId --log-failed | Select-String -Pattern "test failed|failed test" -Context 2,2
} else {
    gh run view $BuildId --log-failed
}
