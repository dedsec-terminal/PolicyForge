import re

with open('docs/index.html', 'r', encoding='utf-8') as f:
    html = f.read()

old_logic = "var filename = href.split('/').pop();\n          var targetDoc = registry.find(function(d) { return d.src.endsWith('/' + filename) || d.src === filename; });"
new_logic = """// Resolve target document precisely by matching the exact source path
          // Since relative paths might include '../', we normalize it or match against known src paths.
          var targetDoc = registry.find(function(d) { 
              // Basic normalization for simple relative paths
              var cleanHref = href.replace(/^(\.\.\/)+/, '').replace(/^(\.\/)+/, '');
              return d.src.endsWith(cleanHref); 
          });"""

if old_logic in html:
    html = html.replace(old_logic, new_logic)
    with open('docs/index.html', 'w', encoding='utf-8') as f:
        f.write(html)
        print("Updated router basename logic")
