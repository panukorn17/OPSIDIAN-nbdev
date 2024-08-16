# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_cfd_utils.ipynb.

# %% auto 0
__all__ = ['clean_sys_path', 'create_analysis_container', 'setup_fluid_properties']

# %% ../nbs/03_cfd_utils.ipynb 3
import sys
import os

def clean_sys_path():
    # Store the original sys.path
    original_path = sys.path.copy()

    # Essential paths (modify as needed)
    essential_paths = [
        '',  # Current directory
        os.path.dirname(sys.executable),  # Python installation directory
        os.path.join(os.path.dirname(sys.executable), 'lib', 'site-packages'),  # Site-packages
    ]

    # Add FreeCAD and CfdOF paths
    freecad_path = r"C:\Program Files\FreeCAD 0.21\bin"  # Adjust this path
    cfdof_path = r'C:\Users\ASUS\AppData\Roaming\FreeCAD\Mod\CfdOF'
    essential_paths.extend([freecad_path, cfdof_path])

    # Clean sys.path
    sys.path = []
    for path in essential_paths:
        if path not in sys.path and os.path.exists(path):
            sys.path.append(path)

    # Add back any missing essential paths from the original sys.path
    for path in original_path:
        if path not in sys.path and os.path.exists(path):
            if any(essential_keyword in path.lower() for essential_keyword in ['python', 'freecad', 'cfdof']):
                sys.path.append(path)

    print("Cleaned sys.path:")
    for path in sys.path:
        print(path)

# Run the cleaning function
clean_sys_path()

# %% ../nbs/03_cfd_utils.ipynb 4
import FreeCAD as App


# %% ../nbs/03_cfd_utils.ipynb 5
import CfdOF
def create_analysis_container():
    """
    Function to create the analysis container on freeCAD

    Parameters:
    shape (Part.Shape): The object to be analysed
    """
    # create a cfd analysis group object
    analysis = CfdOF.CfdAnalysis.makeCfdAnalysis('CfdAnalysis')
    CfdOF.CfdTools.setActiveAnalysis(analysis)
    analysis.addObject(CfdOF.Solve.CfdPhysicsSelection.makeCfdPhysicsSelection())
    analysis.addObject(CfdOF.Solve.CfdFluidMaterial.makeCfdFluidMaterial('FluidProperties'))
    analysis.addObject(CfdOF.Solve.CfdInitialiseFlowField.makeCfdInitialFlowField())
    analysis.addObject(CfdOF.Solve.CfdSolverFoam.makeCfdSolverFoam())

# %% ../nbs/03_cfd_utils.ipynb 7
def setup_fluid_properties(name='Water', type='Isothermal', density='998 kg/m^3', dynamicViscosity='1.003e-3 kg/m/s'):
    """
    Function to set up the fluid properties for CfdOF
    """
    print("Setting up fluid proberties")
    if name == 'Water':
        desc = 'Standard distilled water properties at 20 Degrees Celsius and 1 atm'
        App.ActiveDocument.FluidProperties.Label = 'Water'
    else:
        desc = ''
        App.ActiveDocument.FluidProperties.Label = 'Fluid'
    App.ActiveDocument.FluidProperties.Material = {'CardName': name + type,
                                       'AuthorAndLicence': '',
                                       'Name': name,
                                       'Type': type,
                                       'Description': desc,
                                       'Density': density,
                                       'DynamicViscosity': dynamicViscosity}
