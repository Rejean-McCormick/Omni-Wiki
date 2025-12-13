import tkinter as tk
from tkinter import scrolledtext, messagebox
import os
import re

# --- CONFIGURATION DES CORRECTIONS ---

# 1. Remplacement de noms de fichiers (pour SUMMARY.md et les liens standards)
# Format : "Ancien_Nom" : "Nouveau_Nom"
FILENAME_FIXES = {
    # Ame-Artificielle (Majuscules -> TitleCase)
    "CONTROLE_ET_PERSONNALISATION.md": "Controle-Et-Personnalisation.md",
    "CREATION_DE_CHEMINS.md": "Creation-De-Chemins.md",
    "ETHIQUE_ET_GOUVERNANCE.md": "Ethique-Et-Gouvernance.md",
    "META_COGNITION_ET_RESOLUTION.md": "Meta-Cognition-Et-Resolution.md",
    "SPECIFICATIONS_FONCTIONNELLES.md": "Specifications-Fonctionnelles.md",

    # Konnaxion (Caractères spéciaux)
    "Konnaxion-–-Technical-Architecture-&-Services.md": "Konnaxion-Technical-Architecture-And-Services.md",

    # SwarmCraft (Parenthèses, &)
    "Central-Matrix-(Runtime-State).md": "Central-Matrix-Runtime-State.md",
    "Credits-&-Lineage.md": "Credits-And-Lineage.md",
    "Deterministic-Pipeline-(SCAN-PLAN-EXECUTE).md": "Deterministic-Pipeline-Scan-Plan-Execute.md",
    "Orchestration-Slice-by-Slice-Prompt-Hydration.md": "Orchestration-Slice-By-Slice-Prompt-Hydration.md", # Fix B majuscule
    "Story-Bible-(Creative-Intent).md": "Story-Bible-Creative-Intent.md",
    "Story-Scaffold-(Templates-Outline-Parts).md": "Story-Scaffold-Templates-Outline-Parts.md",
    
    # Corrections de liens cassés dans README root
    "SwarmCraft/Home.md": "SwarmCraft/README.md",
    "Ame-Artificielle/Home.md": "Ame-Artificielle/README.md",
    "Ariane/Home.md": "Ariane/README.md",
    "Konnaxion/Home.md": "Konnaxion/README.md",
    "Orgo/Home.md": "Orgo/README.md",
    "tools/Home.md": "tools/README.md",
    "SenTient/Home.md": "SenTient/README.md"
}

# 2. Remplacement des Wiki-Links [[...]] vers [Title](File.md)
# Format : "Texte entre crochets" : "Nom du fichier cible"
WIKI_LINK_MAP = {
    # SwarmCraft
    "Credits & Lineage": "Credits-And-Lineage.md",
    "Central Matrix (Runtime State)": "Central-Matrix-Runtime-State.md",
    "Story Bible (Creative Intent)": "Story-Bible-Creative-Intent.md",
    "Story Scaffold (Templates-Outline-Parts)": "Story-Scaffold-Templates-Outline-Parts.md",
    "Story Scaffold (Templates + Outline + Parts)": "Story-Scaffold-Templates-Outline-Parts.md",
    "Schema Templates": "Schema-Templates.md",
    "Schema Outline": "Schema-Outline.md",
    "Outline Grid CSV Round-Trip": "Outline-Grid-CSV-Round-Trip.md",
    "Outline Grid & CSV Round-Trip": "Outline-Grid-CSV-Round-Trip.md",
    "Deterministic Pipeline (SCAN-PLAN-EXECUTE)": "Deterministic-Pipeline-Scan-Plan-Execute.md",
    "Deterministic Pipeline (SCAN → PLAN → EXECUTE)": "Deterministic-Pipeline-Scan-Plan-Execute.md",
    "Orchestration Slice-by-Slice Prompt Hydration": "Orchestration-Slice-By-Slice-Prompt-Hydration.md",
    "Orchestration: Slice-by-Slice Prompt Hydration": "Orchestration-Slice-By-Slice-Prompt-Hydration.md",
    "Multi-Project Management": "Multi-Project-Management.md",
    "RAG Memory System": "RAG-Memory-System.md",
    "Dashboard TUI Reference": "Dashboard-TUI-Reference.md",
    "Dashboard (TUI) Reference": "Dashboard-TUI-Reference.md",
    "Provider Adapter Grok": "Provider-Adapter-Grok.md",
    "Provider Adapter: Grok": "Provider-Adapter-Grok.md",
    "Architecture Overview": "Architecture-Overview.md",

    # Ariane
    "Theseus": "Theseus.md",
    "Atlas": "Atlas.md",
    "Consumers": "Consumers.md",
    "Atlas/Core-Schema": "Atlas-Core-Schema.md",
    "Atlas/Graph-Model": "Atlas-Graph-Model.md",
    "Atlas/Ontology-Vocabulary": "Atlas-Ontology-Vocabulary.md",
    "Consumers/AI-Agent-Integration": "Consumers-AI-Agent-Integration.md",
    "Consumers/Future-Overlay-Client": "Consumers-Future-Overlay-Client.md",
    "Background-UI-as-Data": "Background-UI-as-Data.md",
    "Hybrid-Mapping-and-Human-Guided-Assistants": "Hybrid-Mapping-and-Human-Guided-Assistants.md",
    "Theseus/State-Identification": "Theseus-State-Identification.md",
    "Theseus/Exploration-Engine": "Theseus-Exploration-Engine.md",
    "Theseus/Drivers": "Theseus-Drivers.md"
}

