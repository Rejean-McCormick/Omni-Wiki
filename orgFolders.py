import os
import shutil
import json

# Configuration: Mapping files to their new 'Optimal' subfolders
# Format: "Current_Folder": { "New_Subfolder": ["File1.md", "File2.md"] }
MOVES = {
    "Konnaxion": {
        "KonnectED": [
            "Knowledge.md",
            "CertifiKation.md"
        ],
        "Ethikos": [
            "Korum.md",
            "Konsultations.md"
        ],
        "Kreative": [
            "Konservation.md",
            "Kontact.md"
        ],
        "keenKonnect": [
            "Konstruct.md",
            "Stockage.md"
        ],
        "Kollective-Intelligence": [
            "EkoH.md",
            "Smart-Vote.md"
        ],
        "Technical": [
            "Konnaxion-Technical-Architecture-And-Services.md"
        ]
        # README.md stays in root of Konnaxion
    },
    "SwarmCraft": {
        "Core": [
            "Architecture-Overview.md",
            "Central-Matrix-Runtime-State.md",
            "Deterministic-Pipeline-Scan-Plan-Execute.md"
        ],
        "Scaffold": [
            "Story-Bible-Creative-Intent.md",
            "Story-Scaffold-Templates-Outline-Parts.md",
            "Schema-Templates.md",
            "Schema-Outline.md",
            "Outline-Grid-CSV-Round-Trip.md"
        ],
        "Runtime": [
            "Orchestration-Slice-By-Slice-Prompt-Hydration.md",
            "Multi-Project-Management.md",
            "RAG-Memory-System.md",
            "Provider-Adapter-Grok.md",
            "Dashboard-TUI-Reference.md"
        ],
        "Meta": [
            "Credits-And-Lineage.md"
        ]
        # README.md stays in root
    },
    "Ariane": {
        "Atlas": [
            "Atlas.md",
            "Atlas-Core-Schema.md",
            "Atlas-Graph-Model.md",
            "Atlas-Ontology-Vocabulary.md"
        ],
        "Theseus": [
            "Theseus.md",
            "Theseus-Drivers.md",
            "Theseus-Exploration-Engine.md",
            "Theseus-State-Identification.md"
        ],
        "Consumers": [
            "Consumers.md",
            "Consumers-AI-Agent-Integration.md",
            "Consumers-Future-Overlay-Client.md",
            "Hybrid-Mapping-and-Human-Guided-Assistants.md"
        ],
        "Concepts": [
            "Background-UI-as-Data.md",
            "Glossary.md"
        ]
        # README.md stays in root
    }
}

def move_files():
    base_path = os.getcwd()
    print(f"📂 Optimizing folder structure in: {base_path}\n")

    for main_folder, sub_structure in MOVES.items():
        main_folder_path = os.path.join(base_path, main_folder)
        
        if not os.path.exists(main_folder_path):
            print(f"⚠️  Skipping {main_folder} (not found)")
            continue

        print(f"🔹 Processing {main_folder}...")

        for subfolder, files in sub_structure.items():
            # Create the subfolder path (e.g. Konnaxion/KonnectED)
            target_dir = os.path.join(main_folder_path, subfolder)
            
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                print(f"   Created directory: {subfolder}")

            for filename in files:
                src = os.path.join(main_folder_path, filename)
                dst = os.path.join(target_dir, filename)

                if os.path.exists(src):
                    try:
                        shutil.move(src, dst)
                        print(f"   Moved: {filename} -> {subfolder}/")
                    except Exception as e:
                        print(f"   ❌ Error moving {filename}: {e}")
                elif os.path.exists(dst):
                     print(f"   Skipped: {filename} (already in {subfolder})")
                else:
                    print(f"   ⚠️  File not found: {filename}")

def generate_mint_json_snippet():
    # This generates the navigation block for mint.json based on the NEW structure
    nav = [
        {
            "group": "Introduction",
            "pages": ["index"]
        },
        {
            "group": "Konnaxion",
            "pages": [
                "Konnaxion/README",
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
                "SwarmCraft/README",
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
                "Ariane/README",
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
             "pages": ["Orgo/README"]
        },
        {
             "group": "Âme Artificielle",
             "pages": [
                "Ame-Artificielle/README",
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
                "abstract-wiki-architect/README",
                "SenTient/README",
                "tools/README"
            ]
        }
    ]

    print("\n" + "="*50)
    print("✅ COPY THIS INTO YOUR mint.json 'navigation' section:")
    print("="*50)
    print(json.dumps({"tabs": [{"tab": "Wiki", "groups": nav}]}, indent=2))

if __name__ == "__main__":
    move_files()
    generate_mint_json_snippet()