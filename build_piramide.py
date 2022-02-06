level = 2000


def build_piramide(level):
    for i in range(0, level):
        print("0",end=' ')
    print("\n")

    if level-1 > 0:
        build_piramide(level -1)

if __name__ == "__main__":
    build_piramide(level)
