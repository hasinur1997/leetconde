# Flipping an image

def flip_and_invert_image(image):
    for i in range(len(image)):
        image[i].reverse()

        for j in range(len(image[i])):
            if image[i][j] == 0:
                image[i][j] = 1
            else:
                image[i][j] = 0
    return image

print(flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]))



