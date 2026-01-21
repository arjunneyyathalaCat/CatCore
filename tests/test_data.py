import os
import glob
import pytest
import yaml
from pathlib import Path
from typing import Dict, Any, Union, List

from catcore.datamodel import catcore
from linkml_runtime.loaders import yaml_loader

DATA_DIR_VALID = Path(__file__).parent / "data" / "valid"
DATA_DIR_INVALID = Path(__file__).parent / "data" / "invalid"

VALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_VALID, '*.yaml'))
INVALID_EXAMPLE_FILES = glob.glob(os.path.join(DATA_DIR_INVALID, '*.yaml'))

# Mapping from identifier patterns or context to concrete class names
CHARACTERIZATION_TECHNIQUE_MAP = {
    'xray_source': {
        'Cu Kalpha': 'PowderXRD',
        'Al Kalpha': 'XPS',
    },
    'adsorbate_gas': 'BET',
    'reducing_gas_composition': 'TPR',
    'oxidizing_gas_composition': 'TPO',
    'excitation_laser_wavelength': 'RamanSpectroscopy',
    'minimum_wavenumber': 'InfraredSpectroscopy',
    'element_analyzed': 'XRayAbsorptionSpectroscopy',
    'nucleus': 'NMRSpectroscopy',
    'gun_type': 'TransmissionElectronMicroscopy',
    'image_resolution': 'ScanningElectronMicroscopy',
    'initial_temperature': 'Thermogravimetry',
    'combustion_temperature': 'ElementalAnalysis',
    'minimum_wavelength': 'UVVisSpectroscopy',
    'adsorption_gas': 'DRIFTS',
    'scan_rate': 'CyclicVoltammetry',
    'light_wavelength': 'DynamicLightScattering',
    'spray_voltage': 'ESI_MS',
    'excitation_wavelength': 'PhotoluminescenceSpectroscopy',
    'lifetime_fitting_model': 'PhotoluminescenceLifetime',
    'eluent': 'SizeExclusionChromatography',
    'gradient_program': 'HPLC_MS',
    'primary_energy': 'EDX',
    'electrode_configuration': 'ConductivityMeasurement',
}

PREPARATION_METHOD_MAP = {
    'impregnation_type': 'Impregnation',
    'precipitating_agent': 'CoPrecipitation',
    'hydrolysis_ratio': 'SolGel',
    'filling_volume': 'Solvothermal',
    'plasma_type': 'PlasmaAssisted',
    'fuel': 'CombustionSynthesis',
    'substrate': 'AtomicLayerDeposition',
    'microwave_frequency': 'MicrowaveAssisted',
    'sonication_power': 'SonochemicalSynthesis',
    'flame_type': 'FlameSprayPyrolysis',
    'ball_material': 'MechanochemicalSynthesis',
    'reaction_vessel': 'MolecularSynthesis',
}

SIMULATION_METHOD_MAP = {
    'exchange_correlation_functional': 'DFT',
    'force_field': 'MolecularDynamics',
    'rate_constants': 'Microkinetics',
    'interaction_potential': 'MonteCarlo',
}

CALCULATED_PROPERTY_MAP = {
    'formation_energy': 'ThermodynamicStability',
    'piezoelectric_tensor': 'Piezoelectricity',
    'elastic_tensor': 'ElasticConstants',
    'surface_energy': 'Surfaces',
    'band_path': 'ElectronicStructure',
    'polarization_direction': 'Ferroelectrics',
    'direct_indirect': 'BandGap',
    'material_composition': 'DielectricTensors',
    'force_constant_method': 'PhononDispersion',
    'fit_method': 'EquationsOfState',
    'ph_range': 'AqueousStability',
    'grain_boundary_plane': 'GrainBoundaries',
}

REACTOR_DESIGN_MAP = {
    'gas_distributor_type': 'FluidizedBedReactor',
}

# Default classes for abstract types when no specific fields are found
DEFAULT_CLASSES = {
    'reactor_design_type': 'FixedBedReactor',
    'product_identification_method': 'GCMS',
}


def infer_class_type(data: Dict[str, Any], type_map: Dict[str, Any], default_class: str = None) -> str:
    """Infer the concrete class type based on present fields."""
    for key, class_name in type_map.items():
        if key in data:
            if isinstance(class_name, dict):
                # Need to check value
                for value_pattern, cn in class_name.items():
                    if value_pattern in str(data[key]):
                        return cn
            else:
                return class_name

    # Return default class if no specific fields found
    return default_class


def instantiate_polymorphic_objects(data: Union[Dict, List], parent_key: str = None) -> Union[Dict, List]:
    """Recursively instantiate concrete classes for polymorphic fields."""
    if isinstance(data, list):
        return [instantiate_polymorphic_objects(item, parent_key) for item in data]

    if not isinstance(data, dict):
        return data

    # Check for explicit type hint (both 'type' and '@type' for LinkML compatibility)
    explicit_type = data.get('type') or data.get('@type')

    # Recursively process nested structures first
    result = {}
    for key, value in data.items():
        if key in ('type', '@type'):  # Skip the type hint fields
            continue
        result[key] = instantiate_polymorphic_objects(value, key)

    # Now handle polymorphic instantiation for specific keys
    if parent_key == 'characterization_technique':
        class_name = explicit_type or infer_class_type(result, CHARACTERIZATION_TECHNIQUE_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'preparation_method':
        class_name = explicit_type or infer_class_type(result, PREPARATION_METHOD_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'simulation_method':
        class_name = explicit_type or infer_class_type(result, SIMULATION_METHOD_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'calculated_property':
        class_name = explicit_type or infer_class_type(result, CALCULATED_PROPERTY_MAP)
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'reactor_design_type':
        class_name = explicit_type or infer_class_type(result, REACTOR_DESIGN_MAP,
                                                       DEFAULT_CLASSES.get('reactor_design_type'))
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    elif parent_key == 'product_identification_method':
        # For now, use GCMS as default if no specific fields found
        class_name = explicit_type or DEFAULT_CLASSES.get('product_identification_method')
        if class_name:
            cls = getattr(catcore, class_name)
            return cls(**result)

    return result


@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_files(filepath):
    """Test loading of all valid data files."""
    target_class_name = Path(filepath).stem.split("-")[0]
    tgt_class = getattr(catcore, target_class_name)

    # Load the YAML content
    with open(filepath, 'r') as f:
        data_dict = yaml.safe_load(f)

    # Handle polymorphic fields by instantiating concrete classes
    poly_fields = [
        'characterization_technique',
        'preparation_method',
        'simulation_method',
        'calculated_property',
        'reactor_design_type',
        'product_identification_method',
        'operation_parameters',
        'precursor'
    ]

    for poly_field in poly_fields:
        if poly_field in data_dict and data_dict[poly_field]:
            data_dict[poly_field] = instantiate_polymorphic_objects(
                data_dict[poly_field],
                poly_field
            )

    # Instantiate the target class
    obj = tgt_class(**data_dict)

    assert obj
