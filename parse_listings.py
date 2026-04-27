import re
from pathlib import Path
from collections import Counter
text = Path('매물목록.txt').read_text(encoding='utf-8')
entries = [e.strip() for e in re.split(r'\n\s*\n', text) if e.strip()]
print('entries', len(entries))
pattern = re.compile(r'집주인([^\n]+)')
for name, count in Counter(pattern.match(e.splitlines()[0].strip()).group(1).strip() if pattern.match(e.splitlines()[0].strip()) else 'UNKNOWN' for e in entries).most_common():
    print(name, count)
print('--- sample entries ---')
for e in entries[:10]:
    first = e.splitlines()[0].strip()
    name = pattern.match(first).group(1).strip() if pattern.match(first) else 'UNKNOWN'
    price = re.search(r'매매\s*([0-9억,]+)', e)
    layout = re.search(r'아파트([^,\n]+)', e)
    desc = e.splitlines()[3].strip() if len(e.splitlines()) > 3 else ''
    date = re.search(r'확인매물\s*([0-9.]+)', e)
    print(name, price.group(1) if price else '', layout.group(1).strip() if layout else '', desc, date.group(1) if date else '')
