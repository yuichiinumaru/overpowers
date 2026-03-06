param (
    [Parameter(Mandatory=$true)]
    [string]$PrNumber
)

gh pr checks $PrNumber --json name,state,url
