# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_cfd_utils.ipynb.

# %% auto 0
__all__ = ['freecad_path', 'cfdof_path', 'create_analysis_container', 'setup_fluid_properties']

# %% ../nbs/03_cfd_utils.ipynb 3
import sys
sys.path.append("..")
freecad_path = r"C:\Program Files\FreeCAD 0.21\bin"
cfdof_path = r'C:\Users\ASUS\AppData\Roaming\FreeCAD\Mod\CfdOF'
if freecad_path not in sys.path:    
    sys.path.append(freecad_path)
if cfdof_path not in sys.path:    
    sys.path.append(cfdof_path)

# %% ../nbs/03_cfd_utils.ipynb 4
import FreeCAD as App
import CfdOF

# %% ../nbs/03_cfd_utils.ipynb 5
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

# %% ../nbs/03_cfd_utils.ipynb 6
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
