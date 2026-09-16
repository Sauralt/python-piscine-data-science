from __future__ import annotations

import numpy as np


def zoom_image(image, factor: int = 2, target_size: int = 400):
    """Return a centered square crop of the image, capped at 400x400."""
    if image.ndim == 2:
        height, width = image.shape
    else:
        height, width, _ = image.shape

    side = min(height, width, target_size)
    if side <= 0:
        raise ValueError("Image is too small to crop a valid square.")

    center_y = height // 2
    center_x = width // 2
    y0 = max(0, center_y - side // 2)
    y1 = min(height, y0 + side)
    x0 = max(0, center_x - side // 2)
    x1 = min(width, x0 + side)

    if (y1 - y0) != side or (x1 - x0) != side:
        y0 = max(0, center_y - side // 2)
        y1 = y0 + side
        x0 = max(0, center_x - side // 2)
        x1 = x0 + side

    return image[y0:y1, x0:x1]


def ft_rotate(array: np.ndarray) -> np.ndarray:
    """Rotate an image array by 90 degrees counter-clockwise."""
    if array.ndim == 2:
        return np.rot90(array)
    if array.ndim == 3:
        return np.rot90(array)
    raise ValueError("The input must be a 2D or 3D NumPy array.")


def main() -> None:
    try:
        from load_image import ft_load
    except Exception as exc:
        print(f"Error: unable to import loader: {exc}")
        return

    try:
        image = ft_load("animal.jpeg")
    except Exception as exc:
        print(f"Error: {exc}")
        return

    print(f"Original shape: {image.shape}")
    print(f"Original dtype: {image.dtype}")
    print("Original pixels:")
    print(image)

    zoomed = zoom_image(image, factor=2)
    print(f"Zoomed shape: {zoomed.shape}")
    print("Zoomed pixels:")
    print(zoomed)

    rotated = ft_rotate(zoomed)
    print(f"Rotated shape: {rotated.shape}")
    print("Rotated pixels:")
    print(rotated)

    try:
        import matplotlib.pyplot as plt
        plt.figure("Zoomed and rotated image")
        plt.imshow(rotated)
        plt.title("Zoomed and rotated image")
        plt.xlabel("X axis")
        plt.ylabel("Y axis")
        plt.show()
    except ImportError:
        try:
            from PIL import Image
            Image.fromarray(rotated).show()
        except Exception as exc:
            print(f"Error: unable to display image: {exc}")
    except Exception as exc:
        print(f"Error: unable to display image: {exc}")


if __name__ == "__main__":
    main()
