import os

# This dictionary defines how files were moved. 
# It maps the OLD filename to the NEW relative path from the module root.
# Example: "Knowledge.md" is now in "KonnectED/Knowledge.md"
MOVES = {
    # Konnaxion moves
    "Knowledge.md": "KonnectED/Knowledge.md",
    "CertifiKation.md": "KonnectED/CertifiKation.md",
    "Korum.md": "Ethikos/Korum.md",
    "Konsultations.md": "Ethikos/Konsultations.md",
    "Konservation.md": "Kreative/Konservation.md",
    "Kontact.md": "Kreative/Kontact.md",
    "Konstruct.md": "keenKonnect/Konstruct.md",
    "Stockage.md": "keenKonnect/Stockage.md",
    "EkoH.md": "Kollective-Intelligence/EkoH.md",
    "Smart-Vote.md": "Kollective-Intelligence/Smart-Vote.md",
    "Konnaxion-Technical-Architecture-And-Services.md": "Technical/Konnaxion-Technical-Architecture-And-Services.md",
    
    # SwarmCraft moves
    "Architecture-Overview.md": "Core/Architecture-Overview.md",
    "Central-Matrix-Runtime-State.md": "Core/Central-Matrix-Runtime-State.md",
    "Deterministic-Pipeline-Scan-Plan-Execute.md": "Core/Deterministic-Pipeline-Scan-Plan-Execute.md",
    "Story-Bible-Creative-Intent.md": "Scaffold/Story-Bible-Creative-Intent.md",
    "Story-Scaffold-Templates-Outline-Parts.md": "Scaffold/Story-Scaffold-Templates-Outline-Parts.md",
    "Schema-Templates.md": "Scaffold/Schema-Templates.md",
    "Schema-Outline.md": "Scaffold/Schema-Outline.md",
    "Outline-Grid-CSV-Round-Trip.md": "Scaffold/Outline-Grid-CSV-Round-Trip.md",
    "Orchestration-Slice-By-Slice-Prompt-Hydration.md": "Runtime/Orchestration-Slice-By-Slice-Prompt-Hydration.md",
    "Multi-Project-Management.md": "Runtime/Multi-Project-Management.md",
    "RAG-Memory-System.md": "Runtime/RAG-Memory-System.md",
    "Provider-Adapter-Grok.md": "Runtime/Provider-Adapter-Grok.md",
    "Dashboard-TUI-Reference.md": "Runtime/Dashboard-TUI-Reference.md",
    "Credits-And-Lineage.md": "Meta/Credits-And-Lineage.md",

    # Ariane moves
    "Atlas.md": "Atlas/Atlas.md",
    "Atlas-Core-Schema.md": "Atlas/Atlas-Core-Schema.md",
    "Atlas-Graph-Model.md": "Atlas/Atlas-Graph-Model.md",
    "Atlas-Ontology-Vocabulary.md": "Atlas/Atlas-Ontology-Vocabulary.md",
    "Theseus.md": "Theseus/Theseus.md",
    "Theseus-Drivers.md": "Theseus/Theseus-Drivers.md",
    "Theseus-Exploration-Engine.md": "Theseus/Theseus-Exploration-Engine.md",
    "Theseus-State-Identification.md": "Theseus/Theseus-State-Identification.md",
    "Consumers.md": "Consumers/Consumers.md",
    "Consumers-AI-Agent-Integration.md": "Consumers/Consumers-AI-Agent-Integration.md",
    "Consumers-Future-Overlay-Client.md": "Consumers/Consumers-Future-Overlay-Client.md",
    "Hybrid-Mapping-and-Human-Guided-Assistants.md": "Consumers/Hybrid-Mapping-and-Human-Guided-Assistants.md",
    "Background-UI-as-Data.md": "Concepts/Background-UI-as-Data.md",
    "Glossary.md": "Concepts/Glossary.md"
}

def update_links_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        changes = 0
        
        # Simple string replacement for links
        # This looks for patterns like [Label](OldFile.md) and replaces with [Label](NewSubfolder/OldFile.md)
        for old_file, new_path in MOVES.items():
            
            # CASE 1: Updating links inside a ROOT README (e.g. Konnaxion/README.md)
            # Link was [Link](Knowledge.md), now needs to be [Link](KonnectED/Knowledge.md)
            if f"({old_file})" in new_content:
                new_content = new_content.replace(f"({old_file})", f"({new_path})")
                changes += 1

            # CASE 2: Updating links inside MOVED files
            # If we are inside KonnectED/Knowledge.md and we link to CertifiKation.md
            # They are siblings now, so (CertifiKation.md) is actually still valid IF they moved to the same folder.
            # But if they moved to DIFFERENT folders, we'd need ../ logic. 
            # For this script, we focus on fixing the Hub/README pages which are most critical.

        if changes > 0:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"✅ Fixed {changes} links in {filepath}")

    except Exception as e:
        print(f"❌ Error processing {filepath}: {e}")

def main():
    # Scan only the main module READMEs, as they act as the "Hubs" and contain the most links
    target_files = [
        "Konnaxion/README.md",
        "SwarmCraft/README.md",
        "Ariane/README.md",
        "SUMMARY.md" 
    ]

    print("--- Fixing Links in Hub Pages ---")
    for tf in target_files:
        if os.path.exists(tf):
            update_links_in_file(tf)
        else:
            print(f"Skipping {tf} (not found)")

if __name__ == "__main__":
    main()