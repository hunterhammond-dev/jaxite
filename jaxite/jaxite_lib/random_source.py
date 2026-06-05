"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import random_source

RandomSource = random_source.RandomSource
CycleRng = random_source.CycleRng
SystemRandomSource = random_source.SystemRandomSource
PseudorandomSource = random_source.PseudorandomSource
NormalOnlyRng = random_source.NormalOnlyRng
ConstantUniformRng = random_source.ConstantUniformRng
ZeroRng = random_source.ZeroRng
VARYING_MAGNITUDE_TEST_RNGS = random_source.VARYING_MAGNITUDE_TEST_RNGS
ALL_RNGS = random_source.ALL_RNGS
