import random

CODE = 'ASKLDFJALKSDJFLKAS9009sdafu0asdf\
asodf909-423-0fsdi0a0isd==as=-234&*%%&N)H&HND)SN)FN)DNF))SD)0sf003cnq3n98c89q245890245-2334155445asdf\
asjkdfi834fu803fv890u3cu90cf3u9034fuj354u9cv3u89cv90uc3fgcf590yY87utg7utg7u90FG09U90GVU9JU94F\
8ASDFUASDUFSU9DU90SDU9FSVSDFV9S9FSDFUDU-0FA0SVUQC0U4WVI--+_+_+(+-0P4Q3V=*/*+/-/-/-9SF9SAF6S46DF846344FSG49\
U9ASDOFU9SD99udf90gu90dfgu9asu9ujU9DFGUJVE40TUJ-0AVJ0-0guj9bj0tj04uj00UU)U)0uu540u53-5#%*)*_)^_^*$%$$^&\
*(^%^*T&ISDGASDT*(T&(gibdafgustf9&*(T&(&TT&#T&dfy8hstf89t79R&*^R*@#^*$T&gicusdhfy9rhet23t79y80fbnixcvbnx bn& t78 &*\
U*(G&*@#^(DFBJKCVO:XCZV"<>}|}{DFT&*@T*@!H~UH*U(JHIOPNIDFJ(PSDFU)#-*/-diOH*DFHIOVCNLJLDFHSY)()*(#$*)@)(\
89*DSFU*()SDFU(DVJPOCXJIL:V_I$%*_$#(_(_#@%(_@#$*)YHDFO:VC:VNKLXCLESDULF#PW$_(@#_)_#R*$#Y@%*(BUJlJKCJISDFJI\
*&)*(R()#()U$#O@HNILSDVNKLFVBJO:FBJIPJKVZXGU&EIOR*(#)*($()#*)@Y(OFOSDUOFOUISDFOIUJ,asf,k,szwaek,9wsx4wsx34o0\
ow38xmkm w38493trcfgyjhrgjiofui90ui904rfgio04fgwjhi0jhio-qwe4ve4gvj89-4fgj89-wegj9-4gvq4vq4vj9-4v4k9jw54vjk9\
ASDFHIO0WEFJHI9090238978954809054UJMFXDFHNFUHNXDFRGJHIORU,UI3Ujuu$%w%^i##$jkjk%$kc%ek$6K56  5676MK67%\
7UE8R9TG90WGOIXCVUJW05T3445846648*-/*/*-SDAF/-G/ASDFGS/*/*34GV54/*35/*-CF4F54CER4fgj89-wKJK,9L-/9L0/-690*-\
XS*12ZX*3ZX423*42XQ-WAX*-W4V5-V E5-N8-K/*,.-=./.]]=\.]-0/-9[.-FSDUIFOASPDFPOASDPFO[SADGK[5BU9-549T34\
DVJPOCXJIL:V_I$%*_$#(_(_#@%(_@#$*)YHDFO:JPOCXJIL:V_I$%*_$#(_(_#@%(_@#VC:VNKLX4fgj89-w4fgj89-w4fgj89-wCLESDULF#PW$_\
rcfgyjh2XQ-WAX*-W4V5-V E5-N8-K/*,.-=./.]]=\.]-0/-9[.-FSDUIFOK/*,.-=./.]]=\.]-0/-9[.-FSDAr-9[.-FSDUIFOASPDFPOASgjio\
DVJPOCXJIL:V_I$%*_$#(rcfgyj2XQ-WAX*-W4V5-V E5-N(_@#$*)YHDU(DVJPOCXJIL:V_I$%*_$#(_(_#@%(_@#$*)YHFO:VC:VNKLXCLESDULF#PW$_\
SDT*(T&(gibdafgustf9&*(T&(&TT&#T&XCZV"<>}|}{DFT&*@T*@!Hjkdfi834fu803fv890u3cu90cf3u9034fuj35~UH*dfy8hstf89t79R&\
2XQ-WAX*-W4V5-V E5-N8-K/*,.-=./.]]=\.]-0/-9[-&(&TT&#T&dfy8hstf89t79R&*^R*@#^*$T&gicusdh9[.-FSDUIFOASPDFPOAS.-FSDUIFOA\
'

def get_code(code: str) -> str:
    CODE_2 = ''
    i = 0
    while i < len(code) - 1:
        if i % 3 == 0:
            CODE_2 += code[i]
        i += 1
    
    """CODE_3 = ''

    i2 = 0
    while i2 < len(code) - 1:
        if i2 % 7 == 0:
            CODE_3 += code[i2]
        i += 1

    CODE_4 = ''

    i3 = 0
    while i3 < len(code) - 1:
        if i3 % 5 == 0:
            CODE_4 += code[i3]
        i += 1"""

    FINAL_CODE = 'happystay' + 'CODE_4' + 'CODE_3' + CODE_2
    
    return FINAL_CODE

def get_random_code(x: int) -> str:
    code = 'XCE'
    for n in range(x):
        code += str(random.random())
    return code