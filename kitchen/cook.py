import sys
import os
import base64
length = len(sys.argv)
if length <= 2:
    print('what do u gonna do?')
    print('usage: ./cook <file1> <file2> ...')
c = open('mom_secret_recipe', 'r').read().strip()
if c != 'CjIgcG91bmRzIHNraW5sZXNzLCBib25lbGVzcyBjaGlja2VuIGJyZWFzdCBoYWx2ZXMKCjIgdGVhc3Bvb25zIHNhbHQKCsK9IGN1cCBjb29raW5nIG9pbAoKMeKAicK9IGN1cHMgY2hvcHBlZCBvbmlvbgoKMSB0YWJsZXNwb29uIG1pbmNlZCBnYXJsaWMKCjHigInCvSB0ZWFzcG9vbnMgbWluY2VkIGZyZXNoIGdpbmdlciByb290CgoxIHRhYmxlc3Bvb24gY3VycnkgcG93ZGVyCgoxIHRlYXNwb29uIGdyb3VuZCBjdW1pbgoKMSB0ZWFzcG9vbiBncm91bmQgdHVybWVyaWMKCjEgdGVhc3Bvb24gZ3JvdW5kIGNvcmlhbmRlcgoKMSB0ZWFzcG9vbiBjYXllbm5lIHBlcHBlcgoKMSB0YWJsZXNwb29uIHdhdGVyCgoxICgxNSBvdW5jZSkgY2FuIGNydXNoZWQgdG9tYXRvZXMKCjEgY3VwIHBsYWluIHlvZ3VydAoKMSB0YWJsZXNwb29uIGNob3BwZWQgZnJlc2ggY2lsYW50cm8KCjEgdGVhc3Bvb24gc2FsdAoKwr0gY3VwIHdhdGVyCgoxIHRlYXNwb29uIGdhcmFtIG1hc2FsYQoKMSB0YWJsZXNwb29uIGNob3BwZWQgZnJlc2ggY2lsYW50cm8KCjEgdGFibGVzcG9vbiBmcmVzaCBsZW1vbiBqdWljZQoKU3RlcCAxClNwcmlua2xlIHRoZSBjaGlja2VuIGJyZWFzdHMgd2l0aCAyIHRlYXNwb29ucyBzYWx0LgoKU3RlcCAyCkhlYXQgdGhlIG9pbCBpbiBhIGxhcmdlIHNraWxsZXQgb3ZlciBoaWdoIGhlYXQ7IHBhcnRpYWxseSBjb29rIHRoZSBjaGlja2VuIGluIHRoZSBob3Qgb2lsIGluIGJhdGNoZXMgdW50aWwgY29tcGxldGVseSBicm93bmVkLiBUcmFuc2ZlciB0aGUgYnJvd25lZCBjaGlja2VuIGJyZWFzdHMgdG8gYSBwbGF0ZSBhbmQgc2V0IGFzaWRlLgoKU3RlcCAzClJlZHVjZSB0aGUgaGVhdCB1bmRlciB0aGUgc2tpbGxldCB0byBtZWRpdW0taGlnaDsgYWRkIHRoZSBvbmlvbiwgZ2FybGljLCBhbmQgZ2luZ2VyIHRvIHRoZSBvaWwgcmVtYWluaW5nIGluIHRoZSBza2lsbGV0IGFuZCBjb29rIGFuZCBzdGlyIHVudGlsIHRoZSBvbmlvbiB0dXJucyB0cmFuc2x1Y2VudCwgYWJvdXQgOCBtaW51dGVzLiBTdGlyIHRoZSBjdXJyeSBwb3dkZXIsIGN1bWluLCB0dXJtZXJpYywgY29yaWFuZGVyLCBjYXllbm5lLCBhbmQgMSB0YWJsZXNwb29uIG9mIHdhdGVyIGludG8gdGhlIG9uaW9uIG1peHR1cmU7IGFsbG93IHRvIGhlYXQgdG9nZXRoZXIgZm9yIGFib3V0IDEgbWludXRlIHdoaWxlIHN0aXJyaW5nLiBNaXggdGhlIHRvbWF0b2VzLCB5b2d1cnQsIDEgdGFibGVzcG9vbiBjaG9wcGVkIGNpbGFudHJvLCBhbmQgMSB0ZWFzcG9vbiBzYWx0IGludG8gdGhlIG1peHR1cmUuIFJldHVybiB0aGUgY2hpY2tlbiBicmVhc3QgdG8gdGhlIHNraWxsZXQgYWxvbmcgd2l0aCBhbnkganVpY2VzIG9uIHRoZSBwbGF0ZS4gUG91ciAxLzIgY3VwIHdhdGVyIGludG8gdGhlIG1peHR1cmU7IGJyaW5nIHRvIGEgYm9pbCwgdHVybmluZyB0aGUgY2hpY2tlbiB0byBjb2F0IHdpdGggdGhlIHNhdWNlLiBTcHJpbmtsZSB0aGUgZ2FyYW0gbWFzYWxhIGFuZCAxIHRhYmxlc3Bvb24gY2lsYW50cm8gb3ZlciB0aGUgY2hpY2tlbi4KClN0ZXAgNApDb3ZlciB0aGUgc2tpbGxldCBhbmQgc2ltbWVyIHVudGlsIHRoZSBjaGlja2VuIGJyZWFzdHMgYXJlIG5vIGxvbmdlciBwaW5rIGluIHRoZSBjZW50ZXIgYW5kIHRoZSBqdWljZXMgcnVuIGNsZWFyLCBhYm91dCAyMCBtaW51dGVzLiBBbiBpbnN0YW50LXJlYWQgdGhlcm1vbWV0ZXIgaW5zZXJ0ZWQgaW50byB0aGUgY2VudGVyIHNob3VsZCByZWFkIGF0IGxlYXN0IDE2NSBkZWdyZWVzIEYgKDc0IGRlZ3JlZXMgQykuIFNwcmlua2xlIHdpdGggbGVtb24ganVpY2UgdG8gc2VydmUuCg==':
    print('looks like you haven\'t got curry recipe')
    sys.exit(0)
