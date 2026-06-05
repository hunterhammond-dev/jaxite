"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import key_switch

LweKeySwitchingKey = key_switch.LweKeySwitchingKey
gen_key = key_switch.gen_key
switch_key = key_switch.switch_key
jit_switch_key = key_switch.jit_switch_key
