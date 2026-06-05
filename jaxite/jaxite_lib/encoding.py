"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import encoding

EncodingParameters = encoding.EncodingParameters
encode = encoding.encode
decode_without_removing_padding = encoding.decode_without_removing_padding
decode = encoding.decode
remove_noise = encoding.remove_noise
round_to_power_of_2 = encoding.round_to_power_of_2
extract_noise = encoding.extract_noise
