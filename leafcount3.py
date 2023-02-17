# from skimage import io
# from sklearn.cluster import KMeans
# import numpy as np

# # Load the image
# image = io.imread("C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png")

# # Convert the image to a 2D array
# rows = image.shape[0]
# cols = image.shape[1]
# image = image.reshape(rows*cols, 3)

# # Use KMeans to cluster the image into N distinct clusters
# N = 6
# kmeans = KMeans(n_clusters=N, random_state=0).fit(image)

# # Count the number of unique objects in the image
# unique_objects = len(np.unique(kmeans.labels_))

# print("Number of unique objects in the image:", unique_objects)

# import matplotlib.pyplot as plt

# # Get the cluster labels for each pixel
# labels = kmeans.labels_

# # Create a mask for each cluster
# masks = []
# for i in range(N):
#     masks.append(labels.reshape(rows, cols) == i)

# # Plot the original image and masks
# plt.figure(figsize=(20, 10))
# plt.subplot(1, N+1, 1)
# plt.imshow(io.imread("C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png"))
# plt.title("Original Image")

# for i in range(N):
#     plt.subplot(1, N+1, i+2)
#     plt.imshow(masks[i], cmap='gray')
#     plt.title("Cluster {}".format(i))

# plt.show()

# import matplotlib.pyplot as plt
# import numpy as np
# import cv2
# from sklearn.cluster import DBSCAN

# # Load the image
# img = cv2.imread("C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png")
# rows, cols, channels = img.shape

# # Convert the image to a 2D array
# img_2d = img.reshape(-1, channels)

# # Apply HDBSCAN
# clustering = DBSCAN(eps=3, min_samples=2).fit(img_2d)
# labels = clustering.labels_

# # Create a mask for each cluster
# unique_labels = np.unique(labels)
# masks = []
# for label in unique_labels:
#     mask = (labels == label).reshape(rows, cols)
#     masks.append(mask)

# # Plot the original image and masks
# plt.figure(figsize=(20, 10))
# plt.subplot(1, len(unique_labels)+1, 1)
# plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
# plt.title("Original Image")

# for i, mask in enumerate(masks):
#     plt.subplot(1, len(unique_labels)+1, i+2)
#     plt.imshow(mask, cmap='gray')
#     plt.title("Object {}".format(i))

# plt.show()

import matplotlib.pyplot as plt
import numpy as np
import cv2
from sklearn.cluster import DBSCAN

# Load the image
img = cv2.imread("C://Users//derkm//Develop3//psqa//psqa2//Sample_pic//test_image.png")
img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)  # Resize the image
rows, cols, channels = img.shape

# Convert the image to a 2D array
img_2d = img.reshape(-1, channels)

# Apply HDBSCAN
clustering = DBSCAN(eps=3, min_samples=2).fit(img_2d)
labels = clustering.labels_

# Create a mask for each cluster
unique_labels = np.unique(labels)
masks = []
for label in unique_labels:
    mask = (labels == label).reshape(rows, cols)
    masks.append(mask)

# Plot the original image and masks
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title("Original Image")

plt.subplot(1, 2, 2)
plt.imshow(masks[0], cmap='gray')
plt.title("Object 0")

plt.show()



