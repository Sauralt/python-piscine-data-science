from __future__ import annotations
from typing import Any


def ft_load(path: str) -> Any:
    """Load an image from a path and return it as a NumPy array."""
    try:
        import numpy as np
        from PIL import Image
    except ImportError as exc:
        raise RuntimeError("Missing dependency: install Pillow and NumPy") \
            from exc

    try:
        with Image.open(path) as img:
            return np.array(img)
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Image not found: {path}") from exc
    except Exception as exc:
        raise RuntimeError(f"Unable to load image '{path}': {exc}") from exc
