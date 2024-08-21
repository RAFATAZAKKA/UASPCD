#
# import tkinter as tk
# from tkinter import filedialog
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# img_path = None
# img_original = None
# img_processed = None
# img_plot = None
#
# def open_image():
#     global img_path, img_original, img_processed, img_plot
#     img_path = filedialog.askopenfilename(initialdir="./", title="Pilih Gambar", filetypes=(("Image Files", "*.jpg *.png"), ("All Files", "*.*")))
#     if img_path:
#         img_original = cv2.imread(img_path)
#         img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
#         img_processed = np.copy(img_original)
#         show_image()
#
# def show_image():
#     global img_processed, img_plot
#     if img_plot:
#         img_plot.get_tk_widget().pack_forget()
#     plt.figure(figsize=(8, 6))
#     if len(img_processed.shape) == 2:  # Check if the image is grayscale or binary
#         plt.imshow(img_processed, cmap='gray')
#     else:
#         plt.imshow(img_processed)
#     plt.axis('off')
#     img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
#     img_plot.get_tk_widget().pack()
#
# def convert_to_original():
#     global img_processed, img_original
#     img_processed = np.copy(img_original)
#     show_image()
#
# def convert_to_negative():
#     global img_processed
#     img_processed = 255 - img_processed
#     show_image()
#
# def convert_to_grayscale():
#     global img_processed
#     img_processed = cv2.cvtColor(img_processed, cv2.COLOR_RGB2GRAY)
#     show_image()
#
# def convert_to_black_white():
#     global img_processed
#     img_gray = cv2.cvtColor(img_processed, cv2.COLOR_RGB2GRAY)
#     _, img_processed = cv2.threshold(img_gray, 128, 255, cv2.THRESH_BINARY)
#     show_image()
#
# def sharpen_image():
#     global img_processed
#     kernel = np.array([[0, -1, 0],
#                        [-1, 5, -1],
#                        [0, -1, 0]])
#     img_processed = cv2.filter2D(img_processed, -1, kernel)
#     show_image()
#
# def show_histogram():
#     global img_processed, img_plot
#     if img_plot:
#         img_plot.get_tk_widget().pack_forget()
#     plt.figure(figsize=(8, 6))
#     plt.hist(img_processed.ravel(), 256, [0, 256])
#     plt.title('Histogram')
#     plt.xlabel('Intensitas Piksel')
#     plt.ylabel('Jumlah Piksel')
#     img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
#     img_plot.get_tk_widget().pack()
#
# def save_image():
#     global img_processed
#     save_path = filedialog.asksaveasfilename(initialdir="./", title="Simpan Gambar", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
#     if save_path:
#         if len(img_processed.shape) == 2:  # Grayscale or binary image
#             cv2.imwrite(save_path, img_processed)
#         else:  # Color image
#             cv2.imwrite(save_path, cv2.cvtColor(img_processed, cv2.COLOR_RGB2BGR))
#         print(f"Gambar berhasil disimpan di {save_path}")
#
# root = tk.Tk()
# root.title("Image Processing App")
#
# # Buatkan frame untuk mengatur posisi tombol
# frame_top = tk.Frame(root)
# frame_top.pack(side=tk.TOP, padx=10, pady=10)
#
# frame_bottom = tk.Frame(root)
# frame_bottom.pack(side=tk.BOTTOM, padx=10, pady=10)
#
# btn_open = tk.Button(frame_top, text="Buka Gambar", command=open_image)
# btn_open.pack(side=tk.LEFT, padx=10)
#
# btn_save = tk.Button(frame_top, text="Simpan Gambar", command=save_image)
# btn_save.pack(side=tk.LEFT, padx=10)
#
# btn_original = tk.Button(frame_bottom, text="Tampilkan Gambar Normal", command=convert_to_original)
# btn_original.pack(side=tk.LEFT, padx=10)
#
# btn_negative = tk.Button(frame_bottom, text="Convert to Negative", command=convert_to_negative)
# btn_negative.pack(side=tk.LEFT, padx=10)
#
# btn_grayscale = tk.Button(frame_bottom, text="Convert to Grayscale", command=convert_to_grayscale)
# btn_grayscale.pack(side=tk.LEFT, padx=10)
#
# btn_black_white = tk.Button(frame_bottom, text="Convert to Black & White", command=convert_to_black_white)
# btn_black_white.pack(side=tk.LEFT, padx=10)
#
# btn_sharpen = tk.Button(frame_bottom, text="Sharpen Image", command=sharpen_image)
# btn_sharpen.pack(side=tk.LEFT, padx=10)
#
# btn_histogram = tk.Button(frame_bottom, text="Show Histogram", command=show_histogram)
# btn_histogram.pack(side=tk.LEFT, padx=10)
#
# root.mainloop()
#


