from datetime import datetime
from datetime import date

class Loan:
    def loan_system(self,amount,time,date):
        month=["Januray","Feburary","March","April","May","June","July","August","September","October","November","December"]
        date=str(date)
        date_num=date.split("-")[-1]
        # print(date_num)
        print("Loan Creation Date:",date)
        print("Principal Amount:",amount)
        print("Number of EMI's:",time)
        rate=12
        year=time/12
        Total_Interest=(amount*rate*year)/100
        EMI_month=Total_Interest/12
        Total_Amount_Payable=amount+Total_Interest
        print("EMI Details:")
        today=datetime.now()
        month_name=today.strftime("%B")
        index = month.index(month_name)-1
        serial_number = 0
        Principal_remaining=Total_Amount_Payable
        year=2020
        principal=amount/12
        for i in range(time):
            serial_number+=1
            index=index+1
            EMI_month_name=month[index]
            if EMI_month_name=="December":
                index=-1
                year=year+1
            li = [date_num, EMI_month_name, year]
            total_emi=principal+EMI_month
            Principal_remaining=Principal_remaining-total_emi
            EMI_Date="-".join(map(str,li))
            print("EMI Number",serial_number,",","Principal EMI:",principal,",","Interest EMI=",EMI_month,
                                              ",","Total EMI=",total_emi,",",
                                            "EMI Date:",EMI_Date,",",
                  "Principal Remaining:",Principal_remaining,end="\n")

print("Enter Loan Amount:",end=" ")
amount=int(input())
print("Enter number of months:",end=" ")
time=int(input())
today=date.today()
s=Loan()
s.loan_system(amount,time,today)
