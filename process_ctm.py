import re

with open('mapping/control-traceability-matrix.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_lines = []
skip_mode = False
for line in lines:
    if line.startswith('> **Note on'):
        continue # Skip generation-history commentary
    if line.startswith('**Generated:**') or line.startswith('**Source:**'):
        continue
    if line.startswith('**Version:** 2.1'):
        new_lines.append('**Version:** XX\n')
        continue
        
    new_lines.append(line)

text = "".join(new_lines)
# Remove extra newlines where we deleted comments
text = re.sub(r'\n{3,}', '\n\n', text)

# Table header fix
# Old: | Safeguard ID | Policy | Safeguard Summary | ISO 27001 Ref | NIST CSF Ref | PCI DSS Ref | DPDP Act Ref | GDPR Ref | Notes |
# New: | Control ID | Policy / Control | Objective | ISO/IEC 27001:2022 | NIST CSF 2.0 | PCI DSS v4.0.1 | DPDP Act / Rules | GDPR | Evidence / Rationale | Status |
text = text.replace('| Safeguard ID | Policy | Safeguard Summary | ISO 27001 Ref | NIST CSF Ref | PCI DSS Ref | DPDP Act Ref | GDPR Ref | Notes |',
                    '| Control ID | Policy / Control | Objective | ISO/IEC 27001:2022 | NIST CSF 2.0 | PCI DSS v4.0.1 | DPDP Act / Rules | GDPR | Evidence / Rationale | Status |')
text = text.replace('| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |',
                    '| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |')

# Process rows
corrected_controls = ['BC-06', 'BC-08', 'DC-08', 'IR-06', 'VR-05', 'VR-08', 'VR-10']

final_text_lines = []
for line in text.split('\n'):
    if line.startswith('| ') and not line.startswith('| Control ID |') and not line.startswith('| :--- |') and not line.startswith('| Column |'):
        # It's a data row. Could be in a main table or summary table.
        parts = [p.strip() for p in line.split('|')][1:-1]
        
        # If it's a main CTM row, it has 9 columns originally.
        if len(parts) == 9:
            ctrl_id = parts[0]
            notes = parts[8]
            status = 'Confirmed'
            if ctrl_id in corrected_controls:
                status = 'Corrected'
            
            if 'Review' in notes:
                status = 'Review Required'
                notes = notes.replace('Review - ', '').strip()
            
            if notes == '-' or notes == '':
                notes = '-'
            
            new_line = f"| {parts[0]} | {parts[1]} | {parts[2]} | {parts[3]} | {parts[4]} | {parts[5]} | {parts[6]} | {parts[7]} | {notes} | {status} |"
            final_text_lines.append(new_line)
        elif len(parts) == 6 and 'With DPDP Act Ref' in line:
            # Summary table header
            final_text_lines.append(line.replace('With DPDP Act Ref', 'With DPDP Act / Rules Ref'))
        elif len(parts) == 4 and 'Version' in line:
            final_text_lines.append(line)
        elif len(parts) == 4 and 'Initial skeleton matrix.' in line:
            # Change real date to DD.MM.YY if not already
            final_text_lines.append('| 1.0 | DD.MM.YY | Compliance Lead / IT Security Lead | Initial skeleton matrix. |')
        elif len(parts) == 4 and 'Full rebuild' in line:
            final_text_lines.append('| 2.0 | DD.MM.YY | IT Security Lead | Full rebuild - all 83 safeguard IDs extracted and mapped from final policy files; Review flags added; cross-references linked. |')
        elif len(parts) == 4 and 'Applied audit corrections' in line:
            final_text_lines.append('| 2.1 | DD.MM.YY | Compliance Lead | Applied audit corrections (BC-08, IR-06, VR-05, VR-08, BC-06, VR-10); removed resolved review flags. |')
        else:
            final_text_lines.append(line)
    else:
        final_text_lines.append(line)

final_text = '\n'.join(final_text_lines)

# Fix table description
final_text = final_text.replace('Safeguard ID', 'Control ID')
final_text = final_text.replace('Safeguard Summary', 'Objective')

with open('mapping/control-traceability-matrix.md', 'w', encoding='utf-8') as f:
    f.write(final_text)
