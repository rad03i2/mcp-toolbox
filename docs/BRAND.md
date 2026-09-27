# MCP Toolbox — Brand Guide

## Identity concept: Signal Grid

MCP Toolbox is a **local protocol bridge for small developer tools**. Its visual identity therefore treats the project as a compact signal router rather than a generic AI product.

The central visual idea is a **hub with connected utility nodes**:

- the hub represents the MCP/FastMCP server;
- surrounding nodes represent narrowly scoped tools;
- connection lines represent structured MCP calls over a local stdio bridge;
- distinct node colors reinforce that the server contains separate, focused capabilities.

The identity should feel technical, modular, precise, and intentionally constrained.

## Color system

| Role | Color | Hex |
| --- | --- | --- |
| Main background | Carbon black | `#090B10` |
| Surface | Graphite | `#151923` |
| Primary signal | Electric lime | `#B7FF3C` |
| Protocol accent | Electric violet | `#8B5CF6` |
| Data accent | Cyan | `#4DE3FF` |
| Primary text | Ice white | `#F5F7FA` |
| Muted text | Steel gray | `#99A1AD` |

**Primary accent:** `#B7FF3C`

Electric lime represents an active local tool path. Violet is reserved for protocol / identity elements. Cyan is used for structured data and formatting.

## Logo

Primary file:

- `assets/project-logo.svg`

The logo combines a central hexagonal hub with four connected utility nodes. It is deliberately not a lettermark and should remain recognizable without the project name.

### Usage rules

- Keep the square aspect ratio.
- Do not place text inside the icon.
- Preserve the relative node colors.
- Keep clear space around the icon equal to roughly 10% of its width.
- Avoid placing the logo on bright lime backgrounds.
- At small sizes, use the icon without additional text.

## Project cover

Primary file:

- `assets/project-cover.svg`

The cover communicates the actual project scope:

- FastMCP hub;
- local stdio connection model;
- text / hashing / Base64 utilities;
- JSON formatting;
- UUID generation;
- UTC time.

It intentionally avoids terminal screenshots, robot imagery, AI brains, cloud graphics, and filesystem icons because those would imply capabilities the project does not expose.

## Typography

Use portable developer-oriented typography:

- **Headings:** Inter / Segoe UI / Arial.
- **Technical labels:** JetBrains Mono / Consolas / monospace.
- **Arabic:** Noto Sans Arabic / Arial.

Technical labels may use uppercase and moderate letter spacing. Body documentation should remain normal case for readability.

## Shapes and iconography

Preferred shapes:

- hexagonal hubs;
- rounded-square utility nodes;
- thin signal paths;
- small status dots;
- restrained grid backgrounds.

Avoid glossy 3D toolboxes, stock AI imagery, and dense dashboard decoration.

## Writing tone

Documentation should be exact and permission-aware:

- say “MCP server” rather than “AI agent”;
- say “local stdio transport” rather than implying remote hosting;
- call Base64 an encoding, never encryption;
- state that SHA-1 / MD5 exist for compatibility;
- do not imply filesystem, shell, browser, or network capabilities;
- mark roadmap concepts clearly as future ideas.

## Distinction from other repository identities

Signal Grid is intentionally **developer/protocol-centric**. Its carbon + electric-lime palette, network-node geometry, and modular tool-hub concept differentiate it from media, OCR, security, or desktop-product identities elsewhere in the portfolio.

## Attribution

Project by **رضوان عبدالهادي** / **Radwan Abd alhady Ahmed**.
