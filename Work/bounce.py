# bounce.py
#
# Exercise 1.5
def bounceBall(n: int) -> None:
    height = 100 # meters

    for bounce in range(1, n+1):
        bh = (height * 3)/5
        print(bounce, end = ' ')
        print(round(bh, 4))
        height = bh

def main():
    bounceBall(10)

if __name__ == '__main__':
    main()
