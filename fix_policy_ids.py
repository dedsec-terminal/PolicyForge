def replace_in_file(path, old, new):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    c = c.replace(old, new)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)

replace_in_file('policies/vendor-third-party-risk.md', '| **Policy ID** | VD |', '| **Policy ID** | VR |')
replace_in_file('policies/password-authentication.md', '| **Policy ID** | PW |', '| **Policy ID** | PA |')
