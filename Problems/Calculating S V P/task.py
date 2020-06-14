# put your python code here
length = int(input())
width = int(input())
height = int(input())

sum_lengths = 4 * (length + width + height)
surface_area = 2 * (length * width + width * height + length * height)
volume = length * width * height
print(sum_lengths)
print(surface_area)
print(volume)