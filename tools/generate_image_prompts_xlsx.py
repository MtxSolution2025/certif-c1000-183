#!/usr/bin/env python3
"""Generate c1000-183-image-prompts.xlsx — universal image prompts for SVG illustrations.

Universal format compatible with DALL-E 3, Flux Pro, Midjourney v6, Stable Diffusion XL.
Adapt platform-specific parameters (--ar, --style, --v) when copying into your generation tool.

Usage:
    cd ~/Desktop/certif-c1000-183
    python3 tools/generate_image_prompts_xlsx.py
"""

from __future__ import annotations

from pathlib import Path

from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.utils import get_column_letter


COLUMNS = [
    ("lesson_id", 18),
    ("image_path", 50),
    ("figure_type", 12),
    ("title_fr", 35),
    ("subject", 80),
    ("style", 50),
    ("composition", 60),
    ("color_palette", 55),
    ("lighting", 35),
    ("mood", 30),
    ("technical_directives", 55),
    ("negative_prompt", 70),
    ("references", 55),
    ("priority", 8),
    ("notes", 50),
]


# Lesson 3.1 — Configurer les options Organization (niveau Org)
PROMPTS = [
    {
        "lesson_id": "c1000-183-3-1",
        "image_path": "assets/illustrations/lesson-c1000-183-3-1.svg",
        "figure_type": "hero",
        "title_fr": "Architecture multi-Organization Maximo",
        "subject": (
            "Isometric architectural diagram showing 4 concentric data storage levels of IBM Maximo Manage: "
            "System level (outer ring), Set level (Item Set + Company Set), Organization level (entity boxes), "
            "Site level (innermost cubes representing physical locations). Two example Organizations rendered "
            "as labeled boxes (USORG with US flag accent and DEORG with Germany flag accent), each containing "
            "2-3 Site cubes underneath. Above the Org boxes, two cylinder shapes representing the shared Item "
            "Set and shared Company Set with arrows pointing down to both Orgs. No literal text labels — visual "
            "hierarchy speaks. Clean line-art with subtle depth shading."
        ),
        "style": (
            "Clean technical isometric illustration, vector-flat with soft depth shading, business-didactic, "
            "in the spirit of Stripe Press infographics or Linear's marketing diagrams"
        ),
        "composition": (
            "Centered composition. Top third: System level horizontal band (subtle blue tint). Middle third: "
            "two cylinders side by side for Item Set (teal) and Company Set (slate gray) with downward arrows. "
            "Lower middle: 2 Organization boxes (USORG amber-tinted, DEORG amber-tinted). Bottom: 4-5 Site cubes "
            "as foundation row (teal-tinted). Generous padding 80px around. Background subtle topographic line "
            "pattern at 5% opacity (Relvio brand element)."
        ),
        "color_palette": (
            "Primary teal #1D9E75 (Sets + Sites), accent amber #F59E0B (Organizations), info blue #3B82F6 "
            "(System level band), neutral slate #475569 for arrows and labels, white #FFFFFF background, "
            "subtle topographic teal #1D9E75 at 5% alpha for background texture"
        ),
        "lighting": "Soft directional from top-left, no harsh shadows, gentle ambient occlusion under each box",
        "mood": "Professional, didactic, structured, neutral business",
        "technical_directives": (
            "1280x480px aspect ratio (cinematic banner). SVG-friendly clean lines and flat fills. No raster "
            "textures. No literal text labels (we add them in HTML overlays). Suitable for both light and "
            "dark mode display via CSS filter inversion if needed."
        ),
        "negative_prompt": (
            "no people, no faces, no realistic photo textures, no shadow gradients, no text labels, no IBM "
            "logos, no Maximo logos, no trademarks, no 3D render look, no skeuomorphism, no neon glows, "
            "no chromatic aberration, no busy backgrounds"
        ),
        "references": (
            "IBM Docs Multiple Sites Configuration Figure 3 (sanitized) https://www.ibm.com/docs/en/maximo-manage/9.0.0?topic=sites-organizations-overview ; "
            "Stripe Press infographics style ; Linear.app marketing illustrations"
        ),
        "priority": "P1",
        "notes": (
            "Hero image for lesson 3.1. The 4-level hierarchy must be unambiguously readable at a glance. "
            "Color coding: blue=System, gray=Set, amber=Org, teal=Site. Keep the visual minimal — viewers "
            "should grasp the concept in <3 seconds."
        ),
    },
]


def main() -> None:
    """Build the workbook and write it to the repo root."""
    wb = Workbook()
    ws = wb.active
    ws.title = "image-prompts"

    # Header row with brand teal fill
    teal_fill = PatternFill(start_color="1D9E75", end_color="1D9E75", fill_type="solid")
    white_font = Font(color="FFFFFF", bold=True, size=11)
    for idx, (col_name, col_width) in enumerate(COLUMNS, start=1):
        letter = get_column_letter(idx)
        cell = ws.cell(row=1, column=idx, value=col_name)
        cell.fill = teal_fill
        cell.font = white_font
        cell.alignment = Alignment(horizontal="left", vertical="center", wrap_text=True)
        ws.column_dimensions[letter].width = col_width

    # Data rows
    wrap_align = Alignment(horizontal="left", vertical="top", wrap_text=True)
    for row_idx, prompt in enumerate(PROMPTS, start=2):
        for col_idx, (col_name, _) in enumerate(COLUMNS, start=1):
            cell = ws.cell(row=row_idx, column=col_idx, value=prompt.get(col_name, ""))
            cell.alignment = wrap_align

    # Freeze header row
    ws.freeze_panes = "A2"

    # Increase row heights for readability
    ws.row_dimensions[1].height = 30
    for r in range(2, len(PROMPTS) + 2):
        ws.row_dimensions[r].height = 220

    output_path = Path(__file__).resolve().parent.parent / "c1000-183-image-prompts.xlsx"
    wb.save(output_path)
    print(f"Wrote {len(PROMPTS)} prompt(s) to {output_path}")


if __name__ == "__main__":
    main()
