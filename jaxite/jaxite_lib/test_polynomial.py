"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import test_polynomial

gen_test_polynomial = test_polynomial.gen_test_polynomial
identity_test_polynomial = test_polynomial.identity_test_polynomial
trivial_encryption = test_polynomial.trivial_encryption
gen_and_encrypt = test_polynomial.gen_and_encrypt
