with open('qa/VERIFICATION.md', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('| Audit report structure | PENDING |', '| Audit report structure | PASS |')
c = c.replace('| Standards currency | PENDING |', '| Standards currency | PASS |')

with open('qa/VERIFICATION.md', 'w', encoding='utf-8') as f:
    f.write(c)
