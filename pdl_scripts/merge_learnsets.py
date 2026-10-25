
import re
from pathlib import Path

CHAMPIONS_FILE = Path("data/mods/champions/learnsets.backup.ts")
NATIONAL_FILE = Path("data/learnsets.backup.ts")
OUTPUT_FILE = Path("data/mods/pdl/learnsets.ts")


def find_matching_brace(text, opening):
    """Find the matching closing brace, ignoring strings and comments."""
    depth = 0
    i = opening
    state = "normal"

    while i < len(text):
        c = text[i]
        nxt = text[i + 1] if i + 1 < len(text) else ""

        if state == "line_comment":
            if c == "\n":
                state = "normal"
        elif state == "block_comment":
            if c == "*" and nxt == "/":
                state = "normal"
                i += 1
        elif state in ("single", "double", "template"):
            quote = {"single": "'", "double": '"', "template": "`"}[state]
            if c == "\\":
                i += 1
            elif c == quote:
                state = "normal"
        elif c == "/" and nxt == "/":
            state = "line_comment"
            i += 1
        elif c == "/" and nxt == "*":
            state = "block_comment"
            i += 1
        elif c == "'":
            state = "single"
        elif c == '"':
            state = "double"
        elif c == "`":
            state = "template"
        elif c == "{":
            depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                return i

        i += 1

    raise ValueError(f"No matching closing brace at position {opening}")


def extract_object(text, opening):
    closing = find_matching_brace(text, opening)
    return text[opening + 1:closing], closing


def parse_learnsets(path):
    """Return Pokémon names and their original complete object blocks."""
    source = path.read_text(encoding="utf-8")

    declaration = re.search(r"\bLearnsets\s*:[^=]*=\s*\{", source)
    if not declaration:
        declaration = re.search(r"\bLearnsets\s*=\s*\{", source)

    if not declaration:
        raise ValueError(f"Could not find Learnsets object in {path}")

    opening = source.find("{", declaration.start())
    body, _ = extract_object(source, opening)

    pokemon = {}
    pos = 0

    while pos < len(body):
        match = re.search(
            r"(?m)^\s*([a-zA-Z0-9_-]+)\s*:\s*\{",
            body[pos:],
        )
        if not match:
            break

        name = match.group(1)
        object_opening = pos + match.end() - 1
        object_body, object_closing = extract_object(body, object_opening)

        if re.search(r"\blearnset\s*:", object_body):
            # Preserve the complete Pokémon object, including all original moves.
            pokemon[name] = body[object_opening:object_closing + 1]

        pos = object_closing + 1

    return pokemon


def main():
    champions = parse_learnsets(CHAMPIONS_FILE)
    national = parse_learnsets(NATIONAL_FILE)

    print(f"Champions Pokémon parsed: {len(champions)}")
    print(f"National Dex Pokémon parsed: {len(national)}")

    if not champions or not national:
        raise RuntimeError("Parsing failed; output was NOT written.")

    # Start with Champions unchanged. Only add entirely missing Pokémon.
    merged = dict(champions)
    added_pokemon = 0

    for name, block in national.items():
        if name not in merged:
            merged[name] = block
            added_pokemon += 1

    if len(merged) < len(champions):
        raise RuntimeError("Merged count is too small; output was NOT written.")

    if "archaludon" in champions:
        if "bodypress:" in champions["archaludon"]:
            print("Champions Archaludon already contains Body Press.")
        else:
            print("Champions Archaludon does not contain Body Press.")
            if "bodypress:" in merged["archaludon"]:
                print("Body Press was unexpectedly found in the preserved block.")

    # Write the preserved Pokémon blocks without reconstructing their moves.
    lines = [
        "export const Learnsets: import('../../../sim/dex-species').ModdedLearnsetDataTable = {"
    ]

    for name, block in merged.items():
        # Normalize outer indentation while preserving the block's contents.
        block_lines = block.splitlines()
        lines.append(f"    {name}: {{")

        for line in block_lines[1:-1]:
            lines.append("    " + line.strip() if line.strip() else "")

        lines.append("    },")

    lines.extend(["};", ""])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print(f"\nMerged Pokémon: {len(merged)}")
    print(f"Added Pokémon from National Dex: {added_pokemon}")
    print("Existing Champions learnsets were not supplemented with National Dex moves.")
    print(f"Output written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
