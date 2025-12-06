"""
Python for Water Modellers - Example Script
A simple example demonstrating basic hydraulic calculations
"""

import math


def calculate_manning_velocity(n, R, S):
    """
    Calculate flow velocity using Manning's equation.
    
    Parameters:
    -----------
    n : float
        Manning's roughness coefficient
    R : float
        Hydraulic radius (m)
    S : float
        Channel slope (m/m)
    
    Returns:
    --------
    float
        Flow velocity (m/s)
    """
    velocity = (1/n) * (R ** (2/3)) * (S ** 0.5)
    return velocity


def calculate_discharge(velocity, area):
    """
    Calculate discharge using continuity equation.
    
    Parameters:
    -----------
    velocity : float
        Flow velocity (m/s)
    area : float
        Cross-sectional area (m²)
    
    Returns:
    --------
    float
        Discharge (m³/s)
    """
    return velocity * area


def main():
    print("=" * 50)
    print("Python for Water Modellers")
    print("Example: Manning's Equation for Open Channel Flow")
    print("=" * 50)
    
    # Example parameters for a rectangular channel
    width = 5.0  # meters
    depth = 2.0  # meters
    slope = 0.001  # m/m
    manning_n = 0.025  # concrete channel
    
    # Calculate hydraulic radius (for rectangular channel)
    wetted_perimeter = width + 2 * depth
    area = width * depth
    hydraulic_radius = area / wetted_perimeter
    
    # Calculate velocity and discharge
    velocity = calculate_manning_velocity(manning_n, hydraulic_radius, slope)
    discharge = calculate_discharge(velocity, area)
    
    # Display results
    print(f"\nChannel Properties:")
    print(f"  Width: {width} m")
    print(f"  Depth: {depth} m")
    print(f"  Slope: {slope} m/m")
    print(f"  Manning's n: {manning_n}")
    
    print(f"\nCalculated Values:")
    print(f"  Cross-sectional area: {area:.2f} m²")
    print(f"  Wetted perimeter: {wetted_perimeter:.2f} m")
    print(f"  Hydraulic radius: {hydraulic_radius:.2f} m")
    print(f"  Flow velocity: {velocity:.2f} m/s")
    print(f"  Discharge: {discharge:.2f} m³/s")
    print("=" * 50)


if __name__ == "__main__":
    main()
