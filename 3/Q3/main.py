inputs = input().strip().split()
n, index = int(inputs[0]), int(inputs[1])

color_list = sorted([color for color in input().strip().split()]) 

seen_color = [color for color in input().strip().split()]

sum = 0
for color in seen_color:
    sum += color_list.index(color)

guess = color_list[(index - sum) % n]

print(guess)