# import tkinter as tk
# from tkinter import filedialog
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# img_path = None
# img_original = None
# img_processed = None
# img_plot = None
#
# def open_image():
#     global img_path, img_original, img_processed, img_plot
#     img_path = filedialog.askopenfilename(initialdir="./", title="Pilih Gambar", filetypes=(("Image Files", "*.jpg *.png"), ("All Files", "*.*")))
#     if img_path:
#         img_original = cv2.imread(img_path)
#         img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
#         img_processed = np.copy(img_original)
#         show_image()
#
# def show_image():
#     global img_processed, img_plot
#     if img_plot:
#         img_plot.get_tk_widget().pack_forget()
#     plt.figure(figsize=(8, 6))
#     if len(img_processed.shape) == 2:  # Check if the image is grayscale or binary
#         plt.imshow(img_processed, cmap='gray')
#     else:
#         plt.imshow(img_processed)
#     plt.axis('off')
#     img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
#     img_plot.get_tk_widget().pack()
#
# def convert_to_original():
#     global img_processed, img_original
#     img_processed = np.copy(img_original)
#     show_image()
#
# def increase_contrast():
#     global img_processed
#     if len(img_processed.shape) == 3:  # Color image
#         img_yuv = cv2.cvtColor(img_processed, cv2.COLOR_RGB2YUV)
#         img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
#         img_processed = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
#     else:  # Grayscale image
#         img_processed = cv2.equalizeHist(img_processed)
#     show_image()
#
#
# def sharpen_image():
#     global img_processed
#     kernel = np.array([[0, -1, 0],
#                        [-1, 5, -1],
#                        [0, -1, 0]])
#     img_processed = cv2.filter2D(img_processed, -1, kernel)
#     show_image()
#
#
# def reduce_noise():
#     global img_processed
#     img_processed = cv2.bilateralFilter(img_processed, 9, 75, 75)
#     show_image()
#
#
# def adjust_brightness_contrast():
#     global img_processed, img_original, brightness_slider, contrast_slider
#     brightness = brightness_slider.get()
#     contrast = contrast_slider.get()
#     img_processed = cv2.convertScaleAbs(img_original, alpha=contrast/127.0 + 1, beta=brightness)
#     show_image()
#
#
# def show_histogram():
#     global img_processed, img_plot
#     if img_plot:
#         img_plot.get_tk_widget().pack_forget()
#     plt.figure(figsize=(8, 6))
#     plt.hist(img_processed.ravel(), 256, [0, 256])
#     plt.title('Histogram')
#     plt.xlabel('Intensitas Piksel')
#     plt.ylabel('Jumlah Piksel')
#     img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
#     img_plot.get_tk_widget().pack()
#
# def save_image():
#     global img_processed
#     save_path = filedialog.asksaveasfilename(initialdir="./", title="Simpan Gambar", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
#     if save_path:
#         if len(img_processed.shape) == 2:  # Grayscale or binary image
#             cv2.imwrite(save_path, img_processed)
#         else:  # Color image
#             cv2.imwrite(save_path, cv2.cvtColor(img_processed, cv2.COLOR_RGB2BGR))
#         print(f"Gambar berhasil disimpan di {save_path}")
#
# root = tk.Tk()
# root.title("Image Processing App")
#
# # Buatkan frame untuk mengatur posisi tombol
# frame_top = tk.Frame(root)
# frame_top.pack(side=tk.TOP, padx=10, pady=10)
#
# frame_bottom = tk.Frame(root)
# frame_bottom.pack(side=tk.BOTTOM, padx=10, pady=10)
#
# btn_open = tk.Button(frame_top, text="Buka Gambar", command=open_image)
# btn_open.pack(side=tk.LEFT, padx=10)
#
# btn_save = tk.Button(frame_top, text="Simpan Gambar", command=save_image)
# btn_save.pack(side=tk.LEFT, padx=10)
#
# btn_original = tk.Button(frame_bottom, text="Tampilkan Gambar Normal", command=convert_to_original)
# btn_original.pack(side=tk.LEFT, padx=10)
#
# btn_increase_contrast = tk.Button(frame_bottom, text="Increase Contrast", command=increase_contrast)
# btn_increase_contrast.pack(side=tk.LEFT, padx=10)
#
# btn_sharpen = tk.Button(frame_bottom, text="Sharpen Image", command=sharpen_image)
# btn_sharpen.pack(side=tk.LEFT, padx=10)
#
# btn_reduce_noise = tk.Button(frame_bottom, text="Reduce Noise", command=reduce_noise)
# btn_reduce_noise.pack(side=tk.LEFT, padx=10)
#
# brightness_slider = tk.Scale(frame_bottom, from_=-100, to=100, orient=tk.HORIZONTAL, label="Brightness", command=lambda x: adjust_brightness_contrast())
# brightness_slider.set(0)  # Set default value
# brightness_slider.pack(side=tk.LEFT, padx=10)
#
# contrast_slider = tk.Scale(frame_bottom, from_=-100, to=100, orient=tk.HORIZONTAL, label="Contrast", command=lambda x: adjust_brightness_contrast())
# contrast_slider.set(0)  # Set default value
# contrast_slider.pack(side=tk.LEFT, padx=10)
#
#
# btn_histogram = tk.Button(frame_bottom, text="Show Histogram", command=show_histogram)
# btn_histogram.pack(side=tk.LEFT, padx=10)
#
# root.mainloop()

