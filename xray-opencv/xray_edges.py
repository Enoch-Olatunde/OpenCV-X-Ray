import cv2
import matplotlib.pyplot as plt
import numpy as np

# 1. Load - replace with your file: NIH sample, Kaggle chest X-ray
# download sample: https://nihcc.app.box.com/v/ChestXray-NIHCC
img_path = 'Knee_X-ray.png' # put any X-ray/MRI here
img = cv2.imread(img_path)
if img is None:
    # fallback: create synthetic for testing
    print("No image found, using sample from OpenCV")
    img = cv2.imread(cv2.samples.findFile('lena.png'))

# 2. Process
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (5,5), 0)
edges = cv2.Canny(blurred, 30, 100)

# 3. Plot side-by-side
fig, axs = plt.subplots(1,3, figsize=(15,5))
axs[0].imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
axs[0].set_title('Original')
axs[0].axis('off')
axs[1].imshow(gray, cmap='gray')
axs[1].set_title('Grayscale')
axs[1].axis('off')
axs[2].imshow(edges, cmap='gray')
axs[2].set_title('Canny Edges')
axs[2].axis('off')
plt.tight_layout()
plt.savefig('xray_result.png', dpi=300)
plt.show()
