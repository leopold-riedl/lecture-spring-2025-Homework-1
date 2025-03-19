import math
from HW_1 import pv_system_output, wind_power_output, total_renewable_energy

def test_pv_system_output():
    """Test solar panel energy output calculation."""
    result = pv_system_output(panel_number=100, panel_size=2, efficiency=0.2, sunlight_hours=5)
    expected_output = round(100 * 2 * 0.2 * 1000 * 5 / 1000, 2)  # Manually calculated expected result
    assert result == expected_output

def test_wind_power_output():
    """Test wind turbine energy output calculation."""
    result = wind_power_output(wind_speed=10, blade_length=50, capacity_factor=0.35, wind_hours=10)
    swept_area = math.pi * (50 ** 2)
    expected_power = 0.5 * 1.225 * swept_area * (10 ** 3) * 0.35 / 1000  # Convert to kW
    expected_output = round(expected_power * 10, 2)  # Multiply by wind hours
    assert result == expected_output

def test_total_renewable_energy():
    """Test total energy calculation from solar and wind sources."""
    result = total_renewable_energy(solar_kwh=500, wind_kwh=1000)
    expected_output = 500 + 1000
    assert result == expected_output