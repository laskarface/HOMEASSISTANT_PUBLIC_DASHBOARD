domains = {}

for entity_id in hass.states.entity_ids():
    domain = entity_id.split('.')[0]
    domains.setdefault(domain, []).append(entity_id)

output = "### ENTITIES BY DOMAIN ###\n\n"

for domain, entities in sorted(domains.items()):
    output += f"{domain}:\n"
    for e in entities:
        output += f"  - {e}\n"
    output += "\n"

logger.info("\n" + output)