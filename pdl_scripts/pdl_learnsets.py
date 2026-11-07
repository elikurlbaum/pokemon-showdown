
import re
import shutil
import textwrap
from pathlib import Path

ROOT = Path("/Users/elikurlbaum/showdown/pokemon-showdown")

CHAMPIONS_FILE = ROOT / "data/mods/champions/learnsets.ts"
CHAMPIONS_BACKUP = ROOT / "data/mods/champions/learnsets.backup.ts"
NATIONAL_FILE = ROOT / "data/learnsets.ts"
OUTPUT_FILE = ROOT / "data/mods/pdl/learnsets.ts"


def find_matching_brace(text, opening):
    """Find matching closing brace, ignoring strings and comments."""
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
            quote = {
                "single": "'",
                "double": '"',
                "template": "`",
            }[state]

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


def find_matching_array_bracket(text, opening):
    """Find matching closing bracket, respecting strings and comments."""
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
            quote = {
                "single": "'",
                "double": '"',
                "template": "`",
            }[state]

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

        elif c == "[":
            depth += 1

        elif c == "]":
            depth -= 1
            if depth == 0:
                return i

        i += 1

    raise ValueError(f"No matching closing bracket at position {opening}")


def extract_object(text, opening):
    closing = find_matching_brace(text, opening)
    return text[opening + 1:closing], closing


def parse_learnsets(path):
    """Return Pokémon names and their complete original object blocks."""
    source = path.read_text(encoding="utf-8")

    declaration = re.search(
        r"\bLearnsets\s*(?::[^=]*)?=\s*\{",
        source
    )

    if not declaration:
        raise ValueError(f"Could not find Learnsets object in {path}")

    opening = source.find("{", declaration.start())
    body, _ = extract_object(source, opening)

    pokemon = {}
    pos = 0

    while pos < len(body):
        match = re.search(
            r"(?m)^\s*([a-zA-Z0-9_-]+)\s*:\s*\{",
            body[pos:]
        )

        if not match:
            break

        name = match.group(1)
        object_opening = pos + match.end() - 1

        object_body, object_closing = extract_object(
            body, object_opening
        )

        if re.search(r"\blearnset\s*:", object_body):
            pokemon[name] = body[
                object_opening:object_closing + 1
            ]

        pos = object_closing + 1

    return pokemon


def remove_event_data(content):
    """Remove complete eventData arrays, including nested objects."""
    count = 0

    while True:
        match = re.search(
            r"(?m)^[ \t]*eventData\s*:\s*\[",
            content
        )

        if not match:
            break

        bracket_start = content.index("[", match.start())
        bracket_end = find_matching_array_bracket(
            content, bracket_start
        )

        # Remove the property, array, and trailing comma.
        end = bracket_end + 1

        while end < len(content) and content[end] in " \t":
            end += 1

        if end < len(content) and content[end] == ",":
            end += 1

        if end < len(content) and content[end] == "\r":
            end += 1

        if end < len(content) and content[end] == "\n":
            end += 1

        content = content[:match.start()] + content[end:]
        count += 1

    return content, count


def clean_learnsets(content):
    """Apply all learnset cleanup operations."""

    # 1. Remove frustration
    content, frustration_count = re.subn(
        r"(?m)^[ \t]*frustration\s*:\s*\[[^\]]*\],?\s*\n?",
        "",
        content
    )

    # 2. Remove hiddenpower
    content, hiddenpower_count = re.subn(
        r"(?m)^[ \t]*hiddenpower\s*:\s*\[[^\]]*\],?\s*\n?",
        "",
        content
    )

    # 3. Replace every move learnset array with ["9M"]
    # EventData is removed first so its moves arrays aren't modified.
    content, event_data_count = remove_event_data(content)

    move_array_count = 0

    content, move_array_count = re.subn(
        r"(?m)^([ \t]*[a-zA-Z0-9_-]+\s*:\s*)\[[^\]\n]*\](,?[ \t]*)$",
        r'\1["9M"]\2',
        content
    )

    # 4. Remove eventOnly properties
    content, event_only_count = re.subn(
        r"(?m)^[ \t]*eventOnly\s*:\s*(?:true|false),?[ \t]*\n?",
        "",
        content
    )

    return content, {
        "frustration": frustration_count,
        "hiddenpower": hiddenpower_count,
        "move_arrays": move_array_count,
        "eventData": event_data_count,
        "eventOnly": event_only_count,
    }


def main():
    # Step 1: Back up original Champions learnsets
    shutil.copy2(CHAMPIONS_FILE, CHAMPIONS_BACKUP)

    # Step 2: Parse both source files
    champions = parse_learnsets(CHAMPIONS_BACKUP)
    national = parse_learnsets(NATIONAL_FILE)

    print(f"Champions Pokémon parsed: {len(champions)}")
    print(f"National Dex Pokémon parsed: {len(national)}")

    if not champions or not national:
        raise RuntimeError(
            "Parsing failed; output was NOT written."
        )

    # Step 3: Start with Champions unchanged.
    # Only add entirely missing Pokémon from National Dex.
    merged = dict(champions)
    added_pokemon = 0

    for name, block in national.items():
        if name not in merged:
            merged[name] = block
            added_pokemon += 1

    if len(merged) < len(champions):
        raise RuntimeError(
            "Merged count is too small; output was NOT written."
        )

    # Step 4: Reconstruct merged Learnsets file
    lines = [
        "export const Learnsets: import('../../../sim/dex-species').ModdedLearnsetDataTable = {"
    ]

    for name, block in merged.items():
        block_inner = block[1:-1]
        block_inner = textwrap.dedent(block_inner).strip("\n")

        lines.append(f"    {name}: {{")

        if block_inner:
            for line in block_inner.splitlines():
                lines.append(
                    "        " + line if line.strip() else ""
                )

        lines.append("    },")

    lines.extend(["};", ""])

    merged_content = "\n".join(lines)

    # Step 5: Clean the merged learnsets
    cleaned_content, counts = clean_learnsets(merged_content)

    # Step 6: Write final PDL learnsets
    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(
        cleaned_content,
        encoding="utf-8"
    )

    # Step 7: Summary
    print("\n========== MERGE SUMMARY ==========")
    print(f"Champions Pokémon preserved: {len(champions)}")
    print(f"National Dex Pokémon added: {added_pokemon}")
    print(f"Total merged Pokémon: {len(merged)}")

    print("\n========== CLEANUP SUMMARY ==========")
    print(f"Removed frustration entries: {counts['frustration']}")
    print(f"Removed hiddenpower entries: {counts['hiddenpower']}")
    print(f"Normalized move arrays: {counts['move_arrays']}")
    print(f"Removed eventData arrays: {counts['eventData']}")
    print(f"Removed eventOnly properties: {counts['eventOnly']}")

    print("\n========== OUTPUT ==========")
    print(f"Champions backup: {CHAMPIONS_BACKUP}")
    print(f"Final output: {OUTPUT_FILE}")
    print("Existing Champions learnsets were not supplemented.")
    print("Learnsets processing completed successfully!")


if __name__ == "__main__":
    main()
