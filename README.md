# usbc-dual-rail

USB-C-powered dual-rail breakout — both 5 V (passthrough from USB) AND
3.3 V (via AMS1117 LDO) on separate 2-pin headers, each with a colour-
coded power-good LED (yellow for 5 V, green for 3.3 V).

PCBA-3 test project for the [kicad-claude-toolkit](https://github.com/nickleassdimebutt/kicad-claude-toolkit)
v3 toolchain. Same component count as usbc-3v3 (15) but a different
topology — exercises the toolkit on a multi-rail design.

## Layout status

The validated routes from usbc-3v3 (J1 escape, VBUS bus stub, CC
pulldowns, GND bridges) are reused verbatim. The 5 V branch (D2/R10
power-LED + J2 5V_OUT header) and the +3V3 branch updates (J3 3V3_OUT)
are deferred to KiCad GUI hand-routing.

DRC: 2 minor violations (1 dangling track endpoint, 1 silk edge
clearance — both fixable by trimming) and 9 unconnected items (the
routing TODO).

## Build

```powershell
& "C:\Program Files\KiCad\10.0\bin\python.exe" build.py --datasheet --sim
```

## Topology summary

| Block | Components | Function |
|-------|------------|----------|
| `usbc_power` | J1 + R1, R2 | USB-C 5 V input + CC pulldowns |
| `ldo` | U1 + C1, C2, C3 | AMS1117-3.3 LDO with bypass caps |
| `led` (5 V) | D2 + R10 | Yellow 5 V power-good indicator |
| `led` (3 V) | D1 + R3 | Green 3.3 V power-good indicator |
| `header` | J2, J3 | Two 2-pin output headers (5V_OUT, 3V3_OUT) |
| `mounting` | H1, H2 | Two M2 corner holes |

15 components, 7 nets, 50 × 30 mm.
