# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
def h_boiling_Amalfi(
    m: float,
    x: float,
    Dh: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    kl: float,
    Hvap: float,
    sigma: float,
    q: float,
    A_channel_flow: float,
    chevron_angle: int = ...
) -> float: ...


def h_boiling_Han_Lee_Kim(
    m: float,
    x: float,
    Dh: float,
    rhol: float,
    rhog: float,
    mul: float,
    kl: float,
    Hvap: float,
    Cpl: int,
    q: float,
    A_channel_flow: float,
    wavelength: float,
    chevron_angle: int = ...
) -> float: ...


def h_boiling_Huang_Sheer(
    rhol: float,
    rhog: float,
    mul: float,
    kl: float,
    Hvap: float,
    sigma: float,
    Cpl: int,
    q: float,
    Tsat: float,
    angle: float = ...
) -> float: ...


def h_boiling_Lee_Kang_Kim(
    m: float,
    x: float,
    D_eq: float,
    rhol: float,
    rhog: float,
    mul: float,
    mug: float,
    kl: float,
    Hvap: float,
    q: float,
    A_channel_flow: float
) -> float: ...


def h_boiling_Yan_Lin(
    m: float,
    x: float,
    Dh: float,
    rhol: float,
    rhog: float,
    mul: float,
    kl: float,
    Hvap: float,
    Cpl: int,
    q: float,
    A_channel_flow: float
) -> float: ...

__all__: List[str]