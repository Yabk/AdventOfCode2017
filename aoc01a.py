#!/usr/bin/python3


if __name__ == '__main__':

    captcha = input('')
    sum = 0

    for i in range (len(captcha)):
        if captcha[i] == captcha[(i+1)%len(captcha)]:
            sum += int(captcha[i])

    print(sum)
