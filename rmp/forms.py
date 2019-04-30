from django import forms
from rmp.models import (
    ExecutiveSummary,
    Facility,
    Registration,
    StateCd,
    StateCounts,
    Process,
    ProcChem,
    ChemCd,
    tblExecutiveSummaries,
    tblFacility,
    tblS1Facilities,
    tblS1FlammableMixtureChemicals,
    tblS1ProcessChemicals,
    tblS6AccidentChemicals,
    tblS6AccidentHistory,
)

class LocationSearch(forms.Form):
