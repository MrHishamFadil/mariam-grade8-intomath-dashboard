# Design System: Mariam's Grade 8 Into Math Dashboard (HMH Into Math TE)

## 1. Visual Theme & Atmosphere
A restrained, high-agency educational mathematics interface with confident asymmetric layouts and fluid spring-physics feedback. The atmosphere is calm, academic, and inspiring — combining the clarity of a modern design studio with the rigorous visual clarity needed for Grade 8 Transformational Geometry (HMH Into Math). Density is balanced (Level 5), avoiding claustrophobic data-stuffing while providing immediate access to coordinate tools, live geometric manipulation, and instant step-by-step model answers.

## 2. Color Palette & Roles
- **Canvas Base** (`#F8FAFC`) — Primary background surface; subtle cool neutral slate tone.
- **Pure Surface** (`#FFFFFF`) — Card, panel, and modal containers with 1px border.
- **Deep Charcoal Ink** (`#0F172A`) — Primary typography, Slate-900 depth for crisp legibility.
- **Muted Slate** (`#64748B`) — Secondary text, mathematical explanations, coordinate labels, DOK tags.
- **Whisper Border** (`rgba(226, 232, 240, 0.8)`) — Structural separation, grid dividers, table rules.
- **Primary Indigo** (`#4F46E5`) — Single primary accent for CTAs, active tab pills, selected coordinate handles, vector paths.
- **Mathematical Success** (`#059669`) — Correct answer verification, congruent mapping badges, positive feedback.
- **Mathematical Alert** (`#D97706`) — Pedagogical hints, invariance caveats (e.g. orientation reversal in reflections).
- **Mathematical Error** (`#DC2626`) — Incorrect attempt indicators, non-congruent figure warnings.

*(Banned: AI neon gradient glows, saturated electric purple, pure black #000000, uncalibrated high-contrast neons).*

## 3. Typography Rules
- **Display & Section Titles:** `Outfit`, `-apple-system`, `BlinkMacSystemFont`, `sans-serif` — Track-tight (`letter-spacing: -0.025em`), weight-driven hierarchy (`font-weight: 700` and `800`).
- **Body & Explanations:** `Outfit`, `Inter`, `sans-serif` — Relaxed leading (`line-height: 1.6`), max 72 characters per line for high readability during prolonged study.
- **Mathematical Notation & Coordinates:** `KaTeX`, `JetBrains Mono`, `monospace` — Strict tabular figures for coordinate pairs $(x, y)$, mapping arrows $\to$, scale factors $k$, and geometric proofs $\triangle ABC \cong \triangle A'B'C'$.
- **Banned:** Generic serif fonts in software UI, low-contrast washed-out grays, text overlapping visuals.

## 4. Component Stylings
- **Navigation Tabs:** Rounded pill containers (`border-radius: 9999px`) with tactile state indicators, subtle backdrop blur (`backdrop-filter: blur(12px)`), and active state highlight.
- **Interactive Question Cards:** Clean Bento-box elevation with generous internal padding (`clamp(1.25rem, 2.5vw, 1.75rem)`). Labeled option buttons with high-contrast letter badges (A, B, C, D) and focus ring in Primary Indigo.
- **Buttons:** Tactile feedback on press (`transform: translateY(1px)`). Primary fill in Indigo (`#4F46E5`), secondary in soft outline (`border: 1.5px solid var(--border)`).
- **Coordinate Canvas (Sandbox):** High-precision SVG grid with subtle 1px gridlines (`#E2E8F0`), distinct colored vertices (Preimage: Indigo `#4F46E5`, Image: Emerald `#059669`), and draggable or slider-driven transformation controls.
- **Feedback & Hint Containers:** Smooth vertical slide reveal with left accent border (`3px solid var(--accent)`), rendering KaTeX equations seamlessly.

## 5. Layout Principles
- **Grid-First Modular Architecture:** 12-column adaptive container constrained to `1400px` max-width.
- **Clean Spatial Zones:** Strict separation between concept instruction, interactive coordinate manipulation, and practice problem arenas.
- **Mobile-First Responsive Collapse:** Multi-column coordinate grids collapse smoothly below `768px`. All interactive tap targets adhere to a minimum of `44px` height and width.

## 6. Motion & Interaction
- **Spring Physics:** Smooth transitions (`cubic-bezier(0.16, 1, 0.3, 1)`) for card expansions, tab switches, and coordinate resets.
- **Perpetual Micro-Feedback:** Instant validation on selection, subtle badge pulses upon level-up, and celebratory particle bursts (confetti) upon achieving 100% quiz mastery.
- **Hardware Acceleration:** All animations restricted to `transform` and `opacity` to maintain 60 FPS on iPads and mobile devices.

## 7. Anti-Patterns (Banned)
- No saturated purple AI glow or gradient text on body copy.
- No pure black (`#000000`) surfaces.
- No unstyled mathematical equations (must be KaTeX rendered).
- No unhandled edge cases in coordinate inputs.
- No generic filler copy ("Elevate your learning"); use authentic HMH Into Math Grade 8 terminology.