# import tkinter as tk
# from tkinter import filedialog
# import cv2
# import matplotlib.pyplot as plt
# import numpy as np
# from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
#
# img_path = None
# img_original = None
# img_processed = None
# img_plot = None
#
# def open_image():
#     global img_path, img_original, img_processed, img_plot
#     img_path = filedialog.askopenfilename(initialdir="./", title="Pilih Gambar", filetypes=(("Image Files", "*.jpg *.png"), ("All Files", "*.*")))
#     if img_path:
#         img_original = cv2.imread(img_path)
#         img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
#         img_processed = np.copy(img_original)
#         show_image()
#
# def show_image():
#     global img_processed, img_plot
#     if img_plot:
#         img_plot.get_tk_widget().pack_forget()
#     plt.figure(figsize=(8, 6))
#     if len(img_processed.shape) == 2:  # Check if the image is grayscale or binary
#         plt.imshow(img_processed, cmap='gray')
#     else:
#         plt.imshow(img_processed)
#     plt.axis('off')
#     img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
#     img_plot.get_tk_widget().pack()
#
# def convert_to_original():
#     global img_processed, img_original
#     img_processed = np.copy(img_original)
#     show_image()
#
# def increase_contrast():
#     global img_processed
#     if len(img_processed.shape) == 3:  # Color image
#         img_yuv = cv2.cvtColor(img_processed, cv2.COLOR_RGB2YUV)
#         img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
#         img_processed = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
#     else:  # Grayscale image
#         img_processed = cv2.equalizeHist(img_processed)
#     show_image()
#
# def sharpen_image():
#     global img_processed
#     kernel = np.array([[0, -1, 0],
#                        [-1, 5, -1],
#                        [0, -1, 0]])
#     img_processed = cv2.filter2D(img_processed, -1, kernel)
#     show_image()
#
# def reduce_noise():
#     global img_processed
#     img_processed = cv2.bilateralFilter(img_processed, 9, 75, 75)
#     show_image()
#
# def adjust_brightness_contrast():
#     global img_processed, img_original, brightness_slider, contrast_slider
#     brightness = brightness_slider.get()
#     contrast = contrast_slider.get()
#     img_processed = cv2.convertScaleAbs(img_original, alpha=contrast/127.0 + 1, beta=brightness)
#     show_image()
#
# def show_histogram():
#     global img_processed, img_plot
#     if img_plot:
#         img_plot.get_tk_widget().pack_forget()
#     plt.figure(figsize=(8, 6))
#     plt.hist(img_processed.ravel(), 256, [0, 256])
#     plt.title('Histogram')
#     plt.xlabel('Intensitas Piksel')
#     plt.ylabel('Jumlah Piksel')
#     img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
#     img_plot.get_tk_widget().pack()
#
# def save_image():
#     global img_processed
#     save_path = filedialog.asksaveasfilename(initialdir="./", title="Simpan Gambar", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
#     if save_path:
#         if len(img_processed.shape) == 2:  # Grayscale or binary image
#             cv2.imwrite(save_path, img_processed)
#         else:  # Color image
#             cv2.imwrite(save_path, cv2.cvtColor(img_processed, cv2.COLOR_RGB2BGR))
#         print(f"Gambar berhasil disimpan di {save_path}")
#
# root = tk.Tk()
# root.title("Image Processing App")
#
# # Warna background
# root.configure(bg='#2e3f4f')
#
# # Buatkan frame untuk mengatur posisi tombol
# frame_top = tk.Frame(root, bg='#2e3f4f')
# frame_top.pack(side=tk.TOP, padx=10, pady=10)
#
# frame_bottom = tk.Frame(root, bg='#2e3f4f')
# frame_bottom.pack(side=tk.BOTTOM, padx=10, pady=10)
#
# # Style untuk tombol
# btn_style = {'bg': '#4caf50', 'fg': 'white', 'font': ('Helvetica', 10, 'bold')}
#
# btn_open = tk.Button(frame_top, text="Buka Gambar", command=open_image, **btn_style)
# btn_open.pack(side=tk.LEFT, padx=10)
#
# btn_save = tk.Button(frame_top, text="Simpan Gambar", command=save_image, **btn_style)
# btn_save.pack(side=tk.LEFT, padx=10)
#
# btn_original = tk.Button(frame_bottom, text="Tampilkan Gambar Normal", command=convert_to_original, **btn_style)
# btn_original.pack(side=tk.LEFT, padx=10)
#
# btn_increase_contrast = tk.Button(frame_bottom, text="Increase Contrast", command=increase_contrast, **btn_style)
# btn_increase_contrast.pack(side=tk.LEFT, padx=10)
#
# btn_sharpen = tk.Button(frame_bottom, text="Sharpen Image", command=sharpen_image, **btn_style)
# btn_sharpen.pack(side=tk.LEFT, padx=10)
#
# btn_reduce_noise = tk.Button(frame_bottom, text="Reduce Noise", command=reduce_noise, **btn_style)
# btn_reduce_noise.pack(side=tk.LEFT, padx=10)
#
# # Tambahkan slider untuk penyesuaian kecerahan dan kontras
# slider_style = {'bg': '#2e3f4f', 'fg': 'white', 'font': ('Helvetica', 10)}
#
# brightness_slider = tk.Scale(frame_bottom, from_=-100, to=100, orient=tk.HORIZONTAL, label="Brightness", command=lambda x: adjust_brightness_contrast(), **slider_style)
# brightness_slider.set(0)  # Set default value
# brightness_slider.pack(side=tk.LEFT, padx=10)
#
# contrast_slider = tk.Scale(frame_bottom, from_=-100, to=100, orient=tk.HORIZONTAL, label="Contrast", command=lambda x: adjust_brightness_contrast(), **slider_style)
# contrast_slider.set(0)  # Set default value
# contrast_slider.pack(side=tk.LEFT, padx=10)
#
# btn_histogram = tk.Button(frame_bottom, text="Show Histogram", command=show_histogram, **btn_style)
# btn_histogram.pack(side=tk.LEFT, padx=10)
#
# root.mainloop()

