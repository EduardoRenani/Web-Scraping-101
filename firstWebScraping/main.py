from urllib.request import urlopen
from bs4 import BeautifulSoup as soup

#URL a ser acessada
my_url = 'http://www.newegg.com/Video-Cards-Video-Devices/Category/ID-38?Tpk=graphics%20card'
#abrindo conexao e pegando a pagina
uClient = urlopen(my_url)
#guardando o conteudo da pagina numa variavel
page_html = uClient.read()
#fechando o cliente.
uClient.close()

#parseando o conteudo em html (poderia ser xml, por exemplo)
page_soup = soup(page_html, "html.parser")

containers = page_soup.findAll("div",{"class":"item-container"})

filename = "products.csv"
f = open(filename, "w")
headers = "brand, product_name, shipping\n"
f.write(headers)


for container in containers:
    brand = container.div.div.a.img["title"]

    title_container = container.findAll("a", {"class":"item-title"})
    product_name = title_container[0].text

    shipping_container = container.findAll("li",{"class":"price-ship"})
    shipping = shipping_container[0].text.strip()

    print("brand: " + brand)
    print("product_name: " + product_name)
    print("shipping: " + shipping)

    f.write(brand + "," + product_name.replace(",", "|") + "," + shipping + "\n")