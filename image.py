from PIL import Image
from shizukani import randomfname
from icrawler.builtin import GoogleImageCrawler
import os


class ImageConverts:
    
    def __init__(self):
        self.files = []
    
    def convert_to_png(self, filepath:str) -> str:
        if filepath[-3:] != "png":
            img = Image.open(filepath)
            f1 = randomfname(10) + ".png"
            img.save(f1)
            f2 = os.path.abspath(f1)
            self.files += [f2]
            
        else:
            f2 = os.path.abspath(filepath)
        
        return f2
    
    def delfiles(self) -> None:
        for file in self.files:
            os.remove(file)


class Scraping:
    def __init__(self, name:str, num=1, path="images"):
        GoogleImageCrawler(storage = {"root_dir" : path}).crawl(keyword=name, max_num=num)

    def crawling(self, name:str, num=1, path="images"):
        print("call crawling", name)
        GoogleImageCrawler(storage = {"root_dir" : path}).crawl(keyword=name, max_num=num)
        
    def scrapings(self, *args, path="images") -> None:
        dirname = randomfname(10)
        names = [(args[i * 2], int(args[i * 2 + 1])) for i in range(len(args) // 2)]
        for i in names:
            self.__init__(i[0], num=i[1], path=path+"/"+dirname)
            count = 1
            os.rename(path + "/" + dirname + "/" + (fname := os.listdir(path + "/" + dirname)),
                       path + "/" + i[0] + str(count) + fname[fname.index(".") - 1])
        os.rmdir(path + "/" + dirname)

    def fnamescraping(self, filename:str, name:str, path="images") -> None:
        dirname = randomfname(10)
        self.__init__(self, name, 1, path + "/" + dirname)
        os.rename(path + "/" + dirname + "/" + (fname := os.listdir(path + "/" + dirname)[0]),
                  path + "/" + filename + fname[fname.index(".") - 1])
        os.rmdir(path + "/" + dirname)
    
    def pngscraping(self, name:str, num=1, path="images") -> None:
        dirname = randomfname(10)
        self.crawling(name, num, path + "/" + dirname)
        converter = ImageConverts()
        for fname in os.listdir(path + "/" + dirname):
            converter.convert_to_png(fname)
        for i, fname in enumerate(converter.files):
            os.rename(path + "/" + dirname + "/" + fname, path + "/" + str(i).zfill(6) + ".png")
        converter.delfiles()
        os.rmdir(path + "/" + dirname)
