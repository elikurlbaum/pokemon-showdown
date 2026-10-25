
from pathlib import Path
import re

INPUT_FILE = Path("data/mods/champions/formats-data.ts")
OUTPUT_FILE = Path("data/mods/pdl/formats-data.ts")


def main():
    source = INPUT_FILE.read_text(encoding="utf-8")

    match = re.search(r"\bFormatsData\s*:[^=]*=\s*\{", source)
    if not match:
        match = re.search(r"\bFormatsData\s*=\s*\{", source)

    if not match:
        raise RuntimeError("Could not find FormatsData export.")

    opening = source.find("{", match.start())

    # Find the matching closing brace, ignoring strings and comments.
    depth = 0
    state = "normal"
    closing = None
    i = opening

    while i < len(source):
        c = source[i]
        nxt = source[i + 1] if i + 1 < len(source) else ""

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
                closing = i
                break

        i += 1

    if closing is None:
        raise RuntimeError("Could not find matching closing brace.")

    body = source[opening + 1:closing]

    # Extract Pokémon entries from the top-level object.
    pokemon = re.findall(
        r"(?m)^\s{0,8}([a-zA-Z0-9_-]+)\s*:\s*\{",
        body,
    )
    pokemon = list(dict.fromkeys(pokemon))

    if not pokemon:
        raise RuntimeError("No Pokémon found. Output was not written.")

    lines = [
        "export const FormatsData: import('../../../sim/dex-species').ModdedSpeciesFormatsDataTable = {"
    ]

    for name in pokemon:
        lines.append(f'    {name}: {{ tier: "OU" }},')

    lines.extend(["};", ""])

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

    print(f"Pokémon entries written: {len(pokemon)}")
    print(f"Output written to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
