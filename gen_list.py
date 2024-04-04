import os

with open('README.md', 'w') as wf:
    wf.write('# Paper List\n')
    ym = None
    for i in sorted(os.listdir(), reverse=True):
        if i == 'README.md' or i.endswith('.py'):
            continue
        if not ym or ym != i.split('.')[0]:
            ym = i.split('.')[0]
            wf.write(f'## {ym}\n')

        with open(i, 'r') as f2:
            title = f2.readline().strip()[2:]
            wf.write(f'#### [{title}]({i})\n')