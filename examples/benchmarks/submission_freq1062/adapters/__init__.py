"""Memory system adapters — auto-discovered by run.py."""

from .memanto import MemantoAdapter
from .mem0 import Mem0Adapter
from .cognee import CogneeAdapter
from .letta import LettaAdapter
from .zep_graphiti import ZepAdapter
from .supermemory import SupermemoryAdapter
from .vector_baseline import VectorBaselineAdapter

__all__ = [
    "MemantoAdapter",
    "Mem0Adapter",
    "CogneeAdapter",
    "LettaAdapter",
    "ZepAdapter",
    "SupermemoryAdapter",
    "VectorBaselineAdapter",
]
