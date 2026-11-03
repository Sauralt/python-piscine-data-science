from __future__ import annotations
import numpy as np


def _check_rgb(array: np.ndarray) -> None:
    if array.ndim != 3 or array.shape[2] != 3:
        raise ValueError("The input array must be a 3D RGB image.")


def ft_invert(array: np.ndarray) -> np.ndarray:
    """Inverts the color of the image received."""
    _check_rgb(array)
    return 255 - array


def ft_red(array: np.ndarray) -> np.ndarray:
    """Keeps only the red channel of the image."""
    _check_rgb(array)
    result = np.zeros_like(array)
    result[:, :, 0] = array[:, :, 0]
    return result


def ft_green(array: np.ndarray) -> np.ndarray:
    """Keeps only the green channel of the image."""
    _check_rgb(array)
    result = np.zeros_like(array)
    result[:, :, 1] = array[:, :, 1]
    return result


def ft_blue(array: np.ndarray) -> np.ndarray:
    """Keeps only the blue channel of the image."""
    _check_rgb(array)
    result = np.zeros_like(array)
    result[:, :, 2] = array[:, :, 2]
    return result


def ft_grey(array: np.ndarray) -> np.ndarray:
    """Converts the image to grayscale."""
    _check_rgb(array)
    grey = np.mean(array, axis=2, dtype=np.float64).astype(np.uint8)
    return np.stack((grey, grey, grey), axis=2)


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

    try:
        array = ft_load("landscape.jpg")
    except Exception as exc:
        print(f"Error: {exc}")
        return

    transformed = [
        ("Original", array),
        ("Invert", ft_invert(array.copy())),
        ("Red", ft_red(array.copy())),
        ("Green", ft_green(array.copy())),
        ("Blue", ft_blue(array.copy())),
        ("Grey", ft_grey(array.copy())),
    ]

    print(array)

    import matplotlib.pyplot as plt

    fig, axes = plt.subplots(2, 3, figsize=(12, 8))
    axes = axes.flatten()

    for ax, (title, image) in zip(axes, transformed):
        ax.imshow(image)
        ax.set_title(title)
        ax.axis("off")

    plt.tight_layout()
    plt.show()
    print(ft_invert.__doc__)


if __name__ == "__main__":
    main()
