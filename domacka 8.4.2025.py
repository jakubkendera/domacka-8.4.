from PIL import image

fr=open("ciernobiely_obrazok_1.txt","r",encoding="UTF-8")
riadok=fr.readline() #zoberieme iba prvy riadok
sirka, vyska=riadok.strip().split()
sirka=int(sirka)
vyska=int(vyska)

obrazok=Image.new("RGB",(sirka,vyska),(255,255,255))
pixels=obrazok.load()
pixels[10,10]=(0,0,0)
pixels[11,10]=(0,0,0)
pixels[12,10]=(0,0,0)

obrazok.save("ciernobielyObrazok.png")
obrazok.show()
