import matplotlib.pyplot as plt
from torchvision.transforms import transforms
import numpy as np


def visualize(image, noisy_image, GT, anomaly_map, index, category) :
    for idx, img in enumerate(image):
        plt.figure(figsize=(11,11))
        plt.axis('off')
        plt.subplot(1, 4, 1)
        plt.imshow(show_tensor_image(image[idx]))
        plt.title('clear image')


        plt.subplot(1, 4, 2)
        plt.imshow(show_tensor_image(noisy_image[idx]))
        plt.title('reconstructed image')
        

       
        plt.subplot(1, 4, 3)
        plt.imshow(show_tensor_mask(GT[idx]))
        plt.title('ground truth')

        plt.subplot(1, 4, 4)
        plt.imshow(show_tensor_mask(anomaly_map[idx]))
        plt.title('result')
        plt.savefig('results/{}sample{}.png'.format(category,index+idx))
        plt.close()



def show_tensor_image(image):
    reverse_transforms = transforms.Compose([
        transforms.Lambda(lambda t: (t + 1) / (2)),
        transforms.Lambda(lambda t: t.permute(1, 2, 0)), # CHW to HWC
        transforms.Lambda(lambda t: t * 255.),
        transforms.Lambda(lambda t: t.cpu().numpy().astype(np.uint8)),
        transforms.ToPILImage(),
    ])

    # Take first image of batch
    if len(image.shape) == 4:
        image = image[0, :, :, :] 
    return reverse_transforms(image)

def show_tensor_mask(image):
    reverse_transforms = transforms.Compose([
       # transforms.Lambda(lambda t: (t + 1) / 2),
        transforms.Lambda(lambda t: t.permute(1, 2, 0)), # CHW to HWC
       # transforms.Lambda(lambda t: t * 255.),
        transforms.Lambda(lambda t: t.cpu().numpy().astype(np.uint8)),
     #   transforms.ToPILImage(),
    ])

    # Take first image of batch
    if len(image.shape) == 4:
        image = image[0, :, :, :] 
    return reverse_transforms(image)
        