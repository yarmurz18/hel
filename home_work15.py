import requests
url = "https://dummyjson.com/products?limit=200"
response = requests.get(url)
products: list[dict] = response.json()["products"]
for product in products:
    if product.get("brand") == "TechGear":
        print(product["id"])
    if product["id"] == 135:
        product_images = product["images"]
        for image_url in product_images:
            response2 = requests.get(image_url)
            with open("phone.png", mode="wb") as file:
                file.write(response2.content)
