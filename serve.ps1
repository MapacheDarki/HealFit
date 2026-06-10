$port = 8000
$prefix = "http://localhost:$port/"
$listener = New-Object System.Net.HttpListener
$listener.Prefixes.Add($prefix)
$listener.Start()
Write-Host "Servidor local iniciado en $prefix"
Write-Host "Presiona Ctrl+C para detener."

while ($listener.IsListening) {
    $context = $listener.GetContext()
    $request = $context.Request
    $path = $request.Url.LocalPath.TrimStart('/')
    if ([string]::IsNullOrWhiteSpace($path)) { $path = 'index.html' }
    $path = $path -replace '/+', '/'
    $file = Join-Path (Get-Location) $path

    if (!(Test-Path $file)) {
        $context.Response.StatusCode = 404
        $response = [System.Text.Encoding]::UTF8.GetBytes('404 Not Found')
        $context.Response.ContentType = 'text/plain'
        $context.Response.ContentLength64 = $response.Length
        $context.Response.OutputStream.Write($response, 0, $response.Length)
        $context.Response.OutputStream.Close()
        continue
    }

    $bytes = [System.IO.File]::ReadAllBytes($file)
    $contentType = switch ([System.IO.Path]::GetExtension($file).ToLower()) {
        '.html' {'text/html'}
        '.css' {'text/css'}
        '.js' {'application/javascript'}
        '.png' {'image/png'}
        '.jpg' {'image/jpeg'}
        '.jpeg' {'image/jpeg'}
        '.gif' {'image/gif'}
        '.svg' {'image/svg+xml'}
        default {'application/octet-stream'}
    }
    $context.Response.ContentType = $contentType
    $context.Response.ContentLength64 = $bytes.Length
    $context.Response.OutputStream.Write($bytes, 0, $bytes.Length)
    $context.Response.OutputStream.Close()
}
$listener.Stop()
