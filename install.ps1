# Installs the Chiikawa Dots Pets into the Codex pets folder on Windows.
# Usage (PowerShell):
#   irm https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main/install.ps1 | iex
# Pick specific pets by setting $env:CHIIKAWA_PETS first, for example "chiikawa,usagi".

$ErrorActionPreference = 'Stop'

$repoRawUrl = 'https://raw.githubusercontent.com/heelee912/chiikawa-dots-pets/main'
$availablePets = @('chiikawa', 'hachiware', 'usagi', 'momonga', 'shisa', 'rakko', 'kurimanju', 'siren', 'furuhonya', 'anoko', 'dekatsuyo')
$requestedPets = if ($env:CHIIKAWA_PETS) { $env:CHIIKAWA_PETS -split '[,\s]+' | Where-Object { $_ } } else { $availablePets }

$codexHome = if ($env:CODEX_HOME) { $env:CODEX_HOME } else { Join-Path $HOME '.codex' }
$petsRoot = Join-Path $codexHome 'pets'

foreach ($petId in $requestedPets) {
    if ($availablePets -notcontains $petId) {
        throw "Unknown pet '$petId'. Choose from: $($availablePets -join ', ')"
    }
    $petFolder = Join-Path $petsRoot $petId
    New-Item -ItemType Directory -Force -Path $petFolder | Out-Null
    foreach ($fileName in @('pet.json', 'spritesheet.png')) {
        Invoke-WebRequest -UseBasicParsing -Uri "$repoRawUrl/pets/$petId/$fileName" -OutFile (Join-Path $petFolder $fileName)
    }
    Write-Host "Installed $petId -> $petFolder"
}

Write-Host 'Done. Restart Codex and pick the pet from its pet list.'
