import math

class delievery_fee:
    def Fees(self, n, value):
        pgp_nor = 34*n
        pgp_sen = 38*n
        xpd_sea_large = 45 + value*0.07

        if n <= 3:
            xpd_sea_small = 50*math.floor(n)
        if n > 3:
            xpd_sea_small = 150+8.8*math.floor(n-3)
        
        if n <= 1:
            xpd_air_nor = 50
            xpd_air_sen = 60
        elif 1 < n <= 2:
            xpd_air_nor = 72
            xpd_air_sen = 88
        elif 2 < n <= 3:
            xpd_air_nor = 94
            xpd_air_sen = 116
        else:
            xpd_air_nor = 94+math.floor(n-2)*27
            xpd_air_sen = 116+math.floor(n-2)*30
        
        print('包裹总重：%s kg, 税费：%0.2f \nPGP普通包裹：%0.2f \nPGP敏感包裹：%0.2f \n小坡岛海运大包：%0.2f \n小坡岛海运小包：%0.2f \n小坡岛空运普通：%0.2f \n小坡岛空运敏感：%0.2f' %(n, value*0.07, pgp_nor, pgp_sen, xpd_sea_large, xpd_sea_small, xpd_air_nor, xpd_air_sen))

        #return pgp_nor, pgp_sen, xpd_sea_large, xpd_sea_small, xpd_air_nor,xpd_air_sen

        
#n = float(input("The overall weight (kg):"))
value = float(input("How much are the packages (rmb):"))

fee = delievery_fee()
fee.Fees(n, value)