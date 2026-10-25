
import re
from pathlib import Path

CHAMPIONS_FILE = Path("data/mods/champions/learnsets.ts")
NATIONAL_FILE = Path("data/learnsets.ts")
OUTPUT_FILE = Path("data/mods/pdl/learnsets.ts")


def find_matching_brace(text, opening):
    """Find the closing brace matching text[opening], ignoring strings/comments."""
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

    raise ValueError(f"No matching closing brace for position {opening}")


def extract_object(text, opening):
    closing = find_matching_brace(text, opening)
    return text[opening + 1:closing]


def parse_learnsets(path):
    source = path.read_text(encoding="utf-8")

    # Find the exported Learnsets object.
    declaration = re.search(r"\bLearnsets\s*:[^=]*=\s*\{", source)
    if not declaration:
        declaration = re.search(r"\bLearnsets\s*=\s*\{", source)

    if not declaration:
        raise ValueError(f"Could not find Learnsets object in {path}")

    opening = source.find("{", declaration.start())
    body = extract_object(source, opening)

    pokemon = {}
    pos = 0

    # Each Pokémon is a top-level property whose value is an object.
    while pos < len(body):
        match = re.search(
            r"(?m)^\s{0,8}([a-zA-Z0-9_-]+)\s*:\s*\{",
            body[pos:],
        )
        if not match:
            break

        name = match.group(1)
        object_opening = pos + match.end() - 1
        object_body = extract_object(body, object_opening)

        learnset_match = re.search(r"\blearnset\s*:\s*\{", object_body)
        if learnset_match:
            learnset_opening = object_body.find("{", learnset_match.start())
            learnset_body = extract_object(object_body, learnset_opening)

            moves = {}
            for line in learnset_body.splitlines():
                move_match = re.match(
                    r"^\s*([a-zA-Z0-9_-]+)\s*:\s*(.+?)\s*,?\s*$",
                    line,
                )
                if move_match:
                    move, value = move_match.groups()
                    moves[move] = value.rstrip(",")

            pokemon[name] = moves

        # Skip the entire Pokémon object to avoid matching nested properties.
        pos = object_opening + len(object_body) + 2

    return pokemon


def main():
    champions = parse_learnsets(CHAMPIONS_FILE)
    national = parse_learnsets(NATIONAL_FILE)

    print(f"Champions Pokémon parsed: {len(champions)}")
    print(f"National Dex Pokémon parsed: {len(national)}")

    # Never write an empty or suspiciously incomplete result.
    if not champions or not national:
        raise RuntimeError("Parsing failed; output was NOT written.")

    merged = {name: dict(moves) for name, moves in champions.items()}
    added_pokemon = 0
    added_moves = 0

    for name, national_moves in national.items():
        if name not in merged:
            merged[name] = dict(national_moves)
            added_pokemon += 1
            continue

        for move, value in national_moves.items():
            if move not in merged[name]:
                merged[name][move] = value
                added_moves += 1

    # Build the complete TypeScript output.
    lines = [
        "export const Learnsets: import('../../../sim/dex-species').ModdedLearnsetDataTable = {"
    ]

    for name, moves in merged.items():
        lines.append(f"    {name}: {{")
        lines.append("        learnset: {")

        for move, value in sorted(moves.items()):
            lines.append(f"            {move}: {value},")

        lines.extend(["        },", "    },"])

    lines.extend(["};", ""])

    output = "\n".join(lines)

    # Sanity checks before writing.
    if len(merged) < len(champions):
        raise RuntimeError("Merged count is smaller than Champions count.")
    if "venusaur" not in merged or not merged["venusaur"]:
        raise RuntimeError("Expected Venusaur learnset missing; output not written.")

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text(output, encoding="utf-8")

    print(f"\nMerged Pokémon: {len(merged)}")
    print(f"Added Pokémon from National Dex: {added_pokemon}")
    print(f"Added missing moves: {added_moves}")
    print(f"Output written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
