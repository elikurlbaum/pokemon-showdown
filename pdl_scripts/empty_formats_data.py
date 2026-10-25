
from pathlib import Path
import re

INPUT_FILE = Path(
    "/Users/elikurlbaum/showdown/pokemon-showdown/data/mods/champions/formats-data.ts"
)

OUTPUT_FILE = Path(
    "/Users/elikurlbaum/showdown/pokemon-showdown/data/mods/pdl/formats-data.ts"
)

source = INPUT_FILE.read_text(encoding="utf-8")

# Find the exported FormatsData object.
match = re.search(r"\bFormatsData\s*:[^=]*=\s*\{", source)
if not match:
    match = re.search(r"\bFormatsData\s*=\s*\{", source)

if not match:
    raise RuntimeError("Could not find FormatsData object.")

# Extract Pokémon keys from the top-level object.
opening = source.find("{", match.start())

depth = 0
closing = None
for i in range(opening, len(source)):
    if source[i] == "{":
        depth += 1
    elif source[i] == "}":
        depth -= 1
        if depth == 0:
            closing = i
            break

if closing is None:
    raise RuntimeError("Could not find closing brace for FormatsData.")

body = source[opening + 1:closing]

pokemon = re.findall(
    r"(?m)^\s{0,8}([a-zA-Z0-9_-]+)\s*:\s*\{",
    body,
)

if not pokemon:
    raise RuntimeError("No Pokémon found; output was not written.")

# Remove duplicates while preserving order.
pokemon = list(dict.fromkeys(pokemon))

# Generate empty objects for every Pokémon.
lines = [
    "export const FormatsData: import('../../../sim/dex-species').ModdedSpeciesFormatsDataTable = {"
]

for name in pokemon:
    lines.append(f"    {name}: {{}},")
    
lines.extend(["};", ""])

OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")

print(f"Pokémon entries written: {len(pokemon)}")
print(f"Output: {OUTPUT_FILE}")
