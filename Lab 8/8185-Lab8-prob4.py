#Alinkar Lu
#643040818-5
from abc import ABC, abstractmethod

class Image(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod                                                                                                                        
    def load_image(self, filename):
        pass
        
    @abstractmethod
    def save_image(self, filename):
        pass

class Bitmap(Image):
    def load_image(self,filename):
        print(f"loading bitmap file {filename}")

    def save_image(self,filename):
        print(f"saving bitmap file {filename}")

class Jpeg(Image):
    def load_image(self,filename):
        print(f"loading jpeg file {filename}")

    def save_image(self,filename):
        print(f"loading jpeg file {filename}")



if __name__ == "__main__":
    bitmap1 = Bitmap()
    bitmap1.save_image("kku.bmp")
    bitmap1.load_image("kku.bmp")
    jpeg1 = Jpeg()
    jpeg1.save_image("en.jpg")
    jpeg1.load_image("en.jpg")