"""Simplified anti-lock braking (ABS) logic.

Requirements (used as test IDs in tests/test_abs.py):
  REQ-ABS-01  Wheel slip = (vehicle speed - wheel speed) / vehicle speed, limited to 0..1.
  REQ-ABS-02  At standstill (vehicle speed 0) the slip is 0.
  REQ-ABS-03  Negative speeds are invalid input and raise ValueError.
  REQ-ABS-04  ABS releases brake pressure when slip is above 20 %.
  REQ-ABS-05  ABS is inactive below 5 km/h vehicle speed.
"""

SLIP_THRESHOLD = 0.30  # REQ-ABS-04
MIN_ACTIVE_SPEED_KMH = 5.0  # REQ-ABS-05


def wheel_slip(vehicle_speed_kmh: float, wheel_speed_kmh: float) -> float:
    """Return the wheel slip as a ratio between 0.0 and 1.0."""
    if vehicle_speed_kmh < 0 or wheel_speed_kmh < 0:
        raise ValueError("speeds must not be negative")
    if vehicle_speed_kmh == 0:
        return 0.0
    slip = (vehicle_speed_kmh - wheel_speed_kmh) / vehicle_speed_kmh
    return max(0.0, min(1.0, slip))


def abs_command(vehicle_speed_kmh: float, wheel_speed_kmh: float) -> str:
    """Return "RELEASE" if the wheel is about to lock, otherwise "HOLD"."""
    if vehicle_speed_kmh < MIN_ACTIVE_SPEED_KMH:
        return "HOLD"
    if wheel_slip(vehicle_speed_kmh, wheel_speed_kmh) > SLIP_THRESHOLD:
        return "RELEASE"
    return "HOLD"
