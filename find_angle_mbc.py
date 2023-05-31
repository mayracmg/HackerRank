import math

ab = int(input())
bc = int(input())

tan_x = ab / bc
angle_radians = math.atan(tan_x)

angle_degrees = round(math.degrees(angle_radians))

print(f'{angle_degrees}\N{DEGREE SIGN}')
