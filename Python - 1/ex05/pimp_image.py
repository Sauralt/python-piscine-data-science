
from __future__ import annotations

import numpy as np


def _check_rgb(array: np.ndarray) -> None:
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("The input array must be a 3D RGB image.")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Invert all color channels while keeping the same image shape."""
    _check_rgb(array)
    result = array.copy()
    result[:, :, 0] = 255 - result[:, :, 0]
    result[:, :, 1] = 255 - result[:, :, 1]
    result[:, :, 2] = 255 - result[:, :, 2]
    return result


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keep only the red channel and set other channels to zero."""
    _check_rgb(array)
    result = array.copy()
    result[:, :, 1] = result[:, :, 1] * 0
    result[:, :, 2] = result[:, :, 2] * 0
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keep only the green channel and set other channels to zero."""
    _check_rgb(array)
    result = array.copy()
    result[:, :, 0] = result[:, :, 0] - result[:, :, 0]
    result[:, :, 2] = result[:, :, 2] - result[:, :, 2]
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keep only the blue channel and set other channels to zero."""
    _check_rgb(array)
    result = array.copy()
    result[:, :, 0] = 0
    result[:, :, 1] = 0
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Convert an RGB image to grayscale while preserving shape."""
    _check_rgb(array)
    result = array.copy()
    grey = (result[:, :, 0] + result[:, :, 1] + result[:, :, 2]) / 3
    result[:, :, 0] = grey
    result[:, :, 1] = grey
    result[:, :, 2] = grey
    return result


def display_filters(array: np.ndarray) -> None:
    import matplotlib.pyplot as plt

    filters = [
        ("Original", array.copy()),
        ("Invert", ft_invert(array.copy())),
        ("Red", ft_red(array.copy())),
        ("Green", ft_green(array.copy())),
        ("Blue", ft_blue(array.copy())),
        ("Grey", ft_grey(array.copy())),
    ]

    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.flatten()

    for ax, (title, image) in zip(axes, filters):
        ax.imshow(image)
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()


def main() -> None:
    try:
        from load_image import ft_load
    except ImportError as exc:
        print(f"Error: unable to import loader: {exc}")
        return

    image = ft_load("landscape.jpg")
    display_filters(image)


if __name__ == "__main__":
    main()