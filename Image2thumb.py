#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import glob
from PIL import Image

class Image2thumbnail():

  ##############################
  # イメージ作成               #
  ##############################
  def ImageNew(self, size):
    # とりあえずRGB,背景黒固定
    return Image.new('RGB', (size, size), (0x00, 0x00, 0x00))
  
  ##############################
  # イメージ読み出し           #
  ##############################
  def ImageRead(self, path):
    return Image.open(path)
  
  ##############################
  # サムネイル取得             #
  ##############################
  def GetThumbnail(self, image, size):
    # とりあえずアンチエイリアス固定
    return image.thumbnail((size, size), getattr(Image, 'ANTIALIAS'))
  
  ##############################
  # サムネイル描画             #
  ##############################
  def DrawThumbnail(self, in_image, in_size, out_image, x, y):
    tmp = in_image.crop((0, 0, in_size, in_size))
    out_image.paste(tmp, (x, y, x + in_size, y + in_size))
    return out_image
  
  ##############################
  # サムネイル保存             #
  ##############################
  def WriteThumbnail(self, out_image, out_path):
    out_image.save(out_path)

def main():
  if len(sys.argv) != 2:
    print('Usage : > python %s dirname' % sys.argv[0])
    quit()
  thumbsize = 100
  count = 0
  for path in glob.glob(sys.argv[1] + '/*'):
    count += 1
  for x in range(100):
    if x ** 2 >= count:
      break
  i = 0
  i2t = Image2thumbnail()
  out_img = i2t.ImageNew(thumbsize * x)
  for path in glob.glob(sys.argv[1] + '/*'):
    in_img = i2t.ImageRead(path)
    i2t.GetThumbnail(in_img, thumbsize)
    out_img = i2t.DrawThumbnail(in_img, thumbsize, out_img, (i % x) * thumbsize, (i // x) * thumbsize)
    i += 1
  i2t.WriteThumbnail(out_img, sys.argv[1] + '/thumb.jpg')

if __name__ == "__main__":
  sys.exit(main())
