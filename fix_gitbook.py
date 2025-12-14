import os
import json

# 1. Define the renames (Folder, OldName -> NewName)
renames = {
    "tools": ("README.md", "Dev-Workflow-Hub.md"),
    "SenTient": ("README.md", "SenTient-Engine-Hub.md"),
    "abstract-wiki-architect": ("README.md", "Wiki-Architect-Hub.md"),
    "Orgo": ("README.md", "Orgo-System-Hub.md"),
    "Ariane": ("README.md", "Ariane-Hub.md"),
    "Ame-Artificielle": ("README.md", "Ame-Vision-Hub.md"),
    "SwarmCraft": ("README.md", "SwarmCraft-Hub.md"),
    "Konnaxion": ("README.md", "Konnaxion-Hub.md"),
}

def rename_files():
    print("--- Renaming Files to '-Hub' ---")
    for folder, (old, new) in renames.items():
        old_path = os.path.join(folder, old)
        new_path = os.path.join(folder, new)
        
        # Check if the OLD file exists to rename it
        if os.path.exists(old_path):
            try:
                os.rename(old_path, new_path)
                print(f"✅ Renamed: {old_path} -> {new_path}")
            except Exception as e:
                print(f"❌ Error renaming {old_path}: {e}")
        # Check if it was ALREADY renamed (idempotency)
        elif os.path.exists(new_path):
            print(f"ℹ️  Already renamed: {new_path}")
        else:
            print(f"⚠️  Source file not found: {old_path}")

def update_json():
    print("\n--- Generating new docs.json ---")
    
    new_nav = [
        {
            "group": "Introduction",
            "pages": ["index"]
        },
        {
            "group": "Konnaxion",
            "pages": [
                "Konnaxion/Konnaxion-Hub",
                {
                    "group": "KonnectED (Education)",
                    "pages": ["Konnaxion/KonnectED/Knowledge", "Konnaxion/KonnectED/CertifiKation"]
                },
                {
                    "group": "Ethikos (Governance)",
                    "pages": ["Konnaxion/Ethikos/Korum", "Konnaxion/Ethikos/Konsultations"]
                },
                {
                    "group": "Kreative (Culture)",
                    "pages": ["Konnaxion/Kreative/Konservation", "Konnaxion/Kreative/Kontact"]
                },
                {
                    "group": "keenKonnect (R&D)",
                    "pages": ["Konnaxion/keenKonnect/Konstruct", "Konnaxion/keenKonnect/Stockage"]
                },
                {
                    "group": "Kollective Intelligence",
                    "pages": ["Konnaxion/Kollective-Intelligence/EkoH", "Konnaxion/Kollective-Intelligence/Smart-Vote"]
                },
                {
                    "group": "Technical",
                    "pages": ["Konnaxion/Technical/Konnaxion-Technical-Architecture-And-Services"]
                }
            ]
        },
        {
            "group": "SwarmCraft",
            "pages": [
                "SwarmCraft/SwarmCraft-Hub",
                {
                    "group": "Core Logic",
                    "pages": [
                        "SwarmCraft/Core/Architecture-Overview",
                        "SwarmCraft/Core/Deterministic-Pipeline-Scan-Plan-Execute",
                        "SwarmCraft/Core/Central-Matrix-Runtime-State"
                    ]
                },
                {
                    "group": "Story Scaffold",
                    "pages": [
                        "SwarmCraft/Scaffold/Story-Scaffold-Templates-Outline-Parts",
                        "SwarmCraft/Scaffold/Story-Bible-Creative-Intent",
                        "SwarmCraft/Scaffold/Schema-Templates",
                        "SwarmCraft/Scaffold/Schema-Outline",
                        "SwarmCraft/Scaffold/Outline-Grid-CSV-Round-Trip"
                    ]
                },
                {
                    "group": "Runtime & Tools",
                    "pages": [
                        "SwarmCraft/Runtime/Orchestration-Slice-By-Slice-Prompt-Hydration",
                        "SwarmCraft/Runtime/Multi-Project-Management",
                        "SwarmCraft/Runtime/RAG-Memory-System",
                        "SwarmCraft/Runtime/Provider-Adapter-Grok",
                        "SwarmCraft/Runtime/Dashboard-TUI-Reference"
                    ]
                },
                "SwarmCraft/Meta/Credits-And-Lineage"
            ]
        },
        {
            "group": "Ariane",
            "pages": [
                "Ariane/Ariane-Hub",
                {
                    "group": "Atlas (The Map)",
                    "pages": [
                        "Ariane/Atlas/Atlas",
                        "Ariane/Atlas/Atlas-Graph-Model",
                        "Ariane/Atlas/Atlas-Core-Schema",
                        "Ariane/Atlas/Atlas-Ontology-Vocabulary"
                    ]
                },
                {
                    "group": "Theseus (The Explorer)",
                    "pages": [
                        "Ariane/Theseus/Theseus",
                        "Ariane/Theseus/Theseus-Drivers",
                        "Ariane/Theseus/Theseus-Exploration-Engine",
                        "Ariane/Theseus/Theseus-State-Identification"
                    ]
                },
                {
                    "group": "Consumers",
                    "pages": [
                        "Ariane/Consumers/Consumers",
                        "Ariane/Consumers/Consumers-AI-Agent-Integration",
                        "Ariane/Consumers/Consumers-Future-Overlay-Client",
                        "Ariane/Consumers/Hybrid-Mapping-and-Human-Guided-Assistants"
                    ]
                },
                {
                    "group": "Concepts",
                    "pages": [
                        "Ariane/Concepts/Background-UI-as-Data",
                        "Ariane/Concepts/Glossary"
                    ]
                }
            ]
        },
        {
            "group": "Orgo",
            "pages": ["Orgo/Orgo-System-Hub"]
        },
        {
            "group": "Âme Artificielle",
            "pages": [
                "Ame-Artificielle/Ame-Vision-Hub",
                "Ame-Artificielle/Controle-Et-Personnalisation",
                "Ame-Artificielle/Creation-De-Chemins",
                "Ame-Artificielle/Ethique-Et-Gouvernance",
                "Ame-Artificielle/Meta-Cognition-Et-Resolution",
                "Ame-Artificielle/Specifications-Fonctionnelles"
            ]
        },
        {
            "group": "Outils & Code",
            "pages": [
                "tools/Dev-Workflow-Hub",
                "SenTient/SenTient-Engine-Hub",
                "abstract-wiki-architect/Wiki-Architect-Hub"
            ]
        }
    ]

    try:
        with open("docs.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        print("⚠️ docs.json not found, creating new one.")
        data = {
            "$schema": "https://mintlify.com/docs.json",
            "name": "Omni-Wiki",
            "theme": "mint",
            "topbarLinks": [{"name": "GitHub", "url": "https://github.com/Rejean-McCormick/Omni-Wiki"}]
        }

    data["navigation"] = {"tabs": [{"tab": "Wiki", "groups": new_nav}]}

    with open("docs.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)
    print("✅ docs.json updated.")

if __name__ == "__main__":
    rename_files()
    update_json()