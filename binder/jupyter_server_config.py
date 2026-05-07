"""Binder-specific Jupyter server settings."""

# Public Binder sessions have a small memory budget. Cull idle kernels even if
# their notebook tab is still open so moving through the tutorial does not keep
# every previous notebook kernel resident in memory.
c.MappingKernelManager.cull_idle_timeout = 120
c.MappingKernelManager.cull_interval = 30
c.MappingKernelManager.cull_connected = True
c.MappingKernelManager.cull_busy = False
