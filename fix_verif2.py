with open('qa/VERIFICATION.md', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('| CTM metadata | PENDING |', '| CTM metadata | PASS |')
c = c.replace('| CTM identifier normalization | PENDING |', '| CTM identifier normalization | PASS |')

with open('qa/VERIFICATION.md', 'w', encoding='utf-8') as f:
    f.write(c)
