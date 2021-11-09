import sys
from collections import namedtuple

Passage = namedtuple('Passage', ['title', 'destinations', 'newinfo'])
Destination = namedtuple('Destination', ['title', 'extra'])


def get_passages(lines):
    destinations = []
    title = None
    newinfo = False
    for line in lines:
        if line.startswith('::'):
            if title:
                yield Passage(title, destinations, newinfo)
            title = line.split('{')[0][2:].strip()
            destinations = []
            newinfo = False
        elif '[[' in line:
            line = line.replace('[[', '').split(']')[0]
            dest = line.split('->')[1].strip()
            destinations.append(Destination(dest, ""))
        elif '<<ask' in line:
            dest = line.split('"')[-2]
            destinations.append(Destination(dest, "[color=purple]"))
        elif 'newinfo' in line:
            newinfo = True

    yield Passage(title, destinations, newinfo)


def format(passages):
    print("""
digraph graphname {
""")
    for p in passages:
        if p.newinfo:
            print(f""""{p.title}" [color=orange, shape=box];""")
        for dest in p.destinations:
            print(f""""{p.title}" -> "{dest.title}" {dest.extra};""")
    print("}")


if __name__ == '__main__':
    with open(sys.argv[1]) as f:
        passages = get_passages(f.readlines())
        format(passages)
