from textnode import TextNode, TextType

def main():
    node = TextNode('The quick brown fox jumps over the lazy dog', TextType.LINK, 'https://www.feasting.com')
    print(node)

if __name__ == "__main__":
    main()