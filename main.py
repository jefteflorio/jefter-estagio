#!/usr/bin/python3

from Televisao import Televisao

tele_sansumg = Televisao(5,15, False)

tele_lg = Televisao(10, 20, False)

print("Canal SANSUMG: "+str(tele_sansumg.canal))
print("Canal LG: "+str(tele_lg.canal))
print("volume SANSUMG: "+str(tele_sansumg.volume))
print("volume LG: "+str(tele_lg.volume))
print("Mudo SANSUMG: "+str(tele_sansumg.mudo))
print("Mudo LG: "+str(tele_lg.mudo))