"""Lazy access to the molecular-system owner for selected routes."""

from depdigest import dep_digest


@dep_digest("molsysmt")
def _load_molsysmt():
    import molsysmt

    return molsysmt
