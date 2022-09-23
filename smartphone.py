from re import I


print("Hoe duur is de iPhone")
iphonePrijs = int(input(""))
print("Hoe duur is de Samsung")
samsungPrijs = int(input(""))


    
if samsungPrijs < iphonePrijs <= samsungPrijs + 50:
    prijs = samsungPrijs + 50 - samsungPrijs
    print(f"De iPhone is het duurst, de telefoon kost: {iphonePrijs} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro")
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {prijs} euro duurder")
elif samsungPrijs > iphonePrijs:
    prijs = samsungPrijs - iphonePrijs
    print(f"De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro")
    print(f"De iPhone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro")
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {prijs} euro goedkoper")
elif iphonePrijs > samsungPrijs:
    prijs = iphonePrijs - samsungPrijs
    print(f"De iPhone is het duurst, de telefoon kost: {iphonePrijs} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro")
    print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {prijs} euro goedkoper")




