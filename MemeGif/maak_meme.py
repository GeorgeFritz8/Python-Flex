from PIL import Image, ImageFont, ImageDraw

# Achtergrond openen en oplsaan in de variabele met de naam: achtergrond
achtergrond = Image.open("Meme Achtergrond.jpg")

# De breedte en hoogte van de achtergrond lezen en tonen 
breedte = 400
hoogte = 224

# Afmetingen op het scherm zetten
# Met str() zet je een int (getal) naar een string om. Dan kan print() het gebruiken.
print("De achtergrond is " + str(breedte) + " pixels breed en " + str(hoogte) + " pixels hoog")

# Andere info uitlezen en tonen
print(achtergrond.format, achtergrond.size, achtergrond.mode)


lettertype = ImageFont.truetype("impact.ttf", 20)

# Vraag aan de ImageDraw module om een tekengebied te maken op de achtergrond afbeelding
tekengebied = ImageDraw.Draw(achtergrond)

# Tekst schrijven
tekst = "Everybody: Panicking about Corona at work\nMe: Working from home as a Game Developer"
tekengebied.multiline_text((10,10), tekst, font=lettertype, fill=(200,110,20))

# Het resultaat tonen
achtergrond.show()

# En opslaan onder een andere naam
achtergrond.save("meme_met_tekst.jpg")
