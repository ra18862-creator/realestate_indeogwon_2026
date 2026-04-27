import re
from pathlib import Path
from collections import defaultdict
import json

text = Path('매물목록.txt').read_text(encoding='utf-8')
blocks = [b.strip() for b in re.split(r'(?=집주인)', text) if b.strip()]
print('blocks', len(blocks))
complex_data = defaultdict(list)
for b in blocks:
    lines = [line.strip() for line in b.splitlines() if line.strip()]
    if not lines:
        continue
    header = lines[0]
    m = re.match(r'집주인(.+?)\s*(\d{1,3}동)?$', header)
    if m:
        name = m.group(1).strip()
        dong = m.group(2)
    else:
        tokens = header.replace('집주인','').strip().split()
        name = tokens[0] if tokens else 'UNKNOWN'
        dong = None
    price = None
    layout = None
    date = None
    direction = None
    floor = None
    size = None
    desc = None
    for line in lines[1:]:
        if price is None:
            pm = re.search(r'매매\s*([0-9억,\s]+)', line)
            if pm:
                price = pm.group(1)
        if layout is None:
            lm = re.search(r'아파트([^,\n]+)', line)
            if lm:
                layout = lm.group(1).strip()
                # Extract size, floor, direction from layout
                layout_parts = layout.split('/')
                if len(layout_parts) > 1:
                    size = layout_parts[1].replace('m²', '').strip()
                floor_match = re.search(r'(\d+)/(\d+)층', line)
                if floor_match:
                    floor = f"{floor_match.group(1)}/{floor_match.group(2)}"
                dir_match = re.search(r'(남|북|동|서|남동|남서|북동|북서)향', line)
                if dir_match:
                    direction = dir_match.group(1)
        if date is None:
            dm = re.search(r'확인매물\s*([0-9.]+)', line)
            if dm:
                date = dm.group(1)
        if desc is None and not any(keyword in line for keyword in ['매매', '아파트', '확인매물', '제공', '공인중개사']):
            desc = line
    complex_data[name].append({
        'price': price,
        'layout': layout,
        'size': size,
        'floor': floor,
        'direction': direction,
        'date': date,
        'desc': desc,
        'dong': dong,
        'lines': lines
    })

# Save to JSON
with open('listings.json', 'w', encoding='utf-8') as f:
    json.dump(dict(complex_data), f, ensure_ascii=False, indent=2)

print("Data saved to listings.json")
