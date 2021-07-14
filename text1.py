class Car():
    def __init__(self, carName, color, feature, price):
        self.carName = carName
        self.color = color
        self.feature = feature
        self.price = price

    def checkPrice(self):
        print("The Price of the Car is ", self.price)

    def checkColor(self):
        print("The Color Of the Car is ", self.color)

    def checkFeature(self):
        print("The Feature Of the Car is ", self.feature)


Audi1 = Car("Audi A4 40 TFSI Premium Plus", "white", "Audi A4 40 TFSI Premium Plus is the petrol variant in the A4 lineup and is priced at ₹ 43.19 Lakh.It returns a certified mileage of 17.42 kmpl. This 40 TFSI Premium Plus variant comes with an engine putting out 188 bhp @ 4200 rpm and 320 Nm @ 1450 rpm of max power and max torque respectively. Audi A4 40 TFSI Premium Plus is available in Automatic(Dual Clutch) transmission and offered in 5 colours: Mythos Black Metallic, Navarra Blue Metallic, Terra Grey Metallic, Floret Silver Metallic and Ibis White.", 4300019)
Audi2 = Car("Audi A6", "Silver","The Audi A6 has 1 Petrol Engine on offer. The Petrol engine is 1984 cc . It is available with the Automatic transmission. Depending upon the variant and fuel type the A6 has a mileage of 14.11 kmpl. The A6 is a 5 seater and has length of 4939mm, width of 2110mm and a wheelbase of 2924mm.", 6100089)
BMW1 = Car("BMW 330i","blue","MW 3 Series 330i M Sport is the petrol variant in the 3 Series lineup and is priced at ₹ 56.64 Lakh.It returns a certified mileage of 16.13 kmpl. This 330i M Sport variant comes with an engine putting out 255 bhp @ 5000 rpm and 400 Nm @ 1550 rpm of max power and max torque respectively. BMW 3 Series 330i M Sport is available in Automatic (Torque Converter) transmission and offered in 4 colours: Portimao Blue, Black Sapphire Metallic, Mineral Grey Metallic and Alpine White.", 5600000)
BMW2 = Car("BMW 540i", "white", "If quiet luxury and handsome styling are high on your new-car priorities list, the 2021 BMW 5-series sedan could very well be the answer. Its spacious and plush cabin is a pleasant place to spend your commute, and BMW offers a host of powertrain options to suit your needs, be they fuel efficiency or roaring V-8 performance. A facelift for 2021 brings sharper exterior styling that gives the 5-series an even more upscale appearance, and several tech upgrades should keep it in the fight against key rivals such as the Audi A6, the Genesis G80, and the Mercedes-Benz E-class.", 7000000)
BMW1.checkPrice() 
Audi1.checkFeature()
Audi1.checkColor()
