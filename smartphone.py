print("Hoe duur is de iPhone")
iphonePrijs = int(input(""))
print("Hoe duur is de Samsung")
samsungPrijs = int(input(""))

max = 900

if iphonePrijs >= max and samsungPrijs <= max:
    print(f"De iPhone is het duurst, de telefoon kost: {iphonePrijs} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro")
    print(f"Het advies is dus de Samsung te kopen, de iPhone is te duur")

elif iphonePrijs <= max and samsungPrijs >= max:
    print(f"De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro")
    print(f"De iPhone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro")
    print(f"Het advies is dus de iPhone te kopen, de Samsung is te duur")

elif iphonePrijs >= max and samsungPrijs >= max:
    print("Allebei de telefoons zijn te duur")

elif iphonePrijs > samsungPrijs:
    prijs = iphonePrijs - samsungPrijs
    print(f"De iPhone is het duurst, de telefoon kost: {iphonePrijs} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro")
    print(f"Het advies is dus de Samsung te kopen. Deze is namelijk {prijs} euro goedkoper")

elif samsungPrijs < iphonePrijs <= samsungPrijs + 50:
    prijs = samsungPrijs + 50 - samsungPrijs
    print(f"De iPhone is het duurst, de telefoon kost: {iphonePrijs} Euro")
    print(f"De Samsung is het goedkoopst, de telefoon kost: {samsungPrijs} Euro")
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {prijs} euro duurder")

elif samsungPrijs > iphonePrijs:
    prijs = samsungPrijs - iphonePrijs
    print(f"De Samsung is het duurst, de telefoon kost: {samsungPrijs} Euro")
    print(f"De iPhone is het goedkoopst, de telefoon kost: {iphonePrijs} Euro")
    print(f"Het advies is dus de iPhone te kopen. Deze is namelijk {prijs} euro goedkoper")




