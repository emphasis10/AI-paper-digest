import os

with open('README.md', 'w') as wf:
    wf.write('# Paper List\n')
    ym = None
    for i in sorted(os.listdir('summaries'), reverse=True):
        i = os.path.join('summaries', i)
        if i == 'README.md' or i.endswith('.py') or os.path.isdir(i):
            continue
        if not ym or ym != i.split('/')[-1].split('.')[0]:
            ym = i.split('/')[-1].split('.')[0]
            wf.write(f'## {ym}\n')

        with open(i, 'r') as f2:
            title = f2.readline().strip()[2:]
            wf.write(f'#### [{title}]({i})\n')