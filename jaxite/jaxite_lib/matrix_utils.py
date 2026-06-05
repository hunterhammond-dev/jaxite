"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import matrix_utils

integer_div = matrix_utils.integer_div
x_power_n_minus_1 = matrix_utils.x_power_n_minus_1
int32_to_int8_arr = matrix_utils.int32_to_int8_arr
i32_as_u8_matmul = matrix_utils.i32_as_u8_matmul
hpmatmul_conv_adapt_outer_product = (
    matrix_utils.hpmatmul_conv_adapt_outer_product
)
hpmatmul_conv_adapt_conv = matrix_utils.hpmatmul_conv_adapt_conv
chunk_decomposition = matrix_utils.chunk_decomposition
rechunkify_after_chunkwise_add = matrix_utils.rechunkify_after_chunkwise_add
smul_as_dense_gemv_bat = matrix_utils.smul_as_dense_gemv_bat
smul_as_dense_gemv_bat_jax = matrix_utils.smul_as_dense_gemv_bat_jax
hpmatmul_offline_compile_bat = matrix_utils.hpmatmul_offline_compile_bat
hpmatmul_bat_adapt = matrix_utils.hpmatmul_bat_adapt
hpmatmul_golden = matrix_utils.hpmatmul_golden
toeplitz = matrix_utils.toeplitz
toeplitz_kernelized = matrix_utils.toeplitz_kernelized
toeplitz_poly_mul = matrix_utils.toeplitz_poly_mul
poly_mul = matrix_utils.poly_mul
monomial_mul = matrix_utils.monomial_mul
monomial_mul_list = matrix_utils.monomial_mul_list
poly_mul_list = matrix_utils.poly_mul_list
poly_mul_const_list = matrix_utils.poly_mul_const_list
poly_mul_const_matrix = matrix_utils.poly_mul_const_matrix
monomial_mul_matrix = matrix_utils.monomial_mul_matrix
poly_dot_product = matrix_utils.poly_dot_product
scale_by_x_power_n_minus_1 = matrix_utils.scale_by_x_power_n_minus_1
