import matplotlib.pyplot as plt
import requests
import os



latex_code = r'\frac{a}{b} = c'
webhook_url = 'webhook'



def create_latex_image(latex_code, filename='latex_image.png'):
    plt.figure(figsize=(5, 2))
    plt.text(0.5, 0.5, f"${latex_code}$", fontsize=20, ha='center', va='center')
    plt.axis('off')
    plt.savefig(filename, bbox_inches='tight', pad_inches=0.1)
    plt.close()

def send_image_to_discord(webhook_url, image_path):
    with open(image_path, 'rb') as f:
        response = requests.post(
            webhook_url,
            files={'file': f}
        )
    return response.status_code, response.content


create_latex_image(latex_code)
status_code, response_content = send_image_to_discord(webhook_url, 'latex_image.png')
os.remove('latex_image.png')



print(f'Status Code: {status_code}, Response: {response_content}')


