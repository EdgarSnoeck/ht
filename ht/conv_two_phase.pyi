# DO NOT EDIT - AUTOMATICALLY GENERATED BY tests/make_test_stubs.py!
from typing import List
from typing import (
    Optional,
    Union,
)


def Aggour(
    m: float,
    x: float,
    alpha: float,
    D: float,
    rhol: int,
    Cpl: int,
    kl: float,
    mu_b: float,
    mu_w: Optional[float] = ...,
    L: Optional[int] = ...,
    turbulent: None = ...
) -> float: ...


def Davis_David(m: int, x: float, D: float, rhol: int, rhog: float, Cpl: int, kl: float, mul: float) -> float: ...


def Elamvaluthi_Srinivas(
    m: int,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    Cpl: int,
    kl: float,
    mug: float,
    mu_b: float,
    mu_w: Optional[float] = ...
) -> float: ...


def Groothuis_Hendal(
    m: int,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    Cpl: int,
    kl: float,
    mug: float,
    mu_b: float,
    mu_w: Optional[float] = ...,
    water: bool = ...
) -> float: ...


def Hughmark(
    m: int,
    x: float,
    alpha: float,
    D: float,
    L: float,
    Cpl: int,
    kl: float,
    mu_b: Optional[float] = ...,
    mu_w: Optional[float] = ...
) -> float: ...


def Knott(
    m: int,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    Cpl: Optional[int] = ...,
    kl: Optional[float] = ...,
    mu_b: Optional[float] = ...,
    mu_w: Optional[float] = ...,
    L: Optional[int] = ...,
    hl: None = ...
) -> float: ...


def Kudirka_Grosh_McFadden(
    m: int,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    Cpl: int,
    kl: float,
    mug: float,
    mu_b: float,
    mu_w: Optional[float] = ...
) -> float: ...


def Martin_Sims(
    m: int,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    hl: Optional[float] = ...,
    Cpl: Optional[int] = ...,
    kl: Optional[float] = ...,
    mu_b: Optional[float] = ...,
    mu_w: Optional[float] = ...,
    L: Optional[int] = ...
) -> float: ...


def Ravipudi_Godbold(
    m: int,
    x: float,
    D: float,
    rhol: int,
    rhog: float,
    Cpl: int,
    kl: float,
    mug: float,
    mu_b: float,
    mu_w: Optional[float] = ...
) -> float: ...


def h_two_phase(
    m: int,
    x: float,
    D: float,
    Cpl: int,
    kl: float,
    rhol: Optional[int] = ...,
    rhog: None = ...,
    mul: None = ...,
    mu_b: Optional[float] = ...,
    mu_w: Optional[float] = ...,
    mug: None = ...,
    L: Optional[int] = ...,
    alpha: Optional[float] = ...,
    method: Optional[str] = ...
) -> float: ...

__all__: List[str]