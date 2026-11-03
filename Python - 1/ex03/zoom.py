from __future__ import annotations
import numpy as np


def zoom_image(image: np.ndarray, factor: int = 2, target_size: int = 400) \
        -> np.ndarray:
    """Return a centered square crop of the image, capped at target_size."""
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
    if factor > 1:
        return crop[::factor, ::factor]
    return crop


def main():
    try:
        from load_image import ft_load
    except ImportError as exc:
        print(f"Error: unable to import loader: {exc}")
        return

    try:
        img = ft_load("animal.jpeg")
    except Exception as exc:
        print(f"Error: {exc}")
        return

    height, width = img.shape[:2]

    print(img)

    zoomed = zoom_image(img, factor=2)
    print(f"The shape of image after zoom is: {zoomed.shape}")
    print(zoomed)

    try:
        import matplotlib.pyplot as plt
        plt.figure("Zoomed image")
        ax = plt.gca()
        ax.imshow(zoomed)
        ax.set_title("Zoomed image")
        ax.set_xlabel("X axis")
        ax.set_ylabel("Y axis")
        plt.show()
    except ImportError:
        print("Warning: matplotlib is not installed; image display skipped.")
    except Exception as exc:
        print(f"Error: unable to display image: {exc}")


if __name__ == "__main__":
    main()
