from __future__ import annotations

import numpy as np


def zoom_image(image: np.ndarray, factor: int = 2, target_size: int = 400) \
        -> np.ndarray:
    """Return a centered square crop of the image, kept at target_size."""
    if not isinstance(image, np.ndarray):
        raise TypeError("image must be a NumPy array")
    if image.ndim not in (2, 3):
        raise ValueError("image must be a 2D or 3D NumPy array")

    height, width = image.shape[:2]
    side = min(height, width, target_size)
    if side <= 0:
        raise ValueError("Image is too small to crop a valid square.")

    start_y = max(0, (height - side) // 2)
    start_x = max(0, (width - side) // 2)
    end_y = start_y + side
    end_x = start_x + side

    crop = image[start_y:end_y, start_x:end_x]
    return crop


def ft_rotate(array: np.ndarray) -> np.ndarray:
    """Rotate a 2D or 3D image array by 90 degrees clockwise."""
    if array.ndim == 2:
        rows, cols = array.shape
        return array.T[:, ::-1]
    if array.ndim == 3:
        rows, cols, channels = array.shape
        rotated = np.empty((cols, rows, channels), dtype=array.dtype)
        for i in range(rows):
            for j in range(cols):
                rotated[cols - 1 - j, i, :] = array[i, j, :]
        return rotated
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
    print(image)

    zoomed = zoom_image(image, factor=2)

    rotated = ft_rotate(zoomed)
    print(f"New shape after Transpose: {rotated.shape}")
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
