import re
import csv

def md_table_to_csv(md_path, csv_path, target_header=None):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    rows = []
    capturing = False
    header_added = False

    for line in lines:
        is_table_line = line.strip().startswith('|')
        
        if not capturing:
            if is_table_line and (target_header is None or target_header in line):
                capturing = True
                if not re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                    if not header_added:
                        cells = [c.strip() for c in line.strip().strip('|').split('|')]
                        rows.append(cells)
                        header_added = True
        else:
            if is_table_line:
                if not re.match(r'^\|[\s\-:|]+\|$', line.strip()):
                    cells = [c.strip() for c in line.strip().strip('|').split('|')]
                    rows.append(cells)
            else:
                capturing = False

    with open(csv_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerows(rows)

md_table_to_csv('mapping/control-traceability-matrix.md', 'mapping/control-traceability-matrix.csv', 'Safeguard ID | Policy | Safeguard Summary')
# md_table_to_csv('register/exception-log.md', 'register/exception-log.csv')
# md_table_to_csv('register/review-cadence-tracker.md', 'register/review-cadence-tracker.csv')