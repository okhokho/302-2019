from tkinter import *
def centre_window(window):
    window.update_idletasks()
    w = window.winfo_screenwidth()
    h = window.winfo_screenheight()
    size = tuple(int(_) for _ in window.geometry().split('+')[0].split('x'))
    x = w/2 - size[0]/2
    y = h/2 - size[1]/2
    window.geometry("%dx%d+%d+%d" % (size + (x, y)))

def tax1():


    def tax():
        window_01 = Toplevel(window_00)
        window_01.geometry("540x540")
        centre_window(window_01)
        window_01.title('Tax')
        hys = val_hys.get()
        wys = val_wys.get()
        def hmi():
            hmi = int(hys)
            return round(hmi/12,2)
        def hmpf():
            hmpf = int(hys)
            if hmpf < 85200:  # $7100*12
                hmpf = 0
                return hmpf
            else:
                if hmpf < 360000:  # $30000*12
                    hmpf = hmpf * 0.05
                    return hmpf
                else:
                    hmpf = 18000  # >$30000*12
                    return hmpf
        def hni():
            hni = int(hys) - int(hmpf())
            return hni
        def hBasicallowance():
            hBasicallowance = 132000
            return hBasicallowance

        def hNetChargeableIncome():
            hNetChargeableIncome = int(hni())-int(hBasicallowance())
            if hNetChargeableIncome <= 0:
                hNetChargeableIncome = 0
                return hNetChargeableIncome
            else: return hNetChargeableIncome


        def hfirst():
            hfirst = int(hNetChargeableIncome())
            if hfirst <= 50000:
                hfirst = hfirst*0.02
                return hfirst
            else: hfirst = 1000
            return hfirst

        def hsecond():
            hsecond = int(hNetChargeableIncome())
            if hsecond<= 100000 and hsecond > 50000:
                hsecond = (hsecond-50000)*0.06
                return hsecond
            else:
                if hsecond > 100000:
                    hsecond = 3000
                    return hsecond
                else: hsecond = 0*100
                return hsecond

        def hthird():
            hthird = int(hNetChargeableIncome())
            if hthird<= 150000 and hthird > 100000:
                hthird = (hthird-100000)*0.1
                return hthird
            else:
                if hthird > 150000:
                    hthird = 5000
                    return hthird
                else: hthird = 0*100
                return hthird

        def hfourth():
            hfourth = int(hNetChargeableIncome())
            if hfourth<= 200000 and hfourth > 150000:
                hfourth = (hfourth-150000)*0.14
                return hfourth
            else:
                if hfourth > 200000:
                    hfourth = 7000
                    return hfourth
                else: hfourth = 0*100
                return hfourth
        def hremain():
            hremain = int(hNetChargeableIncome())
            if hremain > 200000:
                return (hremain-200000)*0.17
            else: hremain = 0*100
            return hremain


        def hTaxthereon():
            print(hni())
            hTaxthereon2 = int(hni()) * 0.15
            print(hTaxthereon2)
            hTaxthereon1 = int(hremain())+int(hfourth())+int(hthird())+int(hsecond())+int(hfirst())
            if hTaxthereon1 > hTaxthereon2:
                hTaxthereon = hTaxthereon2
                return hTaxthereon
            else:
                hTaxthereon = hTaxthereon1
                return hTaxthereon




        def htaxredution():
            htaxredution = 0
            return htaxredution

        def hTaxpayable():
            hTaxpayable = int(hTaxthereon())-int(htaxredution())
            return hTaxpayable

        def wmi():
            wmi = int(wys)
            return round(wmi/12,2)
        def wmpf():
            wmpf = int(wys)
            if wmpf < 85200:  # $7100*12
                wmpf = 0
                return wmpf
            else:
                if wmpf < 360000:  # $30000*12
                    wmpf = wmpf * 0.05
                    return wmpf
                else:
                    wmpf = 18000  # >$30000*12
                    return wmpf
        def wni():
            wni = int(wys) - int(wmpf())
            return wni

        def wBasicallowance():
            wBasicallowance = 132000
            return wBasicallowance

        def wNetChargeableIncome():
            wNetChargeableIncome = int(wni())-int(wBasicallowance())
            if wNetChargeableIncome <= 0:
                wNetChargeableIncome = 0
                return wNetChargeableIncome
            else: return wNetChargeableIncome


        def wfirst():
            wfirst = int(wNetChargeableIncome())
            if wfirst <= 50000:
                wfirst = wfirst*0.02
                return wfirst
            else: wfirst = 1000
            return wfirst

        def wsecond():
            wsecond = int(wNetChargeableIncome())
            if wsecond<= 100000 and wsecond > 50000:
                wsecond = (wsecond-50000)*0.06
                return wsecond
            else:
                if wsecond > 100000:
                    wsecond = 3000
                    return wsecond
                else: wsecond = 0*100
                return wsecond

        def wthird():
            wthird = int(wNetChargeableIncome())
            if wthird<= 150000 and wthird > 100000:
                wthird = (wthird-100000)*0.1
                return wthird
            else:
                if wthird > 150000:
                    wthird = 5000
                    return wthird
                else: wthird = 0*100
                return wthird

        def wfourth():
            wfourth = int(wNetChargeableIncome())
            if wfourth<= 200000 and wfourth > 150000:
                wfourth = (wfourth-150000)*0.14
                return wfourth
            else:
                if wfourth > 200000:
                    wfourth = 7000
                    return wfourth
                else: wfourth = 0*100
                return wfourth
        def wremain():
            wremain = int(wNetChargeableIncome())
            if wremain > 200000:
                return (wremain-200000)*0.17
            else: wremain = 0*100
            return wremain

        def wTaxthereon():
            wTaxthereon2 = int(wni()) * 0.15
            wTaxthereon1 = int(wremain())+int(wfourth())+int(wthird())+int(wsecond())+int(wfirst())
            if wTaxthereon1 > wTaxthereon2:
                wTaxthereon = wTaxthereon2
                return wTaxthereon
            else:
                wTaxthereon = wTaxthereon1
                return wTaxthereon

        def wtaxredution():
            wtaxredution = 0
            return wtaxredution

        def wTaxpayable():
            wTaxpayable = int(wTaxthereon())-int(wtaxredution())
            return wTaxpayable

        def jni():
            jni = int(wni()) + int(hni())
            return jni

        def jBasicallowance():
            jBasicallowance = 264000
            return jBasicallowance

        def jNetChargeableIncome():
            jNetChargeableIncome = int(jni())-int(jBasicallowance())
            if jNetChargeableIncome <= 0:
                jNetChargeableIncome = 0
                return jNetChargeableIncome
            else: return jNetChargeableIncome


        def jfirst():
            jfirst = int(jNetChargeableIncome())
            if jfirst <= 50000:
                jfirst = jfirst*0.02
                return jfirst
            else: jfirst = 1000
            return jfirst

        def jsecond():
            jsecond = int(jNetChargeableIncome())
            if jsecond<= 100000 and jsecond > 50000:
                jsecond = (jsecond-50000)*0.06
                return jsecond
            else:
                if jsecond > 100000:
                    jsecond = 3000
                    return jsecond
                else: jsecond = 0*100
                return jsecond

        def jthird():
            jthird = int(jNetChargeableIncome())
            if jthird<= 150000 and jthird > 100000:
                jthird = (jthird-100000)*0.1
                return jthird
            else:
                if jthird > 150000:
                    jthird = 5000
                    return jthird
                else: jthird = 0*100
                return jthird

        def jfourth():
            jfourth = int(jNetChargeableIncome())
            if jfourth<= 200000 and jfourth > 150000:
                jfourth = (jfourth-150000)*0.14
                return jfourth
            else:
                if jfourth > 200000:
                    jfourth = 7000
                    return jfourth
                else: jfourth = 0*100
                return jfourth
        def jremain():
            jremain = int(jNetChargeableIncome())
            if jremain > 200000:
                return (jremain-200000)*0.17
            else: jremain = 0*100
            return jremain

        def jTaxthereon():
            jTaxthereon2 = int(jni()) * 0.15
            jTaxthereon1 = int(jremain())+int(jfourth())+int(jthird())+int(jsecond())+int(jfirst())
            if jTaxthereon1 > jTaxthereon2:
                jTaxthereon = jTaxthereon2
                return jTaxthereon
            else:
                jTaxthereon = jTaxthereon1
                return jTaxthereon

        def jtaxredution():
            jtaxredution = 0
            return jtaxredution

        def jTaxpayable():
            jTaxpayable = int(jTaxthereon())-int(jtaxredution())
            return jTaxpayable


        def SeparateTaxation():
            SeparateTaxation = int(hTaxpayable()) + int(wTaxpayable())
            return SeparateTaxation
        def JointAssessment():
            JointAssessment = int(jTaxpayable())
            return JointAssessment



        Label(window_01, text="").grid(row=0, column=0)
        Label(window_01, text="Husband").grid(row=0, column=1)
        Label(window_01, text="Wife").grid(row=0, column=2)
        Label(window_01, text="Joint").grid(row=0, column=3)

        Label(window_01, text="Monthly Income").grid(row=1, column=0)
        Label(window_01, text=hmi()).grid(row=1, column=1)
        Label(window_01, text=wmi()).grid(row=1, column=2)
        Label(window_01, text="-").grid(row=1, column=3)

        Label(window_01, text="Yearly  Income").grid(row=2, column=0)
        Label(window_01, text=hys).grid(row=2, column=1)
        Label(window_01, text=wys).grid(row=2, column=2)
        Label(window_01, text="-").grid(row=2, column=3)

        Label(window_01, text="Less : MPF contributions").grid(row=3, column=0)
        Label(window_01, text=round(hmpf(),2)).grid(row=3, column=1)
        Label(window_01, text=round(wmpf(),2)).grid(row=3, column=2)
        Label(window_01, text="-").grid(row=3, column=3)

        Label(window_01, text="Net Total Income").grid(row=4, column=0)
        Label(window_01, text=hni()).grid(row=4, column=1)
        Label(window_01, text=wni()).grid(row=4, column=2)
        Label(window_01, text=jni()).grid(row=4, column=3)

        Label(window_01, text="Less : Basicallowance").grid(row=5, column=0)
        Label(window_01, text=hBasicallowance()).grid(row=5, column=1)
        Label(window_01, text=wBasicallowance()).grid(row=5, column=2)
        Label(window_01, text=jBasicallowance()).grid(row=5, column=3)

        Label(window_01, text="Net Chargeable Income").grid(row=6, column=0)
        Label(window_01, text=hNetChargeableIncome()).grid(row=6, column=1)
        Label(window_01, text=wNetChargeableIncome()).grid(row=6, column=2)
        Label(window_01, text=jNetChargeableIncome()).grid(row=6, column=3)

        Label(window_01, text="On the first @2%").grid(row=7, column=0)
        Label(window_01, text=round(hfirst(),2)).grid(row=7, column=1)
        Label(window_01, text=round(wfirst(),2)).grid(row=7, column=2)
        Label(window_01, text=round(jfirst(),2)).grid(row=7, column=3)

        Label(window_01, text="On the second @6%").grid(row=8, column=0)
        Label(window_01, text=round(hsecond(),2)).grid(row=8, column=1)
        Label(window_01, text=round(wsecond(),2)).grid(row=8, column=2)
        Label(window_01, text=round(jsecond(),2)).grid(row=8, column=3)

        Label(window_01, text="On the third @10%").grid(row=9, column=0)
        Label(window_01, text=round(hthird(),2)).grid(row=9, column=1)
        Label(window_01, text=round(wthird(),2)).grid(row=9, column=2)
        Label(window_01, text=round(jthird(),2)).grid(row=9, column=3)

        Label(window_01, text="On the fourth @14%").grid(row=10, column=0)
        Label(window_01, text=round(hfourth(),2)).grid(row=10, column=1)
        Label(window_01, text=round(wfourth(),2)).grid(row=10, column=2)
        Label(window_01, text=round(jfourth(),2)).grid(row=10, column=3)

        Label(window_01, text="Remainder @17%").grid(row=11, column=0)
        Label(window_01, text=round(hremain(),2)).grid(row=11, column=1)
        Label(window_01, text=round(wremain(), 2)).grid(row=11, column=2)
        Label(window_01, text=round(jremain(), 2)).grid(row=11, column=3)

        Label(window_01, text="Tax thereon").grid(row=12, column=0)
        Label(window_01, text=round(hTaxthereon(),2)).grid(row=12, column=1)
        Label(window_01, text=round(wTaxthereon(),2)).grid(row=12, column=2)
        Label(window_01, text=round(jTaxthereon(),2)).grid(row=12, column=3)

        Label(window_01, text="Less : 75% tax reduction (NO use and = 0)").grid(row=13, column=0)
        Label(window_01, text=round(htaxredution(),2)).grid(row=13, column=1)
        Label(window_01, text=round(wtaxredution(),2)).grid(row=13, column=2)
        Label(window_01, text=round(jtaxredution(),2)).grid(row=13, column=3)

        Label(window_01, text="Tax payable").grid(row=14, column=0)
        Label(window_01, text=round(hTaxpayable(),2)).grid(row=14, column=1)
        Label(window_01, text=round(wTaxpayable(),2)).grid(row=14, column=2)
        Label(window_01, text=round(jTaxpayable(),2)).grid(row=14, column=3)

        Label(window_01, text="-").grid(row=15, column=0)
        Label(window_01, text="-").grid(row=15, column=1)
        Label(window_01, text="-").grid(row=15, column=2)
        Label(window_01, text="-").grid(row=15, column=3)

        Label(window_01, text="Separate Taxation ToTal Tax payable").grid(row=16, column=0)
        Label(window_01, text="-").grid(row=16, column=1)
        Label(window_01, text=round(SeparateTaxation(),2)).grid(row=16, column=2)
        Label(window_01, text="-").grid(row=16, column=3)

        Label(window_01, text="Joint Assessment ToTal Tax payable").grid(row=17, column=0)
        Label(window_01, text="-").grid(row=17, column=1)
        Label(window_01, text="-").grid(row=17, column=2)
        Label(window_01, text=round(JointAssessment(),2)).grid(row=17, column=3)

        Label(window_01, text="-").grid(row=18, column=0)
        Label(window_01, text="-").grid(row=18, column=1)
        Label(window_01, text="-").grid(row=18, column=2)
        Label(window_01, text="-").grid(row=18, column=3)

        Label(window_01, text="-").grid(row=19, column=0)
        Label(window_01, text="-").grid(row=19, column=1)
        Label(window_01, text="-").grid(row=19, column=2)
        Label(window_01, text="-").grid(row=19, column=3)


        def checkcase():
            if int(SeparateTaxation()) > int(JointAssessment()):
                Label(window_01, text="Your case, Joint Assessment is lower, you can use that.").grid(row=20, column=0)
                Label(window_01, text="-").grid(row=20, column=1)
                Label(window_01, text="-").grid(row=20, column=2)
                Label(window_01, text=round(JointAssessment(),2)).grid(row=20, column=3)
            else:
                if int(SeparateTaxation()) < int(JointAssessment()):
                    Label(window_01, text="Your case, Separate Taxation is lower, you can use that.").grid(row=20, column=0)
                    Label(window_01, text="-").grid(row=20, column=1)
                    Label(window_01, text=round(SeparateTaxation(),2)).grid(row=20, column=2)
                    Label(window_01, text="-").grid(row=20, column=3)
                else:
                    if int(SeparateTaxation()) == int(JointAssessment()):
                        Label(window_01, text="-").grid(row=20, column=0)
                        Label(window_01, text="-").grid(row=20, column=1)
                        Label(window_01, text="-").grid(row=20, column=2)
                        Label(window_01, text="-").grid(row=20, column=3)
                    else:
                        Label(window_01, text="-").grid(row=20, column=0)
                        Label(window_01, text="-").grid(row=20, column=1)
                        Label(window_01, text="-").grid(row=20, column=2)
                        Label(window_01, text="-").grid(row=20, column=3)


        checkcase()



    window_00 = Tk()
    window_00.geometry("540x540")
    centre_window(window_00)
    window_00.title('Tax')

    Label(window_00, text="Husband's Yearly Salary").grid(row=0, column=0)
    Label(window_00, text="Wife's Yearly Salary").grid(row=1, column=0)

    val_hys = Entry(window_00)
    val_wys = Entry(window_00)
    val_hys.grid(row=0, column=1)
    val_wys.grid(row=1, column=1)
    val_hys.insert(0, "0")
    val_wys.insert(0, "0")

    def error():
        ehys = val_hys.get()
        ewys = val_wys.get()
        if ehys.isdigit() and ewys.isdigit():
            error2()
        else:
            window_02 = Toplevel(window_00)
            window_02.geometry("540x540")
            centre_window(window_02)
            window_02.title('Tax')
            Label(window_02, text="Error").grid(row=0, column=0)
    def error2():
        ehys = val_hys.get()
        ewys = val_wys.get()
        if int(ehys) < 0 or int(ewys) < 0:
            window_02 = Toplevel(window_00)
            window_02.geometry("540x540")
            centre_window(window_02)
            window_02.title('Tax')
            Label(window_02, text="Error").grid(row=0, column=0)
        else: tax()



    Button(window_00, text='Submit', command=error).grid(row=2, column=1)

tax1()
mainloop()