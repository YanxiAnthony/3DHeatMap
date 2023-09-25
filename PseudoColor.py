import matplotlib

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np
import cv2
import os
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

    images = Image.open(file_path)

    # Resize the image to the target size (224x224)
    # image = image.resize((280, 280))
    image = cv2.imread(file_path)
    image = cv2.resize(image, (320, 280))
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Convert the image to a NumPy array
    image_array = np.array(images)

    colors = image_array / 255

    X = np.arange(0, 320, 1)
    Y = np.arange(0, 280, 1)
    X, Y = np.meshgrid(X, Y)
    H, S, V = cv2.split(hsv_image)
    Z = H

    # Convert the image to grayscale (1 channel)

    surf = ax.plot_surface(X, -Y, -Z, facecolors=colors, cmap="rainbow", linewidth=0, antialiased=False)

    ax.set_zlim(np.min(Z), np.max(Z))
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))

    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()

else:
    messagebox.showwarning("警告", "未能正确找到图像！")
