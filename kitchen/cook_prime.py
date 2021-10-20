import sys
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﳂ=True
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ瀞=False
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𥹵=print
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞی=len
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌=open
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𘟓=chr
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𞡘=ord
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚=sys.argv
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐫗=sys.exit
import os
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ=os.remove
import base64
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺍ=base64.b64encode
import subprocess
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ騯=subprocess.PIPE
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𦃥=subprocess.Popen
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𗪢=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𦃥("git branch",shell=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﳂ,stdout=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ騯,stderr=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ騯).communicate()[0]
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𗪢=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𗪢.decode()
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𗪢=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𗪢.split('\n')
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺉ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ瀞
for b in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𗪢:
 if '* kitchen' in b:
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺉ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﳂ
if not 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺉ:
 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𥹵('seems that you aren\'t on a right branch')
 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐫗(0)
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐩶=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞی(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚)
if 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐩶<=2:
 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𥹵('what do u gonna do?')
 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𥹵('usage: ./cook <file1> <file2> ...')
𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺷ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('mom_secret_recipe','r').read().strip()
if 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺷ!='CjIgcG91bmRzIHNraW5sZXNzLCBib25lbGVzcyBjaGlja2VuIGJyZWFzdCBoYWx2ZXMKCjIgdGVhc3Bvb25zIHNhbHQKCsK9IGN1cCBjb29raW5nIG9pbAoKMeKAicK9IGN1cHMgY2hvcHBlZCBvbmlvbgoKMSB0YWJsZXNwb29uIG1pbmNlZCBnYXJsaWMKCjHigInCvSB0ZWFzcG9vbnMgbWluY2VkIGZyZXNoIGdpbmdlciByb290CgoxIHRhYmxlc3Bvb24gY3VycnkgcG93ZGVyCgoxIHRlYXNwb29uIGdyb3VuZCBjdW1pbgoKMSB0ZWFzcG9vbiBncm91bmQgdHVybWVyaWMKCjEgdGVhc3Bvb24gZ3JvdW5kIGNvcmlhbmRlcgoKMSB0ZWFzcG9vbiBjYXllbm5lIHBlcHBlcgoKMSB0YWJsZXNwb29uIHdhdGVyCgoxICgxNSBvdW5jZSkgY2FuIGNydXNoZWQgdG9tYXRvZXMKCjEgY3VwIHBsYWluIHlvZ3VydAoKMSB0YWJsZXNwb29uIGNob3BwZWQgZnJlc2ggY2lsYW50cm8KCjEgdGVhc3Bvb24gc2FsdAoKwr0gY3VwIHdhdGVyCgoxIHRlYXNwb29uIGdhcmFtIG1hc2FsYQoKMSB0YWJsZXNwb29uIGNob3BwZWQgZnJlc2ggY2lsYW50cm8KCjEgdGFibGVzcG9vbiBmcmVzaCBsZW1vbiBqdWljZQoKU3RlcCAxClNwcmlua2xlIHRoZSBjaGlja2VuIGJyZWFzdHMgd2l0aCAyIHRlYXNwb29ucyBzYWx0LgoKU3RlcCAyCkhlYXQgdGhlIG9pbCBpbiBhIGxhcmdlIHNraWxsZXQgb3ZlciBoaWdoIGhlYXQ7IHBhcnRpYWxseSBjb29rIHRoZSBjaGlja2VuIGluIHRoZSBob3Qgb2lsIGluIGJhdGNoZXMgdW50aWwgY29tcGxldGVseSBicm93bmVkLiBUcmFuc2ZlciB0aGUgYnJvd25lZCBjaGlja2VuIGJyZWFzdHMgdG8gYSBwbGF0ZSBhbmQgc2V0IGFzaWRlLgoKU3RlcCAzClJlZHVjZSB0aGUgaGVhdCB1bmRlciB0aGUgc2tpbGxldCB0byBtZWRpdW0taGlnaDsgYWRkIHRoZSBvbmlvbiwgZ2FybGljLCBhbmQgZ2luZ2VyIHRvIHRoZSBvaWwgcmVtYWluaW5nIGluIHRoZSBza2lsbGV0IGFuZCBjb29rIGFuZCBzdGlyIHVudGlsIHRoZSBvbmlvbiB0dXJucyB0cmFuc2x1Y2VudCwgYWJvdXQgOCBtaW51dGVzLiBTdGlyIHRoZSBjdXJyeSBwb3dkZXIsIGN1bWluLCB0dXJtZXJpYywgY29yaWFuZGVyLCBjYXllbm5lLCBhbmQgMSB0YWJsZXNwb29uIG9mIHdhdGVyIGludG8gdGhlIG9uaW9uIG1peHR1cmU7IGFsbG93IHRvIGhlYXQgdG9nZXRoZXIgZm9yIGFib3V0IDEgbWludXRlIHdoaWxlIHN0aXJyaW5nLiBNaXggdGhlIHRvbWF0b2VzLCB5b2d1cnQsIDEgdGFibGVzcG9vbiBjaG9wcGVkIGNpbGFudHJvLCBhbmQgMSB0ZWFzcG9vbiBzYWx0IGludG8gdGhlIG1peHR1cmUuIFJldHVybiB0aGUgY2hpY2tlbiBicmVhc3QgdG8gdGhlIHNraWxsZXQgYWxvbmcgd2l0aCBhbnkganVpY2VzIG9uIHRoZSBwbGF0ZS4gUG91ciAxLzIgY3VwIHdhdGVyIGludG8gdGhlIG1peHR1cmU7IGJyaW5nIHRvIGEgYm9pbCwgdHVybmluZyB0aGUgY2hpY2tlbiB0byBjb2F0IHdpdGggdGhlIHNhdWNlLiBTcHJpbmtsZSB0aGUgZ2FyYW0gbWFzYWxhIGFuZCAxIHRhYmxlc3Bvb24gY2lsYW50cm8gb3ZlciB0aGUgY2hpY2tlbi4KClN0ZXAgNApDb3ZlciB0aGUgc2tpbGxldCBhbmQgc2ltbWVyIHVudGlsIHRoZSBjaGlja2VuIGJyZWFzdHMgYXJlIG5vIGxvbmdlciBwaW5rIGluIHRoZSBjZW50ZXIgYW5kIHRoZSBqdWljZXMgcnVuIGNsZWFyLCBhYm91dCAyMCBtaW51dGVzLiBBbiBpbnN0YW50LXJlYWQgdGhlcm1vbWV0ZXIgaW5zZXJ0ZWQgaW50byB0aGUgY2VudGVyIHNob3VsZCByZWFkIGF0IGxlYXN0IDE2NSBkZWdyZWVzIEYgKDc0IGRlZ3JlZXMgQykuIFNwcmlua2xlIHdpdGggbGVtb24ganVpY2UgdG8gc2VydmUuCg==':
 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𥹵('looks like you haven\'t got curry recipe')
 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐫗(0)
