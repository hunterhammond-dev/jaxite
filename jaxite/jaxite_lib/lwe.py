"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import lwe

LweSecretKey = lwe.LweSecretKey
gen_key = lwe.gen_key
encrypt = lwe.encrypt
jit_encrypt = lwe.jit_encrypt
decrypt_without_denoising = lwe.decrypt_without_denoising
decrypt = lwe.decrypt
noiseless_embedding = lwe.noiseless_embedding
switch_modulus = lwe.switch_modulus
