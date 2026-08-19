with open('mapping/control-traceability-matrix.md', 'r', encoding='utf-8') as f:
    c = f.read()
c = c.replace('India DPDP Act 2025', 'India DPDP Act 2023 / Rules 2025')
with open('mapping/control-traceability-matrix.md', 'w', encoding='utf-8') as f:
    f.write(c)
