import glob

for ext in ['**/*.md', '**/*.csv']:
    for fpath in glob.glob(ext, recursive=True):
        with open(fpath, 'r', encoding='utf-8') as f:
            c = f.read()
        
        c = c.replace('DPDPA 2025', 'DPDP Act 2023')
        
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(c)
