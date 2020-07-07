OneDigits=["one","two","three","four","five","six","seven","eight","nine"]
TwoDigits=["ten","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninty"]
TwoDigitWords=["eleven","tweleve","thirteen","forteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
    
def twodigitreturn(number):
    if number<10:
        Word=OneDigits[number-1]
    elif number>10 and number<20:
        Word=TwoDigitWords[(number%10)-1]
    else:
        Word= TwoDigits[int((number/10)-1)]+" "+OneDigits[(number%10)-1]
    return(Word)
    
def threedigitreturn(number):
    Word=OneDigits[int((number/100)-1)]+" Hundred "+twodigitreturn(number%100)
    return(Word)

def fivedigitreturn(number):
    Word=twodigitreturn(int(number/1000))+" Thousand "+threedigitreturn(number%1000)
    return(Word)

def sixdigitreturn(number):
    Word=OneDigits[int((number/100000)-1)]+" Lakh "+fivedigitreturn(number%100000)
    return(Word)

def Digit2Number(NonDecimalValue,DecimalValue):
    if int(DecimalValue)>99:
        return("Decimal Value cannot be greater than 99, Invalid Input")
    else:
        if len(DecimalValue)==1:
            DecimalWord=OneDigits[int(DecimalValue-1)]+ " Paise"
        else:
            DecimalWord=twodigitreturn(int(DecimalValue))+ " Paise"
        if len(NonDecimalValue)==1:
            NonDecimalWord=OneDigits[int(NonDecimalValue)-1]+" Rupee"
        if len(NonDecimalValue)==2:
            NonDecimalWord=twodigitreturn(int(NonDecimalValue))+" Rupee"
        if len(NonDecimalValue)==3:
            NonDecimalWord=threedigitreturn(int(NonDecimalValue))+" Rupee"
        if len(NonDecimalValue)==4 or len(NonDecimalValue)==5 :
            NonDecimalWord=fivedigitreturn(int(NonDecimalValue))+" Rupee"
        if len(NonDecimalValue)==6:
            NonDecimalWord=sixdigitreturn(int(NonDecimalValue))+" Rupee"
        return(NonDecimalWord+" "+DecimalWord+" Only")

def CheckNumber(Numbers):
    try:
        Check=float(Numbers)
    except:
        return("Not a Valid Number")
    if Check>999999.99:
        return("Number Exceding Max range (0-999999.99), Try with number in range")
    elif Check<0:
        return("Number Below Min range (0-999999.99), Try with number in range")
    else:
        Numbers=Numbers.split(".")
        ReturnValue=Digit2Number(Numbers[0],Numbers[1])
        return(ReturnValue)

if __name__=="__main__":
    Numbers=input("Enter the number:")
    print(CheckNumber(Numbers))