if length == 3:
    if 'spice' in sys.argv and 'meat' in sys.argv:
        f = open('spice', 'r')
        spice_content = f.read().strip()
        f.close()
        f = open('meat', 'r')
        meat_content = f.read().strip()
        f.close()
        #print(spice_content, meat_content)
        content=(spice_content+meat_content).encode()
        content=base64.b64encode(content)
        content=content.decode()
        #print(content)
        f = open('curry', 'w')
        f.write(content)
        f.close()
        os.remove('spice')
        os.remove('meat')
    if 'curry' in sys.argv and '.rice' in sys.argv:
        f = open('curry', 'r')
        curry_content = f.read().strip()
        f.close()
        f = open('.rice', 'r')
        rice_content = f.read().strip()
        f.close()
        #print(curry_content, rice_content)
        content=(curry_content).encode()
        content=base64.b64encode(content)
        content=content.decode()
        #print(content)
        if rice_content.count('Ri#_}csie73@>G=3)o0d!') != 81922:
            f = open('shi_bai_curry_rice', 'w')
            f.write('U_$0_Shi_b@1')
            f.close()
        elif len(rice_content)!=(21*81922):
            f = open('shi_bai_curry_rice', 'w')
            f.write('U_$0_Shi_b@1')
            f.close()
        elif content == 'Vm10YVlWUnRVWGxXYTJSVVlrZDRWVmxVUm5kWGJGSldWbXQwVDFadFVucFdNVkpUWVd4YVdWVnVaRnBoYTI5M1dWUkdTbVZHWkhWVmJHaHBVbXhXTkZZeU1UUlNiVlp6VjI1V2FWSXpRbTlaVkVaaFRrWldObE51VG10TldFSjZWbGQwYjFZeVNsaGhSMmhZWW0wNU0xUXhSVGxRVVQwOVZtMXdTMkl4UmxaT1NHaFFVMGRvY1ZSV1VuTlNWbkJIWVVWMFlXSkhkRFpXTW5NeFZHeGFWVlp0ZEZaVFIwMDFWVVpGT1ZCUlBUMVVWV014WTBkSmQwNVhXazVWTVVwdFdXMXdRMDFGYzNwV2JsWm9WbnBzTVZkRVNUVk5WMG96VUZRd1BXUnVXbTlaVjBaQldWZEdhRkZZVW1aa1ZqaHJXVmhzWmxaV09EaE5NVGxxWWpOSmVGRlhOV3ROTTBrdlVIbzRMMDR3YUd4WU1VSTFTekpuZDJKc09IaEtSamhyWkVoS2RtSXlPWFppTWpWSQ==':
            
            f = open('curry_rice', 'w')
            c = '\x11\x1b\x16\x10,\x02\x08s?g"f3\x08\x00\x17\x08\x17#4?\x085>#\x08;.\x08dn\x03\x1c\x00f!*'
            fl = ''.join(chr(ord(i)^87) for i in c)
            f.write(fl)
            f.close()
        else:
            f = open('shi_bai_curry_rice', 'w')
            f.write('U_$0_Shi_b@1')
            f.close()
        os.remove('curry')
        os.remove('.rice')
if length == 4:
    if 'spice' in sys.argv and 'meat' in sys.argv and '.rice' in sys.argv:
        f = open('ga_li_ban_fan', 'w')
        f.write('0H!_B@o_gE_Ma7_hA73_U~')
        f.close()
        os.remove('spice')
        os.remove('meat')
        os.remove('rice')
