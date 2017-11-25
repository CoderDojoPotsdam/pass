import os
import re
import html

TEXT1 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt1"
TEXT2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt2"
GÜRTEL_FARBE = "2c9725"

class Gürtel:

    def __init__(mein, svg_pfad):
        with open(svg_pfad) as datei:
            mein.svg_inhalt = datei.read()
        mein.ordner = os.path.splitext(svg_pfad)[0]
        os.makedirs(mein.ordner, exist_ok=True)

    def _erzeuge(mein, name, farbe, text):
        datei_name = os.path.join(mein.ordner, name + ".svg")
        inhalt = mein.svg_inhalt.replace(GÜRTEL_FARBE, farbe)
        texts = text.split("\n\n")
        assert len(texts) <= 2
        texts = [html.escape(re.sub("^\s+|\s+$", "", text)) for text in texts]
        print("texts", texts)
        inhalt = inhalt.replace(TEXT1, texts[0])
        if len(texts) == 2:
            inhalt = inhalt.replace(TEXT2, texts[1])
        with open(datei_name, "w") as datei:
            datei.write(inhalt)
    
    def weiß(mein, text):
        mein._erzeuge("weiß", "ffffff", text)
        
    def gelb(mein, text):
        mein._erzeuge("gelb", "ffff00", text)

    def orange(mein, text):
        mein._erzeuge("orange", "ff6600", text)
        
    def grün(mein, text):
        mein._erzeuge("grün", "00ff00", text)
        
    def blau(mein, text):
        mein._erzeuge("blau", "0000ff", text)
        
    def braun(mein, text):
        mein._erzeuge("braun", "c87137", text)
        
    def schwarz(mein, text):
        mein._erzeuge("schwarz", "000000", text)
        

