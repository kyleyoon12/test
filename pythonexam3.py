def search(x,y,z):
    if x+y+z == 180:
        if x<90 and y<90 and z<90:
            print("예각삼각형 입니다.")

        elif x==90 or y==90 or z==90:
            print("직각삼각형 입니다.")

        elif x>90 or y>90 or z>90:
            print("둔각삼각형 입니다.")

    else:
        print("삼각형이 아닙니다.")


a = int(input("제1각: "))
b = int(input("제2각: "))
c = int(input("제3각: "))

print(search(a,b,c))