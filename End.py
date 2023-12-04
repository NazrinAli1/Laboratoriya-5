from random import uniform
# [1.0, 1.4] aralığında təsadüfən bir başlangıc nöqtəsi seç
starting_point = uniform(1.0, 1.4)

x = starting_point
tolerance = 1e-6
max_iterations = 100

for _ in range(max_iterations):
    x -= (x**5 - x - 2) / (5*x**4 - 1)
    if abs(x**5 - x - 2) < tolerance:
        break

# Hesaplanan kökü ekrana yazdır
print("Təqribi kök:", x)
