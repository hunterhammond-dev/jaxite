"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import bootstrap as bootstrap_mod

GEN_BSK_NUM_BATCHES = bootstrap_mod.GEN_BSK_NUM_BATCHES
NON_DIVISIBLE_BATCH_SIZE_WARNING = (
    bootstrap_mod.NON_DIVISIBLE_BATCH_SIZE_WARNING
)
BootstrappingKey = bootstrap_mod.BootstrappingKey
gen_bootstrapping_key = bootstrap_mod.gen_bootstrapping_key
gen_bsk = bootstrap_mod.gen_bootstrapping_key
jit_bootstrap = bootstrap_mod.jit_bootstrap
bootstrap = bootstrap_mod.bootstrap
external_product = bootstrap_mod.external_product
jit_external_product = bootstrap_mod.jit_external_product
cmux = bootstrap_mod.cmux
jit_cmux = bootstrap_mod.jit_cmux
blind_rotate = bootstrap_mod.blind_rotate
jit_blind_rotate = bootstrap_mod.jit_blind_rotate
sample_extract = bootstrap_mod.sample_extract
jit_sample_extract = bootstrap_mod.jit_sample_extract
