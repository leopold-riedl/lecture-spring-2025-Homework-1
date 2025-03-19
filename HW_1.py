import math

def pv_system_output(panel_number: int, panel_size: float, efficiency: float, sunlight_hours: float, irradiance: float = 1000) -> float:
    """
    Calculate solar panel energy output.

    Parameters:
        panel_number (int): Total number solar panels (-).
        panel_size (int): Total area per solar panel (m²).
        efficiency (float): Efficiency of the solar panel (0 to 1).
        sunlight_hours (float): Average sunlight hours per day.
        irradiance (float, optional): Solar irradiance in W/m² (default: 1000 W/m²).

    Returns:
        float: Daily energy output in kWh.
    """
    panel_area = panel_number * panel_size  # Total area of solar panels (m²)
    power_output = panel_area * efficiency * irradiance  # Watts
    energy_output = (power_output * sunlight_hours) / 1000  # Convert to kWh
    return round(energy_output, 2)

def wind_power_output(wind_speed: float, blade_length: float, capacity_factor: float, wind_hours: float, air_density: float = 1.225) -> float:
    """
    Estimate wind turbine energy output using a simplified wind power formula.

    Parameters:
        wind_speed (float): Wind speed in m/s.
        blade_length (float): Length of one turbine blade (m).
        capacity_factor (float): capacity_factor of the turbine (0 to 1).
        wind_hours (float): Average wind hours per day.
        air_density (float, optional): Air density in kg/m³ (default: 1.225 kg/m³).

    Returns:
        float: Power output in kW.
    """
    swept_area = math.pi * (blade_length ** 2)  # Rotor swept area (m²)
    power_available = 0.5 * air_density * swept_area * (wind_speed ** 3)  # Wind power formula
    power_output = capacity_factor * power_available / 1000  # Convert to kW
    energy_output = power_output * wind_hours
    return round(energy_output, 2)

def total_renewable_energy(solar_kwh: float, wind_kwh: float) -> float:
    """
    Compute total renewable energy production from solar and wind sources.

    Parameters:
        solar_kwh (float): Energy output from solar panels (kWh).
        wind_kw (float): Power output from wind turbines (kW).
        wind_hours (int, optional): Duration in hours (default: 18).

    Returns:
        float: Total energy generated in kWh.
    """
    total_energy = solar_kwh + wind_kwh
    return round(total_energy, 2)

if __name__ == "__main__":
    # Example usage with dummy values
    solar_kwh = pv_system_output(panel_number=2500, panel_size=2.79, efficiency=0.22, sunlight_hours=7)
    wind_kwh = wind_power_output(wind_speed=8, blade_length=60, capacity_factor=0.4, wind_hours=18)

    total_energy = total_renewable_energy(solar_kwh, wind_kwh)

    print(f"Daily Solar Energy Output: {solar_kwh} kWh")
    print(f"Wind Turbine Energy Output: {wind_kwh} kWh")
    print(f"Total Renewable Energy Production: {total_energy} kWh")
