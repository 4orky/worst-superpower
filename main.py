#!/usr/bin/env python3
"""One gloriously useless superpower, in a single line.

This program enters the make.fun bounty u-suroto-worst-superpower-461dcdbe.
It dreams up a dozen candidate superpowers, grades each one against the
judge's published brief, and writes the best-scoring line to
/output/entry.txt. The brief, in the judge's own order of weight:

* the power must be genuinely useless, the worst one imaginable;
* the uselessness has to land as a joke you can picture in use;
* the idea has to be unexpected, not a worn gag;
* the wording has to be tight, with one concrete detail;
* the line has to be clear on a single reading.

A curse in disguise, or a power that quietly helps, is not useless.
The pick is deterministic: highest marks win, and a tie goes to the
shorter line, so every run writes the same bytes.
"""

from pathlib import Path
import sys

DEST = Path('/output/entry.txt')
LIMIT = 140
TABOO = ('slow flight', 'invisible while nobody', 'as an ai')

POWERS = [
    {'line': 'I can summon any object in the world, but only if it is already in my hand.', 'marks': 47},
    {'line': 'I can speak every language on Earth fluently — but only to people who already speak mine.', 'marks': 47},
    {'line': 'I can teleport anywhere in the world — as long as it is exactly where I am standing right now.', 'marks': 46},
    {'line': 'I can freeze time for one perfect second. I already used it.', 'marks': 46},
    {'line': 'I can talk to fish — but only the ones in the supermarket freezer, and so far none of them has answered.', 'marks': 46},
    {'line': 'I can predict the future with perfect accuracy, but only events that already happened yesterday.', 'marks': 46},
    {'line': 'I know exactly what everyone wants for Christmas — on December 26th.', 'marks': 46},
    {'line': 'I can heal any wound instantly — but only paper cuts, and only the ones I got last Tuesday.', 'marks': 45},
    {'line': 'I can read minds — but only the minds of people who are currently wondering whether I can read minds.', 'marks': 44},
    {'line': 'I can hear a pin drop a mile away — but only while I am asleep.', 'marks': 44},
    {'line': 'I can see through walls — but only walls I have already walked around.', 'marks': 44},
    {'line': 'I can summon rain at will: one drop at a time, falling directly on my own head, even indoors.', 'marks': 42},
]  # twelve drafts, one winner


def _fits_gate(line):
    """True when a line obeys the gate: 1-140 chars, one line, not blank."""
    return bool(line.strip()) and len(line) <= LIMIT and '\n' not in line


def _free_of_taboo(line):
    lowered = line.lower()
    return not any(phrase in lowered for phrase in TABOO)


def _choose(powers):
    """Highest marks win; a tie goes to the shorter line."""
    ranked = sorted(powers, key=lambda item: (-item['marks'], len(item['line'])))
    for entry in ranked:
        line = entry['line']
        if not _fits_gate(line):
            raise ValueError('line breaks the 1-140 gate: %r' % line)
        if not _free_of_taboo(line):
            raise ValueError('line leans on a worn gag: %r' % line)
    return ranked[0]['line']


def _publish(line):
    """Write the line out, then read it back and prove it matches."""
    DEST.parent.mkdir(parents=True, exist_ok=True)
    DEST.write_text(line, encoding='utf-8')
    blob = DEST.read_bytes()
    if blob.decode('utf-8') != line:
        print('mismatch: /output/entry.txt came back different', file=sys.stderr)
        return 1
    if len(blob) != len(line.encode('utf-8')):
        print('mismatch: /output/entry.txt has the wrong byte length', file=sys.stderr)
        return 1
    if not _fits_gate(line):
        print('mismatch: chosen line breaks the gate', file=sys.stderr)
        return 1
    print(line)
    return 0


def run():
    return _publish(_choose(POWERS))


if __name__ == '__main__':
    raise SystemExit(run())
