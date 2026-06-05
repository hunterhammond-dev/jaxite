"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import polymul_kernel

fallback_vector_matrix_polymul = polymul_kernel.fallback_vector_matrix_polymul
fallback_i32_matmul = polymul_kernel.fallback_i32_matmul
bat_matmul = polymul_kernel.bat_matmul
negacyclic_vector_matrix_polymul = (
    polymul_kernel.negacyclic_vector_matrix_polymul
)
negacyclic_vector_matrix_polymul_bat = (
    polymul_kernel.negacyclic_vector_matrix_polymul_bat
)
i32_matmul_unreduced = polymul_kernel.i32_matmul_unreduced
i32_matmul = polymul_kernel.i32_matmul
