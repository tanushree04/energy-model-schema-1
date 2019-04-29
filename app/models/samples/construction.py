in_material = {
    'type': 'EnergyMaterial',
    'name': 'Internal Source',
    'roughness': 'Smooth',
    'thickness': 0.012,
    'conductivity': 0.6,
    'density': 1000,
    'specific_heat': 4185,
    'thermal_absorptance': 0.95,
    'solar_absorptance': 0.7,
    'visible_absorptance': 0.7
}

in_const = {
    'type': 'EnergyConstruction',
    'name': 'Internal Source',
    'materials': [in_material]
}
