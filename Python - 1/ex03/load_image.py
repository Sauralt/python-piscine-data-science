from __future__ import annotations
from typing import Any
from PIL import Image
import numpy as np


def ft_load(path: str) -> Any:
    """Load an image from the given path and return it as a NumPy array."""
    try:
        with Image.open(path) as img:
            array = np.array(img)
            print(f"The shape of image is: {array.shape}")
            return array
    except FileNotFoundError as exc:
        raise FileNotFoundError(f"Image not found: {path}") from exc
    except Exception as exc:
        raise RuntimeError(f"Unable to load image '{path}': {exc}") from exc
