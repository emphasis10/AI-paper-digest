import os

for i in os.listdir():
    path = i
    if not path.endswith('.md') or 'README' in path:
        continue
    with open(path) as f:
        lines = f.readlines()
    if 'https' in lines[3]:
        continue
    arxiv_id = '.'.join(i.split('.')[:-1])
    arxiv_link = f'https://arxiv.org/pdf/{arxiv_id}.pdf'
    lines = lines[:3] + [f'- [{arxiv_link}]({arxiv_link})\n\n'] + lines[3:]
    with open(path, 'w') as f:
        for line in lines:
            f.write(line)