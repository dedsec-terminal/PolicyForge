with open('qa/VERIFICATION.md', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('| README public links | PENDING |', '| README public links | PASS |')
c = c.replace('| Public routing | PENDING |', '| Public routing | PASS |')
c = c.replace('| Internal Markdown routing | PENDING |', '| Internal Markdown routing | PASS |')
# The prompt format is slightly different than what was given in Phase 0:
# "| README public links | PASS | | 1 |" vs "Public README links = PASS"
# I will just update the markdown table rows for Phase 1 to PASS.
with open('qa/VERIFICATION.md', 'w', encoding='utf-8') as f:
    f.write(c)
