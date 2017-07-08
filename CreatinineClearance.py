print ("Welcome to the Creatinine Calculator")
Plasma_C = float(input("Enter your Plasma Creatinine in umol/L: "))
Urine_C = float(input("Enter your Urine Creatinine for 24hours in umol/L: "))
Urine_V = float(input("Enter the 24h volume of urine in ml/day: "))
Body_Area = float(input("Enter the estimated surface volume of the patient in square meters. If unavailable, enter 0. If you have the height and weight enter 8 to access the algorithm: "))
Crea_Con = 86400
CRCL = (Urine_C * Urine_V) / (Plasma_C * 86400)

if Body_Area == 0:
    print("Your creatinine clearance is : " + str(round(CRCL,2)) + "ml/s")
elif Body_Area == 8:
    Height = float(input("Enter the patient's height in centimeters: "))
    Weight = float(input("Enter the patient's weight in kilograms: "))
    Mosteller_Area = ((Weight*Height)/ 3600)
    Mosteller_AreaReal = Mosteller_Area**0.5 #Need to Calculate the Square root in the Mosteller formula
    print ("Estimated BSA of: " + str(Mosteller_AreaReal))
    MostellerCL = ((Urine_C * Urine_V) / (Plasma_C * 86400)) * (1.73 / Mosteller_AreaReal)
    print("Your corrected creatinine clearance is : " + str(round(MostellerCL, 2)) + "ml/s")
else:
    CorrectedCL = ((Urine_C * Urine_V) / (Plasma_C * 86400)) * (1.73 / Body_Area)
    print("Your corrected creatinine clearance is : " + str(round(CorrectedCL,2)) + "ml/s")