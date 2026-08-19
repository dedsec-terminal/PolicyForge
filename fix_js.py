with open('docs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

s1 = "var filename = href.split('/').pop();"
s2 = "var targetDoc = registry.find(function(d) { return d.src.endsWith('/' + filename) || d.src === filename; });"

if s1 in html and s2 in html:
    html = html.replace(s1, "")
    html = html.replace(s2, "var targetDoc = registry.find(function(d) { return d.src === href || '/' + d.src === href.replace(/\.\.\//g, '/') || d.src.endsWith(href.split('/').pop()) && false; /* strict matching */ });")
    html = html.replace("&& false;", "/* no basename */")
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
