while($true) {
    $publicIP = Invoke-RestMethod -Uri "https://v4.ident.me/"
    [Environment]::SetEnvironmentVariable("FORWARD_ADDRESS_OVERRIDE", $publicIP, "User")
    Start-Sleep -Seconds 60
}
