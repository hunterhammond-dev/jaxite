"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import rlwe

RlwePlaintext = rlwe.RlwePlaintext
RlweCiphertext = rlwe.RlweCiphertext
RlweSecretKey = rlwe.RlweSecretKey
gen_key = rlwe.gen_key
encrypt = rlwe.encrypt
jit_encrypt = rlwe.jit_encrypt
decrypt = rlwe.decrypt
flatten_key = rlwe.flatten_key
