import colorgram
colors = colorgram.extract("hirst_painting.jpg", 30)
rgb_list = [tuple(c.rgb) for c in colors]
bg_color_1 = rgb_list.pop(0)
bg_color_2 = rgb_list.pop(0)