import tkinter as tk
from tkinter import filedialog
import cv2
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

img_path = None
img_original = None
img_processed = None
img_plot = None

def open_image():
    global img_path, img_original, img_processed, img_plot
    try:
        img_path = filedialog.askopenfilename(initialdir="./", title="Pilih Gambar", filetypes=(("Image Files", "*.jpg *.png"), ("All Files", "*.*")))
        if img_path:
            img_original = cv2.imread(img_path)
            img_original = cv2.cvtColor(img_original, cv2.COLOR_BGR2RGB)
            img_processed = np.copy(img_original)
            show_image()
    except Exception as e:
        print(f"Error opening image: {e}")

def show_image():
    global img_processed, img_plot
    if img_plot:
        img_plot.get_tk_widget().pack_forget()
    plt.figure(figsize=(8, 6))
    if len(img_processed.shape) == 2:  # Check if the image is grayscale or binary
        plt.imshow(img_processed, cmap='gray')
    else:
        plt.imshow(img_processed)
    plt.axis('off')
    img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
    img_plot.get_tk_widget().pack()

def convert_to_original():
    global img_processed, img_original
    img_processed = np.copy(img_original)
    show_image()

def increase_contrast():
    global img_processed
    if len(img_processed.shape) == 3:  # Color image
        img_yuv = cv2.cvtColor(img_processed, cv2.COLOR_RGB2YUV)
        img_yuv[:, :, 0] = cv2.equalizeHist(img_yuv[:, :, 0])
        img_processed = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2RGB)
    else:  # Grayscale image
        img_processed = cv2.equalizeHist(img_processed)
    show_image()

