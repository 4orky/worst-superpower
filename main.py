# The Worst Superpower — make.fun bounty
# u-suroto-worst-superpower-461dcdbe
#
# The program writes one invented superpower (1-140 characters) to
# /output/entry.txt: a power so pointless that naming it is the whole joke.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. genuinely useless — the worst, most pointless power imaginable,
#      stated in one line (a real, useful or merely weak power loses)
#   2. the uselessness lands as a joke — picture it in use and laugh at
#      how little it achieves
#   3. unexpected — not slow flight, not invisible-while-nobody-watches
#   4. tight and specific, with a concrete detail that fixes the power
#      in the world
#   5. clear on a single reading, no setup beyond the sentence itself
# A power that is really a curse, or that quietly helps, is not a useless
# superpower. Each candidate carries a hand-scored craft score (0-10 per
# criterion, summed below); selection is deterministic: highest score wins,
# ties go to the shorter text. The output is byte-identical on every run.

CANDIDATES = [
    # score: useless 10, funny 9, fresh 8, tight 10, clear 10 = 47
    # REVISED (2nd pass): "provided it is already in my hand" was stiff
    # and legalistic; "but only if" lands the self-defeating condition
    # in spoken rhythm, so the joke hits in the same breath as the power.
    ("I can summon any object in the world, but only if it is already "
     "in my hand.",
     47),
    # score: useless 10, funny 9, fresh 9, tight 9, clear 10 = 47
    ("I can speak every language on Earth fluently — but only to "
     "people who already speak mine.",
     47),
    # score: useless 10, funny 9, fresh 8, tight 9, clear 10 = 46
    ("I can teleport anywhere in the world — as long as it is exactly "
     "where I am standing right now.",
     46),
    # score: useless 10, funny 9, fresh 8, tight 10, clear 9 = 46
    ("I can freeze time for one perfect second. I already used it.",
     46),
    # score: useless 10, funny 9, fresh 10, tight 8, clear 9 = 46
    ("I can talk to fish — but only the ones in the supermarket "
     "freezer, and so far none of them has answered.",
     46),
    # score: useless 10, funny 9, fresh 8, tight 9, clear 10 = 46
    ("I can predict the future with perfect accuracy, but only events "
     "that already happened yesterday.",
     46),
    # score: useless 9, funny 9, fresh 9, tight 10, clear 10 = 46
    ("I know exactly what everyone wants for Christmas — on "
     "December 26th.",
     46),
    # score: useless 9, funny 9, fresh 9, tight 9, clear 9 = 45
    ("I can heal any wound instantly — but only paper cuts, and only "
     "the ones I got last Tuesday.",
     45),
    # score: useless 9, funny 9, fresh 9, tight 8, clear 9 = 44
    ("I can read minds — but only the minds of people who are "
     "currently wondering whether I can read minds.",
     44),
    # score: useless 9, funny 8, fresh 8, tight 9, clear 10 = 44
    ("I can hear a pin drop a mile away — but only while I am asleep.",
     44),
    # score: useless 9, funny 8, fresh 8, tight 9, clear 10 = 44
    ("I can see through walls — but only walls I have already walked "
     "around.",
     44),
    # score: useless 9, funny 8, fresh 8, tight 8, clear 9 = 42
    ("I can summon rain at will: one drop at a time, falling directly "
     "on my own head, even indoors.",
     42),
]

# The gate requires 1-140 characters of non-whitespace UTF-8 text.
# Banned: the judge's own named clichés and anything that reads as a
# curse or as secretly useful.
BANNED_CLICHES = ("slow flight", "invisible while nobody",
                   "as an ai")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 140, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_CLICHES), \
            f"candidate uses a worn joke: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    message = pick(CANDIDATES)
    import os
    import sys
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(message)
    # Verify: read the output back byte-for-byte and re-check the gate,
    # so a partial write or an encoding slip fails loudly instead of
    # silently submitting a broken entry.
    with open("/output/entry.txt", "rb") as f:
        raw = f.read()
    if raw.decode("utf-8") != message:
        print("error: /output/entry.txt does not match the selected message",
              file=sys.stderr)
        sys.exit(1)
    if not (1 <= len(message) <= 140) or "\n" in message or not message.strip():
        print("error: selected message fails the gate (1-140 chars, one line)",
              file=sys.stderr)
        sys.exit(1)
    print(message)


if __name__ == "__main__":
    main()
