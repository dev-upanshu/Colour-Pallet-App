
import random
import colorsys
import json
from pathlib import Path

# ==========================================
# CHROMA - 1000 PALETTE GENERATOR
# ==========================================

BASE_DIR = Path(__file__).resolve().parent
APP_FILE = BASE_DIR / "src" / "app.js"

PALETTE_COUNT = 1000
COLORS_PER_PALETTE = 5
RANDOM_SEED = 20261105

rng = random.Random(RANDOM_SEED)

ADJECTIVES = [
    "Neon", "Cyber", "Cosmic", "Solar", "Lunar", "Astral",
    "Electric", "Quantum", "Plasma", "Aether", "Velvet",
    "Silk", "Satin", "Cashmere", "Chiffon", "Brocade",
    "Denim", "Canvas", "Leather", "Flannel", "Rustic",
    "Vintage", "Retro", "Antique", "Classic", "Modern",
    "Minimal", "Industrial", "Boho", "Zen", "Tropical",
    "Arctic", "Alpine", "Desert", "Savanna", "Tundra",
    "Jungle", "Canyon", "Oasis", "Glacial", "Golden",
    "Silver", "Bronze", "Copper", "Platinum", "Titanium",
    "Chrome", "Steel", "Iron", "Amber", "Crimson",
    "Scarlet", "Ruby", "Coral", "Blush", "Rose",
    "Mauve", "Lavender", "Violet", "Indigo", "Sapphire",
    "Cobalt", "Azure", "Cyan", "Teal", "Emerald",
    "Jade", "Mint", "Olive", "Sage", "Lemon",
    "Citrus", "Tangerine", "Peach", "Apricot", "Pumpkin",
    "Cinnamon", "Mocha", "Espresso", "Caramel"
]

NOUNS = [
    "Dream", "Vision", "Mirage", "Fantasy", "Illusions",
    "Echo", "Shadows", "Spectrum", "Prism", "Aurora",
    "Sunset", "Sunrise", "Twilight", "Dusk", "Dawn",
    "Horizon", "Eclipse", "Solstice", "Equinox", "Galaxy",
    "Nebula", "Supernova", "Meteor", "Comet", "Orbit",
    "Voyage", "Journey", "Odyssey", "Quest", "Expedition",
    "Breeze", "Storm", "Cyclone", "Monsoon", "Tempest",
    "Zephyr", "Whirlwind", "Cascade", "Waterfall", "River",
    "Ocean", "Abyss", "Trench", "Lagoon", "Atoll",
    "Archipelago", "Island", "Cove", "Harbor", "Bay",
    "Summit", "Peak", "Ridge", "Cliff", "Valley",
    "Canyon", "Plateau", "Glacier", "Iceberg", "Forest",
    "Grove", "Thicket", "Meadow", "Prairie", "Desert",
    "Dune", "Empire", "Kingdom", "Dynasty", "Realm",
    "Sanctuary", "Haven", "Temple", "Palace", "Citadel",
    "Fortress"
]


def hsl_to_hex(h, s, l):
    """Convert HSL values into a HEX colour."""
    r, g, b = colorsys.hls_to_rgb(h, l, s)

    return "#{:02X}{:02X}{:02X}".format(
        round(r * 255),
        round(g * 255),
        round(b * 255)
    )


def generate_palette():
    """Generate five colours with a shared hue and varying lightness."""

    hue = rng.random()

    saturation = rng.uniform(0.45, 0.85)

    palette = []

    # Five progressive lightness levels
    lightness_levels = [0.18, 0.32, 0.48, 0.66, 0.84]

    for level in lightness_levels:
        adjusted_lightness = max(
            0.10,
            min(0.92, level + rng.uniform(-0.035, 0.035))
        )

        adjusted_saturation = max(
            0.35,
            min(0.95, saturation + rng.uniform(-0.08, 0.08))
        )

        palette.append(
            hsl_to_hex(
                hue,
                adjusted_saturation,
                adjusted_lightness
            )
        )

    return palette


def generate_name(index, used_names):
    """Generate a unique palette name."""

    adjective = rng.choice(ADJECTIVES)
    noun = rng.choice(NOUNS)

    base_name = f"{adjective} {noun}"
    name = base_name

    suffix = 2

    while name in used_names:
        name = f"{base_name} {suffix}"
        suffix += 1

    used_names.add(name)

    return name


def generate_palettes():
    """Create the requested number of palettes."""

    results = []
    used_names = set()

    print("Generating CHROMA palettes...")

    for index in range(PALETTE_COUNT):
        name = generate_name(index, used_names)
        colors = generate_palette()

        results.append({
            "name": name,
            "colors": colors
        })

    return results


def inject_into_app(palettes):
    """Safely replace the old generated section in app.js."""

    if not APP_FILE.exists():
        raise FileNotFoundError(
            f"Application file not found: {APP_FILE}"
        )

    source = APP_FILE.read_text(encoding="utf-8")

    marker = "let palettes = seed.map"

    if marker not in source:
        raise RuntimeError(
            "Could not find palette insertion point in src/app.js"
        )

    start_marker = "// --- CHROMA GENERATED PALETTES START ---"
    end_marker = "// --- CHROMA GENERATED PALETTES END ---"

    # Remove the previous generated section if present
    if start_marker in source and end_marker in source:
        start = source.index(start_marker)
        end = source.index(end_marker) + len(end_marker)

        source = (
            source[:start] +
            source[end:]
        )

    # Generate JavaScript source safely
    lines = [
        "",
        start_marker,
        "seed.push("
    ]

    for palette in palettes:
        name = json.dumps(palette["name"])
        colors = json.dumps(palette["colors"])

        lines.append(
            f"  [{name}, {colors}],"
        )

    lines.extend([
        ");",
        end_marker,
        ""
    ])

    generated_code = "\n".join(lines)

    source = source.replace(
        marker,
        generated_code + "\n" + marker,
        1
    )

    APP_FILE.write_text(source, encoding="utf-8")

    print(f"Successfully added {len(palettes)} palettes!")
    print(f"Updated: {APP_FILE}")


def main():
    print("=" * 45)
    print("       CHROMA PALETTE GENERATOR")
    print("=" * 45)

    palettes = generate_palettes()

    inject_into_app(palettes)

    print()
    print("Palette generation completed.")
    print("Total new palettes:", len(palettes))
    print("Colours per palette:", COLORS_PER_PALETTE)


if __name__ == "__main__":
    main()
