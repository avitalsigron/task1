
import matplotlib.pyplot as plt
import numpy as np

# קריאת התמונה
image = plt.imread('/ss.jpg')

# חישוב ההיסטוגרמה
r_hist = np.histogram(image[:,:,0], bins=256, range=(0, 256))
g_hist = np.histogram(image[:,:,1], bins=256, range=(0, 256))
b_hist = np.histogram(image[:,:,2], bins=256, range=(0, 256))

# תצוגה של ההיסטוגרמה
plt.figure(figsize=(8, 20)) # מסגרת היסטוגרמה
plt.title('RGB Histogram')
plt.xlabel('Intensity')
plt.ylabel('Frequency')
plt.xlim([0, 256])
plt.plot(r_hist[1][:-1], r_hist[0], color='r', alpha=0.7, label='Red')
plt.plot(g_hist[1][:-1], g_hist[0], color='g', alpha=0.7, label='Green')
plt.plot(b_hist[1][:-1], b_hist[0], color='b', alpha=0.7, label='Blue')
plt.legend() # מיצג את הקווים
plt.show()