# --- APPLICATION ---

class ContentFixerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GitBook Link Fixer")
        self.root.geometry("800x600")

        # Set working dir to script location
        try:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            os.chdir(script_dir)
        except:
            pass

        # Header
        header = tk.Label(root, text="GitBook Content & Link Fixer", font=("Arial", 14, "bold"))
        header.pack(pady=10)

        desc = tk.Label(root, text=f"Scanning folder: {os.getcwd()}\nChanges: Wiki-Links [[...]] and Broken Filenames", fg="gray")
        desc.pack(pady=5)

        # Log Window
        self.txt_log = scrolledtext.ScrolledText(root, width=90, height=25, state='disabled')
        self.txt_log.pack(padx=10, pady=10)
        
        # Tags for coloring
        self.txt_log.tag_config("INFO", foreground="black")
        self.txt_log.tag_config("CHANGE", foreground="blue")
        self.txt_log.tag_config("SUCCESS", foreground="green")
        self.txt_log.tag_config("ERROR", foreground="red")

        # Buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)
        
        btn_run = tk.Button(btn_frame, text="Lancer les Corrections", bg="#4CAF50", fg="white", 
                            font=("Arial", 11, "bold"), command=self.run_fixes, padx=20)
        btn_run.pack(side=tk.LEFT, padx=10)

    def log(self, message, tag="INFO"):
        self.txt_log.config(state='normal')
        self.txt_log.insert(tk.END, message + "\n", tag)
        self.txt_log.see(tk.END)
        self.txt_log.config(state='disabled')
        self.root.update()

    def run_fixes(self):
        self.txt_log.config(state='normal')
        self.txt_log.delete(1.0, tk.END)
        self.txt_log.config(state='disabled')
        
        self.log("--- STARTING SCAN ---", "INFO")
        
        modified_files = 0
        total_replacements = 0

        # Walk through all Markdown files
        for root_dir, _, files in os.walk("."):
            for file in files:
                if file.endswith(".md"):
                    file_path = os.path.join(root_dir, file)
                    self.process_file(file_path)

        self.log("-" * 40, "INFO")
        self.log("SCAN COMPLETED.", "SUCCESS")
        messagebox.showinfo("Terminé", "Les corrections de contenu sont terminées.")

    def process_file(self, file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            self.log(f"Error reading {file_path}: {e}", "ERROR")
            return

        original_content = content
        changes_made = []

        # 1. FIX WIKI LINKS [[...]]
        # Pattern: [[Captured Text]]
        def replace_wiki_link(match):
            text = match.group(1)
            # Check exact map first
            if text in WIKI_LINK_MAP:
                target_file = WIKI_LINK_MAP[text]
                # If target has a subfolder in map but we prefer relative, standard markdown handles it usually.
                # But here we just want the filename usually or relative path.
                # For simplicity, we assume links are typically siblings or mapped correctly.
                # Clean title for display: remove subfolders from display text if present
                display_text = text.split('/')[-1]
                # Remove parentheses for display text aesthetics if desired, but keeping original text is safer
                # Let's clean the display text slightly:
                display_text = re.sub(r'\(.*?\)', '', text).strip()
                if not display_text: display_text = text
                
                return f"[{display_text}]({target_file})"
            
            # Fallback for unknown [[Links]]: just add .md
            return f"[{text}]({text}.md)"

        new_content = re.sub(r'\[\[(.*?)\]\]', replace_wiki_link, content)
        if new_content != content:
            changes_made.append("Converted Wiki Links")
            content = new_content

        # 2. FIX BROKEN FILENAMES (String Replacement)
        # Used for SUMMARY.md, README.md and standard links
        for bad_name, good_name in FILENAME_FIXES.items():
            if bad_name in content:
                content = content.replace(bad_name, good_name)
                changes_made.append(f"Fixed filename: {bad_name}")

        # 3. SAVE IF CHANGED
        if content != original_content:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                # Log compact summary
                rel_path = os.path.relpath(file_path)
                self.log(f"MODIFIED: {rel_path}", "CHANGE")
                for change in list(set(changes_made))[:3]: # Limit log spam
                    self.log(f"  -> {change}", "INFO")
            except Exception as e:
                self.log(f"Error writing {file_path}: {e}", "ERROR")
        else:
            # self.log(f"No changes: {file_path}", "INFO")
            pass

if __name__ == "__main__":
    root = tk.Tk()
    app = ContentFixerApp(root)
    root.mainloop()