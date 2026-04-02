#!/usr/bin/env python3
import json
import requests

# URL interne de Home Assistant (dans HAOS / add-ons)
BASE_URL = "http://homeassistant:8123"

# 👉 Remplace par ton vrai long-lived token
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJkYzNkOWYxZjI4NGQ0YWZmOGU1NGQ1ZTNmZGU5YjQyOSIsImlhdCI6MTc2NDI1Njk4OSwiZXhwIjoyMDc5NjE2OTg5fQ.-oQqmeEtQJj8j5BOye1wI7O-gye1JLcExxYOD8X3f5c"

headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json",
}

def main():
    # Récupère tous les états
    resp = requests.get(f"{BASE_URL}/api/states", headers=headers)
    resp.raise_for_status()
    entities = resp.json()

    # Regroupe par domaine
    domains = {}
    for e in entities:
        entity_id = e["entity_id"]
        domain = entity_id.split(".")[0]
        domains.setdefault(domain, []).append(entity_id)

    # Écrit la sortie dans /config/entities_export.yaml
    out_path = "/config/entities_export.yaml"
    with open(out_path, "w", encoding="utf-8") as f:
        for domain, ents in sorted(domains.items()):
            f.write(f"{domain}:\n")
            for ent in sorted(ents):
                f.write(f"  - {ent}\n")
            f.write("\n")

    print(f"Export terminé → {out_path}")

if __name__ == "__main__":
    main()