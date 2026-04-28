"""USB-C dual-rail power board — 5 V passthrough + AMS1117-3.3 V regulated.

PCBA-3 test project for the circuit_toolkit. Provides BOTH a direct 5 V
output (USB-C VBUS straight through) AND a 3.3 V output via the AMS1117
LDO, each with its own colour-coded power-good LED. Useful as a single
power source for projects that mix 5 V (relays, motors, level-shifters)
and 3.3 V (sensors, MCUs).
"""
from circuit_toolkit import Board
from circuit_toolkit.blocks import (
    usbc_power, ams1117_ldo, led_indicator, pin_header, m2_mounting_hole,
)


def build() -> Board:
    board = Board("usbc-dual-rail", size=(50, 30))

    # USB-C input (J1, R1, R2)
    vbus, gnd, _, _ = usbc_power(board, ref="J1", cc_pulldowns="5.1k")

    # 3.3 V LDO (U1) + caps (C1, C2, C3)
    v3v3 = ams1117_ldo(
        board, ref="U1",
        vin=vbus, gnd=gnd, output_voltage=3.3,
        in_caps=["10uF/0805"],
        out_caps=["10uF/0805", "100nF/0402"],
    )

    # Power-good LEDs — yellow on the 5 V rail, green on the 3.3 V rail
    led_indicator(
        board, ref_led="D2", ref_resistor="R10",
        vin=vbus, gnd=gnd, color="yellow", current_ma=1.5,
        supply_voltage=5.0,
    )
    led_indicator(
        board, ref_led="D1", ref_resistor="R3",
        vin=v3v3, gnd=gnd, color="green", current_ma=1.3,
        supply_voltage=3.3,
    )

    # Output headers — 2-pin each, separately labelled
    pin_header(board, ref="J2", pins=2, label="5V_OUT",
               nets=[vbus, gnd])
    pin_header(board, ref="J3", pins=2, label="3V3_OUT",
               nets=[v3v3, gnd])

    # Two M2 corner mounting holes
    m2_mounting_hole(board, ref="H1")
    m2_mounting_hole(board, ref="H2")

    return board


if __name__ == "__main__":
    b = build()
    print(b)
    for c in b.components:
        print(f"  {c.ref:<5} {c.value:<25}  {c.block_id}")