if 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐩶==3:
 if 'spice' in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚 and 'meat' in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚:
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('spice','r')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𢇫=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.read().strip()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('meat','r')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺜ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.read().strip()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴=(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𢇫+𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺜ).encode()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺍ(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴)
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴.decode()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('curry','w')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.write(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴)
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ('spice')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ('meat')
 if 'curry' in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚 and '.rice' in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚:
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('curry','r')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞف=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.read().strip()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('.rice','r')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐪅=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.read().strip()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴=(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞف).encode()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺍ(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴)
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴.decode()
  if 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐪅.count('Ri#_}csie73@>G=3)o0d!')!=81922:
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('shi_bai_curry_rice','w')
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.write('U_$0_Shi_b@1')
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  elif 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞی(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐪅)!=(21*81922):
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('shi_bai_curry_rice','w')
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.write('U_$0_Shi_b@1')
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  elif 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ뵴=='Vm10YVlWUnRVWGxXYTJSVVlrZDRWVmxVUm5kWGJGSldWbXQwVDFadFVucFdNVkpUWVd4YVdWVnVaRnBoYTI5M1dWUkdTbVZHWkhWVmJHaHBVbXhXTkZZeU1UUlNiVlp6VjI1V2FWSXpRbTlaVkVaaFRrWldObE51VG10TldFSjZWbGQwYjFZeVNsaGhSMmhZWW0wNU0xUXhSVGxRVVQwOVZtMXdTMkl4UmxaT1NHaFFVMGRvY1ZSV1VuTlNWbkJIWVVWMFlXSkhkRFpXTW5NeFZHeGFWVlp0ZEZaVFIwMDFWVVpGT1ZCUlBUMVVWV014WTBkSmQwNVhXazVWTVVwdFdXMXdRMDFGYzNwV2JsWm9WbnBzTVZkRVNUVk5WMG96VUZRd1BXUnVXbTlaVjBaQldWZEdhRkZZVW1aa1ZqaHJXVmhzWmxaV09EaE5NVGxxWWpOSmVGRlhOV3ROTTBrdlVIbzRMMDR3YUd4WU1VSTFTekpuZDJKc09IaEtSamhyWkVoS2RtSXlPWFppTWpWSQ==':
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('curry_rice','w')
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺷ='\x11\x1b\x16\x10,\x02\x08s?g"f3\x08\x00\x17\x08\x17#4?\x085>#\x08;.\x08dn\x03\x1c\x00f!*'
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𪢾=''.join(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𘟓(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𞡘(i)^87)for i in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﺷ)
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.write(𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𪢾)
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  else:
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('shi_bai_curry_rice','w')
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.write('U_$0_Shi_b@1')
   𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ('curry')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ('.rice')
if 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐩶==4:
 if 'spice' in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚 and 'meat' in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚 and '.rice' in 𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𩼚:
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ=𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞ𐼌('ga_li_ban_fan','w')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.write('0H!_B@o_gE_Ma7_hA73_U~')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞᐎ.close()
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ('spice')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ('meat')
  𐰾𫬑𐩲ﵿ𪅐𧻼𣧹挮ﱞﶆ('rice')
# Created by pyminifier (https://github.com/liftoff/pyminifier)
