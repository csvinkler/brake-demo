import pytest

from brake_demo.__main__ import main
from brake_demo.abs import abs_command, wheel_slip


# REQ-ABS-01
@pytest.mark.parametrize(
    ("vehicle", "wheel", "expected"),
    [
        (100, 100, 0.0),  # rolling freely
        (100, 80, 0.2),
        (100, 0, 1.0),  # locked wheel
        (100, 120, 0.0),  # wheel faster than car (spin) is limited to 0
    ],
)
def test_req_abs_01_slip_formula(vehicle, wheel, expected):
    assert wheel_slip(vehicle, wheel) == pytest.approx(expected)


# REQ-ABS-02
def test_req_abs_02_standstill_has_no_slip():
    assert wheel_slip(0, 0) == 0.0


# REQ-ABS-03
@pytest.mark.parametrize(("vehicle", "wheel"), [(-1, 10), (10, -1)])
def test_req_abs_03_negative_speed_is_rejected(vehicle, wheel):
    with pytest.raises(ValueError):
        wheel_slip(vehicle, wheel)


# REQ-ABS-04
@pytest.mark.parametrize(
    ("vehicle", "wheel", "expected"),
    [
        (100, 85, "HOLD"),  # 15 % slip
        (100, 80, "HOLD"),  # exactly 20 % is still fine
        (100, 75, "RELEASE"),  # 25 % slip
        (100, 0, "RELEASE"),  # locked wheel
    ],
)
def test_req_abs_04_release_above_20_percent_slip(vehicle, wheel, expected):
    assert abs_command(vehicle, wheel) == expected


# REQ-ABS-05
def test_req_abs_05_inactive_at_low_speed():
    assert abs_command(4, 0) == "HOLD"


def test_cli_prints_decision(capsys):
    assert main(["100", "50"]) == 0
    assert "RELEASE" in capsys.readouterr().out


def test_cli_without_arguments_shows_usage(capsys):
    assert main([]) == 2
    assert "usage" in capsys.readouterr().out
