"""Transitional proxy module forwarding to jaxite_cggi."""

# Deprecated compatibility alias forwarding to jaxite_cggi
from jaxite.jaxite_cggi import jax_helpers

tree_flatten = jax_helpers.tree_flatten
tree_unflatten = jax_helpers.tree_unflatten
tree_map = jax_helpers.tree_map
batch_vmap = jax_helpers.batch_vmap
get_tpu_version = jax_helpers.get_tpu_version
