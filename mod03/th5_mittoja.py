##Yksi leiviskä on 20 naulaa
##Yksi naula on 32 luotia
##Yksi luoti on 13,3 grammaa

##Kysy leiviskät
leiviskät = float(input("Anna leiviskät "))

##Kysy naulat
naulat = float(input("Anna naulat "))

##Kysy luodit
luodit = float(input("Anna luodit "))

##Muunna mittasuhteet
##Leiviskät * 20 naulaa
##Naulat * 32 luotia
##Luodit * 13,3g

naulat_lasku = (leiviskät * 20)
luodit_lasku = ((naulat + naulat_lasku) * 32)
grammat_lasku = ((luodit + luodit_lasku) * 13.3)

##Muunna grammat kilogrammoiksi
##1000g = 1kg

kilogramma = (grammat_lasku // 1000)
jakojäännös = (grammat_lasku % 1000)

print(f"Massa nykymittojen mukaan on{kilogramma: .0f} kilogrammaa ja{jakojäännös: .2f} grammaa")