def sharpen_image():
    global img_processed
    kernel = np.array([[0, -1, 0],
                       [-1, 5, -1],
                       [0, -1, 0]])
    img_processed = cv2.filter2D(img_processed, -1, kernel)
    show_image()

def reduce_noise():
    global img_processed
    img_processed = cv2.bilateralFilter(img_processed, 9, 75, 75)
    show_image()

def adjust_brightness_contrast():
    global img_processed, img_original, brightness_slider, contrast_slider
    brightness = brightness_slider.get()
    contrast = contrast_slider.get()
    img_processed = cv2.convertScaleAbs(img_original, alpha=contrast/127.0 + 1, beta=brightness)
    show_image()

def show_histogram():
    global img_processed, img_plot
    if img_plot:
        img_plot.get_tk_widget().pack_forget()
    plt.figure(figsize=(8, 6))
    plt.hist(img_processed.ravel(), 256, [0, 256])
    plt.title('Histogram')
    plt.xlabel('Intensitas Piksel')
    plt.ylabel('Jumlah Piksel')
    img_plot = FigureCanvasTkAgg(plt.gcf(), master=root)
    img_plot.get_tk_widget().pack()

def save_image():
    global img_processed
    try:
        save_path = filedialog.asksaveasfilename(initialdir="./", title="Simpan Gambar", filetypes=(("JPEG files", "*.jpg"), ("PNG files", "*.png"), ("All files", "*.*")))
        if save_path:
            if len(img_processed.shape) == 2:  # Grayscale or binary image
                cv2.imwrite(save_path, img_processed)
            else:  # Color image
                cv2.imwrite(save_path, cv2.cvtColor(img_processed, cv2.COLOR_RGB2BGR))
            print(f"Gambar berhasil disimpan di {save_path}")
    except Exception as e:
        print(f"Error saving image: {e}")

root = tk.Tk()
root.title("Image Processing App")

# Warna background
root.configure(bg='#2e3f4f')

# Buatkan frame untuk mengatur posisi tombol
frame_top = tk.Frame(root, bg='#2e3f4f')
frame_top.pack(side=tk.TOP, padx=10, pady=10)

frame_bottom = tk.Frame(root, bg='#2e3f4f')
frame_bottom.pack(side=tk.BOTTOM, padx=10, pady=10)

# Style untuk tombol
btn_style = {'bg': '#4caf50', 'fg': 'white', 'font': ('Helvetica', 10, 'bold')}

btn_open = tk.Button(frame_top, text="Buka Gambar", command=open_image, **btn_style)
btn_open.pack(side=tk.LEFT, padx=10)

btn_save = tk.Button(frame_top, text="Simpan Gambar", command=save_image, **btn_style)
btn_save.pack(side=tk.LEFT, padx=10)

btn_original = tk.Button(frame_bottom, text="Tampilkan Gambar Normal", command=convert_to_original, **btn_style)
btn_original.pack(side=tk.LEFT, padx=10)

btn_increase_contrast = tk.Button(frame_bottom, text="Increase Contrast", command=increase_contrast, **btn_style)
btn_increase_contrast.pack(side=tk.LEFT, padx=10)

btn_sharpen = tk.Button(frame_bottom, text="Sharpen Image", command=sharpen_image, **btn_style)
btn_sharpen.pack(side=tk.LEFT, padx=10)

btn_reduce_noise = tk.Button(frame_bottom, text="Reduce Noise", command=reduce_noise, **btn_style)
btn_reduce_noise.pack(side=tk.LEFT, padx=10)

# Tambahkan slider untuk penyesuaian kecerahan dan kontras
slider_style = {'bg': '#2e3f4f'}  # Hanya bg yang valid

brightness_slider = tk.Scale(frame_bottom, from_=-100, to=100, orient=tk.HORIZONTAL, label="Brightness", command=lambda x: adjust_brightness_contrast(), **slider_style)
brightness_slider.set(0)  # Set default value
brightness_slider.pack(side=tk.LEFT, padx=10)

contrast_slider = tk.Scale(frame_bottom, from_=-100, to=100, orient=tk.HORIZONTAL, label="Contrast", command=lambda x: adjust_brightness_contrast(), **slider_style)
contrast_slider.set(0)  # Set default value
contrast_slider.pack(side=tk.LEFT, padx=10)

btn_histogram = tk.Button(frame_bottom, text="Show Histogram", command=show_histogram, **btn_style)
btn_histogram.pack(side=tk.LEFT, padx=10)

root.mainloop()

