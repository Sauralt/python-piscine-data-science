from __future__ import annotations


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
    channels = img.shape[2] if img.ndim == 3 else 1

    print(f"Image size: {width} x {height}")
    print(f"Number of channels: {channels}")
    print("Pixel content:")
    print(img)

    zoomed = zoom_image(img, factor=2)
    print("Zoomed image:")
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
