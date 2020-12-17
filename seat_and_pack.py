#!/usr/bin/python
"""Canoe seat and pack positions, see SEAT_AND_PACK_POSITIONS.md.

All dimensions in inches, weights in pounds
"""

la = None
wa = 180
al = 16  # need 16" clear in front of seat front

lc = 86  # 87 would be mid-point, guess slightly back
wc = 40

wp = 40
pl = 27  # pack length

lb = 82


def print_row(values, format="%7s", comment=None):
    """Print one row of data."""
    s = "  ".join([(format % x) for x in values])
    if comment is not None:
        s += "  " + comment
    print(s)


for wa in (170, 180, 190):
    print("Person weight (Wa) = %dlbs" % (wa))
    print_row(["La", "Lp", "Wp", "stp"])
    for wp in (0, 30, 40, 50):
        lp_range = [174] if wp == 0 else [100, 105, 110, 115]
        for lp in lp_range:
            wb = wa + wc + wp  # boat floats so balance
            la = ((lb * wb) - (lc * wc + lp * wp)) * 1.0 / wa
            stp = lp - la - pl / 2.0
            comment = None
            if stp < al and wp > 0:
                comment = "seat too close to pack"
            print_row([la, lp, wp, stp], format="%7.1f", comment=comment)
    print('')
