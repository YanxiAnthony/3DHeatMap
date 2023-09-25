import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import os
import sys
import tkinter as tk
from tkinter import messagebox, filedialog
from PIL import Image

# 创建一个Tkinter窗口来打开文件对话框
root = tk.Tk()
root.withdraw()  # 隐藏Tkinter窗口

# 打开文件对话框并获取用户选择的图像文件路径
file_path = filedialog.askopenfilename(title="选择图像文件",
                                       filetypes=[("图像文件", "*.png *.jpg *.jpeg *.bmp *.gif *.tiff")])

# base_directory = os.path.abspath(os.path.join(os.path.dirname(sys.executable)))
# file_name = "PseudoColorImg.jpg"
# file_path = os.path.join(base_directory, "data", "temp", "pseudoColor_img_area", file_name)

if os.path.exists(file_path):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    X = np.arange(0, 280, 1)
    Y = np.arange(0, 280, 1)
    X, Y = np.meshgrid(X, Y)
    image = Image.open(file_path)

    # Resize the image to the target size (224x224)
    image = image.resize((280, 280))

    # Convert the image to a NumPy array
    image_array = np.array(image)
    # 遍历图像中的每个像素，并打印它们的RGB值
    for i in range(image_array.shape[0]):
        for j in range(image_array.shape[1]):
            pixel_rgb = image_array[i, j]
            print(f"Pixel at ({i}, {j}): R={pixel_rgb[0]}, G={pixel_rgb[1]}, B={pixel_rgb[2]}")

    colors = image_array / 255

    # Convert the image to grayscale (1 channel)
    Z = np.array(image.convert('L'))

    surf = ax.plot_surface(X, -Y, Z, facecolors=colors, cmap="rainbow", linewidth=0, antialiased=False)

    ax.set_zlim(np.min(Z), np.max(Z))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    # # 隐藏X、Y、Z轴上的数值
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_zticks([])
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

else:
    messagebox.showwarning("警告", "未能正确找到图像！")
