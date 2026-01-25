"""
AgentMode - AI Agent optimized output module for SourceSage

This module provides context-aware output modes for AI agents (like Claude Code)
to efficiently explore and analyze codebases without exceeding context limits.
"""

from .agent_output import AgentOutput
from .tree_with_stats import TreeWithStats
from .context_limiter import ContextLimiter
from .file_selector import FileSelector

__all__ = [
    "AgentOutput",
    "TreeWithStats",
    "ContextLimiter",
    "FileSelector",
]
