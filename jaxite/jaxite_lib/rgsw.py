"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import rgsw

RgswPlaintext = rgsw.RgswPlaintext
RgswCiphertext = rgsw.RgswCiphertext
RgswSecretKey = rgsw.RgswSecretKey
gen_key = rgsw.gen_key
key_from_rlwe = rgsw.key_from_rlwe
encrypt = rgsw.encrypt
jit_encrypt = rgsw.jit_encrypt
decrypt = rgsw.decrypt
