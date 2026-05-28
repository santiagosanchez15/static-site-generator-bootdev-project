from textnode import TextType, TextNode

def main():

    node = TextNode(text='some random text', text_type=TextType.LINK, url= 'https://www.boot.dev/lessons/cdae7fca-a7dc-4706-b2c5-7a03d66db1c9')
    print(node)

main()