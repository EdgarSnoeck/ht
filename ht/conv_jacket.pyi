# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import Optional


def Lehrer(
    m: float,
    Dtank: float,
    Djacket: float,
    H: float,
    Dinlet: float,
    rho: float,
    Cp: float,
    k: float,
    mu: float,
    muw: Optional[float] = ...,
    isobaric_expansion: Optional[float] = ...,
    dT: Optional[float] = ...,
    inlettype: str = ...,
    inletlocation: str = ...
) -> float: ...


def Stein_Schmidt(
    m: float,
    Dtank: float,
    Djacket: float,
    H: float,
    Dinlet: float,
    rho: float,
    Cp: float,
    k: float,
    mu: float,
    muw: Optional[float] = ...,
    rhow: Optional[float] = ...,
    inlettype: str = ...,
    inletlocation: str = ...,
    roughness: int = ...
) -> float: ...

__all__: List[str]