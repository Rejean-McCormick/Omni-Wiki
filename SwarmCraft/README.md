# 1. On définit l'entête exact que vous voulez
$summaryContent = @"
# Table des matières

* [Accueil (Rejean McCormick)](README.md)

"@

# 2. Fonction pour générer les liens d'un dossier
function Add-Module {
    param ($folder, $title)
    
    if (Test-Path $folder) {
        # Cherche le fichier principal (README.md ou Home.md)
        $mainFile = ""
        if (Test-Path "$folder\README.md") { $mainFile = "$folder/README.md" }
        elseif (Test-Path "$folder\Home.md") { $mainFile = "$folder/Home.md" }

        # Ajoute le titre du module (Lien principal)
        if ($mainFile) {
            $script:summaryContent += "* [$title]($mainFile)`n"
        } else {
            $script:summaryContent += "* [$title]()`n" # Titre sans lien si pas de Home
        }

        # Ajoute les sous-pages (indalées)
        Get-ChildItem -Path $folder -Filter *.md | 
            Where-Object { $_.Name -ne "README.md" -and $_.Name -ne "Home.md" } | 
            ForEach-Object {
                $subTitle = $_.BaseName -replace "-", " " # Enlève les tirets pour le titre
                $script:summaryContent += "  * [$subTitle]($folder/$($_.Name))`n"
            }
    }
}

# 3. Les Modules Principaux
Add-Module -folder "Konnaxion" -title "Konnaxion"
Add-Module -folder "Orgo" -title "Orgo"

# 4. Section Autres Modules
$summaryContent += "`n## Autres Modules`n"

Add-Module -folder "SwarmCraft" -title "SwarmCraft"
Add-Module -folder "Ame-Artificielle" -title "Âme Artificielle"
Add-Module -folder "Ariane" -title "Ariane"
Add-Module -folder "abstract-wiki-architect" -title "Architecte Abstrait"
Add-Module -folder "SenTient" -title "SenTient (Code)"
Add-Module -folder "tools" -title "Tools"

# 5. Écriture du fichier
$summaryContent | Out-File -FilePath "SUMMARY.md" -Encoding utf8
Write-Host "SUMMARY.md mis à jour avec vos titres personnalisés !" -ForegroundColor Green