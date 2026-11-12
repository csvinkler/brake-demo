"""Command line entry point: python -m brake_demo <vehicle_kmh> <wheel_kmh>"""

import sys

from brake_demo import __version__
from brake_demo.abs import abs_command, wheel_slip


def main(argv: list[str] | None = None) -> int:
    args = sys.argv[1:] if argv is None else argv
    if len(args) != 2:
        print(f"brake-demo {__version__}")
        print("usage: brake-demo <vehicle_speed_kmh> <wheel_speed_kmh>")
        return 2
    vehicle, wheel = float(args[0]), float(args[1])
    print(f"slip = {wheel_slip(vehicle, wheel):.0%}  ->  ABS {abs_command(vehicle, wheel)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
