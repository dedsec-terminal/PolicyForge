with open('scripts/md_to_csv.py', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace("'Safeguard ID | Policy | Safeguard Summary'", "'Control ID | Policy / Control | Objective'")
with open('scripts/md_to_csv.py', 'w', encoding='utf-8') as f:
    f.write(c)
