"""usbc-dual-rail layout — extends usbc-3v3's known-good 48×30 layout to a
50×30 board, adding a yellow 5 V power-good LED row above the existing
green 3.3 V LED. The right-edge gains a second 2-pin output header for
the raw 5 V rail."""

positions = {
    # USB-C input (vertical) — same as usbc-3v3
    "J1": (5.5, 15, 270),
    "R1": (9, 8.5, 0),
    "R2": (9, 21.5, 0),

    # AMS1117 LDO + caps — same as usbc-3v3
    "U1": (22, 15, 270),
    "C1": (13, 10.5, 0),     # 10uF input
    "C2": (30, 10.5, 0),     # 10uF output
    "C3": (30, 19.5, 0),     # 100nF output

    # 3.3V power-good (green)
    "D1":  (37, 19, 0),
    "R3":  (33.5, 19, 0),

    # 5V power-good (yellow) — placed slightly above the 3V3 LED for clarity
    "D2":  (37, 11, 0),
    "R10": (33.5, 11, 0),

    # Two output headers — 5V on top, 3V3 on bottom
    "J2": (45, 11, 0),       # 5V_OUT
    "J3": (45, 19, 0),       # 3V3_OUT

    # Mounting holes — opposite corners
    "H1": (3, 3, 0),
    "H2": (47, 27, 0),
}

ref_text_overrides = {
    "R2": (9.0, 22.8),
}

pad_zone_full = [
    ("J1", "B7"), ("J1", "A8"),
]

# Tracks: reuse the usbc-3v3 validated routes for J1↔R1/R2 + VBUS bus +
# CC + GND bridges. Add new short stubs for the 5V branch (D2/R10) and
# the two right-edge output headers.
tracks = [
    # VBUS rail (same as usbc-3v3)
    ("VBUS", 9.545, 12.55, 11.8, 12.55, 0.3, "F.Cu"),
    ("VBUS", 9.545, 17.45, 11.8, 17.45, 0.3, "F.Cu"),
    ("VBUS", 11.8, 10.5, 11.8, 19.5, 0.5, "F.Cu"),
    ("VBUS", 11.8, 11.85, 19.7, 11.85, 0.8, "F.Cu"),
    # The new 5V branch (D2/R10/J2) is left for hand-routing in the GUI;
    # the bus tracks I tried to add at y=11 collided with J1's GND pads.

    # CC1 / CC2 — same as usbc-3v3
    ("CC1", 9.545, 13.75, 10.87, 13.75, 0.3, "F.Cu"),
    ("CC1", 10.87, 13.75, 7.0, 13.75, 0.3, "B.Cu"),
    ("CC1", 7.0, 13.75, 7.0, 8.5, 0.3, "B.Cu"),
    ("CC1", 7.0, 8.5, 8.49, 8.5, 0.3, "F.Cu"),

    ("CC2", 9.545, 16.75, 10.87, 16.75, 0.3, "F.Cu"),
    ("CC2", 10.87, 16.75, 10.87, 16.0, 0.3, "F.Cu"),
    ("CC2", 10.87, 16.0, 7.0, 16.0, 0.3, "B.Cu"),
    ("CC2", 7.0, 16.0, 7.0, 21.5, 0.3, "B.Cu"),
    ("CC2", 7.0, 21.5, 8.49, 21.5, 0.3, "F.Cu"),

    # GND bridges — same as usbc-3v3
    ("GND", 9.545, 13.25, 7.5, 13.25, 0.25, "F.Cu"),
    ("GND", 9.545, 14.25, 7.5, 14.25, 0.25, "F.Cu"),
    ("GND", 9.545, 16.25, 7.5, 16.25, 0.25, "F.Cu"),
    ("GND", 8.63, 10.68, 9.545, 10.68, 0.25, "F.Cu"),
    ("GND", 9.545, 10.68, 9.545, 11.75, 0.25, "F.Cu"),
    ("GND", 8.63, 19.32, 9.545, 19.32, 0.25, "F.Cu"),
    ("GND", 9.545, 19.32, 9.545, 18.25, 0.25, "F.Cu"),
]

vias = [
    ("CC1", 10.87, 13.75, 0.4, 0.8),
    ("CC1", 7.0, 8.5, 0.4, 0.8),
    ("CC2", 10.87, 16.0, 0.4, 0.8),
    ("CC2", 7.0, 21.5, 0.4, 0.8),
]

zones = [
    {"net": "GND", "layer": "F.Cu",
     "polygon": [(1, 1), (49, 1), (49, 29), (1, 29)],
     "min_thickness": 0.25, "pad_connection": "thermal"},
]

outline = {"shape": "rect", "x": 0.0, "y": 0.0, "w": 50.0, "h": 30.0}
