import numpy as np
import matplotlib.pyplot as plt

# ============================================
# =========some lines must be comment=========
# ============================================

x = []
y = []
z = []
w = []

with open("Output.txt") as f:
    file = f.read().split("\n")
    for i in file:
        x.append(float(i.split(",")[0]))
        y.append(float(i.split(",")[1]))
        z.append(float(i.split(",")[2]))                            #comment when not needed
        #w.append(float(i.split(",")[3]))                            #comment when not needed

# Нормализация цветовой информации (если необходимо)
#w_normalized = (w - np.min(w)) / (np.max(w) - np.min(w))            #comment when not needed
#z_normalized = (z - np.min(z)) / (np.max(z) - np.min(z))            #comment when not needed

# Создание 3D графика
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# print(len(z), len(w))
# print(set(x), set(y), set(z), set(w))

# Построение точек на графике с цветовым градиентом
scatter = ax.scatter(y, z, x, cmap='viridis', s=50)

# Добавление цветовой шкалы
cbar = plt.colorbar(scatter)
cbar.set_label('Color Gradient')

# Настройка осей
ax.set_xlabel('X Axis')
ax.set_ylabel('Y Axis')
ax.set_zlabel('Z Axis')

# Отображение графика
plt.show()
