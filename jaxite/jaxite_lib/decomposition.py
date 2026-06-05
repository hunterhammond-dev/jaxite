"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import decomposition

DecomposedInt = decomposition.DecomposedInt
GadgetMatrix = decomposition.GadgetMatrix
GadgetDecomp = decomposition.GadgetDecomp
DecompositionParameters = decomposition.DecompositionParameters
decompose = decomposition.decompose
recomposition_summands = decomposition.recomposition_summands
recompose = decomposition.recompose
signed_decomposition = decomposition.signed_decomposition
signed_decomposition_polynomial = decomposition.signed_decomposition_polynomial
signed_decomposition_polynomial_list = (
    decomposition.signed_decomposition_polynomial_list
)
decompose_rlwe_ciphertext = decomposition.decompose_rlwe_ciphertext
gadget_matrix = decomposition.gadget_matrix
inverse_gadget = decomposition.inverse_gadget
