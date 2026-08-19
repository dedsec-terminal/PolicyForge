import glob

for ext in ['**/*.md', '**/*.csv']:
    for fpath in glob.glob(ext, recursive=True):
        if 'qa/' in fpath:
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = c.replace('DPDPA Sec', 'DPDP Act 2023 Sec')
        c = c.replace('DPDPA rules', 'DPDP Rules 2025')
        c = c.replace('DPDPA rules', 'DPDP Rules')
        c = c.replace('GDPR/DPDPA Article 32', 'GDPR Article 32 / DPDP Act 2023')
        c = c.replace('DPDPA', 'DPDP Act 2023')
        
        # Clean up any duplicated 'DPDP Act 2023 Act 2023' that might have occurred
        c = c.replace('DPDP Act 2023 2023', 'DPDP Act 2023')
        c = c.replace('DPDP Act 2023 Act 2023', 'DPDP Act 2023')
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
