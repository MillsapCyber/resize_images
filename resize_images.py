import os, re, argparse
from PIL import Image


def resize(path, type):
    dirs = os.listdir(path)
    if not os.path.exists(path + 'resized'):
        os.mkdir(path + 'resized')
    if type == 'png':
        func = resize_png
    elif type == 'jpg':
        func = resize_jpg
    else:
        exit(-1)

    for item in dirs:
        if os.path.isfile(path + item):
            im = Image.open(path + item)
            func(im, item, path)


def resize_png(im, item, path):
    im_resize = im.resize((args.width, args.height), Image.ANTIALIAS)
    p = path + 'resized/' + re.search('(.+?)(\.[^.]*$|$)', item).group(1) + '.png'
    im_resize.save(p, 'PNG', quality=90)


def resize_jpg(im, item, path):
    im = im.convert("RGB")
    im_resize = im.resize((args.width, args.height), Image.ANTIALIAS)
    p = path + 'resized/' + re.search('(.+?)(\.[^.]*$|$)', item).group(1) + '.jpg'
    im_resize.save(p, 'JPEG', quality=90)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Resize all image in the specified directory to width x height (default=500x500)')
    parser.add_argument('-p', '--path', type=str, metavar='',
                        required=True, help='File path of the directory containing the images')
    parser.add_argument('-x', '--width', type=int, default=500, metavar='',
                        required=False, help='width you want to resized image to be')
    parser.add_argument('-y', '--height', type=int, default=500, metavar='',
                        required=False, help='height you want to resized image to be')
    parser.add_argument('-t', '--type', type=str, default='png', metavar='',
                        required=False, help='type of image you want (png/jpg)')

    args = parser.parse_args()
    # replace \'s with /'s for windows ppl
    p = args.path.replace("\\", "/")
    # add trailing slash
    if p[-1] != "/":
        p = p + "/"

    resize(p, args.type)
