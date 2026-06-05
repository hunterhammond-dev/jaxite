"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import test_utils

DEFAULT_ENCODING_PARAMS = test_utils.DEFAULT_ENCODING_PARAMS
ENCODING_PARAMS_128_BIT_SECURITY = test_utils.ENCODING_PARAMS_128_BIT_SECURITY
LWE_RNG_128_BIT_SECURITY = test_utils.LWE_RNG_128_BIT_SECURITY
RLWE_RNG_128_BIT_SECURITY = test_utils.RLWE_RNG_128_BIT_SECURITY
SCHEME_PARAMS_128_BIT_SECURITY = test_utils.SCHEME_PARAMS_128_BIT_SECURITY
BSK_DECOMP_PARAMS_128_BIT_SECURITY = (
    test_utils.BSK_DECOMP_PARAMS_128_BIT_SECURITY
)
KSK_DECOMP_PARAMS_128_BIT_SECURITY = (
    test_utils.KSK_DECOMP_PARAMS_128_BIT_SECURITY
)
ConsistencyChecker = test_utils.ConsistencyChecker
assert_safe_modulus_switch = test_utils.assert_safe_modulus_switch
MidBootstrapDecrypter = test_utils.MidBootstrapDecrypter
