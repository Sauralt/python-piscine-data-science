from PIL import Image
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """Load an image from the given path and return it as a NumPy array."""
    try:
        img = Image.open(path)
    except FileNotFoundError as e:
        raise FileNotFoundError("the image cannot be loaded") from e
    return np.array(img)


if __name__ == "__main__":
    print(ft_load("landscape.jpg"))
