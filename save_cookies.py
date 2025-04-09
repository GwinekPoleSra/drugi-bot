import pickle

# Ciasteczka do zapisania
cookies = [
    {"name": "__Secure-1PAPISID", "value": "1fUgi_Bk0tRoHTD8/Ad5-OkB8_VwDVMExZ"},
    {"name": "__Secure-1PSID", "value": "g.a000vgibgOr1lTTlX8-HRBuqrjvgIzJOZjoNflz9GJAAMZLnuyp3bwSEsvcUmE7qyX77734qMQACgYKAZ0SARcSFQHGX2Mi6XE7fn_9YPMK75hOmwplHxoVAUF8yKomvqRT5mcEwLzaaVOAPFyE0076"},
    {"name": "__Secure-1PSIDCC", "value": "AKEyXzXLOx1iU9W0UF4tVdHtJZSyVSYWpU40jxzUHf-SADarw546Mn-aYeI-U2UDsB-gMik54A"},
    {"name": "__Secure-3PAPISID", "value": "1fUgi_Bk0tRoHTD8/Ad5-OkB8_VwDVMExZ"},
    {"name": "__Secure-3PSID", "value": "g.a000vgibgOr1lTTlX8-HRBuqrjvgIzJOZjoNflz9GJAAMZLnuyp3X-8LhckY_VmNrijXdxvJ-AACgYKAdYSARcSFQHGX2MiWm5Bg6uH0KjCGZKgui3q9BoVAUF8yKrYVgKRWydCh1VdTaKfi7sJ0076"},
    {"name": "__Secure-3PSIDCC", "value": "AKEyXzXWkeP__75zWNqgN1E4U_ykO9TUpg4-gKYtTWZj-DXotWCm8P8aK4ppM7daDcfDQyMeTw"},
    {"name": "1192_1277988", "value": "eyJlbWFpbCI6InBpc3RhbHVzemVsQGdtYWlsLmNvbSIsImVtYWlsU2V0UmVhZE9ubHkiOiIxIiwiaWRhcCI6IjEyNzc5ODgiLCJwYXllciI6Ikxpbmt2ZXJ0aXNlIn01"},
    {"name": "APISID", "value": "9ILx9bIevjUtYnc0/ABEMWg91UURdCCUGY"},
    {"name": "HSID", "value": "AzHMno3UeAntYesJL"},
    {"name": "laravel_session", "value": "h7y8GoaKKQyivdrYkAnoCLosJvWtP8suckAC0jby"},
    {"name": "remember_web_59ba36addc2b2f9401580f014c7f58ea4e30989d", "value": "eyJpdiI6ImEyaGpSOWZPa0ppWk0vd0c1b0hVK0E9PSIsInZhbHVlIjoidFk4T0VVSXppZ1dONUo0NktUb1VhNHBBYXEzQlpGcDNJQVRSUU1jVGJOamUwQlJPZnJZaGw3NUJaOGNHRjV3SUF4V1pBRDh0Y3gxV2VubFF2a2FlZU9PSjVqOVA3NjB5bFRZbFJHdnNiMDhOZ2JVcHJBWVNCbmtPd3l5cmhBNjF2NEs1dDZETFBFM3crMFRpa3dsaDRRZVEzb1NtMzJDKzU5aEE2Sm9qeHk4WnFkZUduZ2JBeE0rZnFaSm56RzcvRlFKVFl4Q2c5eWFCVXdWTEhkTktXS1lkUHd5b1VJdllYSmQ1N0FNR3JRTT0iLCJtYWMiOiJmNTZhM2I2OTI3ZTI2MzJiMmJkNjczZTUwZWIwNDUwOTVjNjUyNWVmZmU2OGExYzUyNmMwMDdmY2Y2NjRkMGY4IiwidGFnIjoiIn0%3D"},
    {"name": "SAPISID", "value": "1fUgi_Bk0tRoHTD8/Ad5-OkB8_VwDVMExZ"},
    {"name": "SID", "value": "g.a000vgibgOr1lTTlX8-HRBuqrjvgIzJOZjoNflz9GJAAMZLnuyp3jsi4gLtMBbt0qQAwjyoY1QACgYKARcSARcSFQHGX2MiItgIcbgyaL-PbAEclL3w4hoVAUF8yKpAN0wTPrhwQg-vSOTxn11G0076"},
    {"name": "SIDCC", "value": "AKEyXzUbGXFa0MjlnXIHyspGGPqqEwBZU4wB_22ZX98RH59yJpxko-Uw5WcmC0Nhv_5eyOKAxg"},
    {"name": "SSID", "value": "AcDAVzeSiW8C61tqO"},
    {"name": "XSRF-TOKEN", "value": "eyJpdiI6IkdUSng3K3JTZU0wbWdTUm04cDE2Qmc9PSIsInZhbHVlIjoiZFhPYmZXTGdoSmVnNXg4QkQ2KzJYR2dOUWk0RjE3VWZZeXZBUGpwQTh2cFB1TFZRQnppUUxnTVlJSjNsZDIxVlVqaWNORG1oMkEyZCtpS2lxK29qWEM3dTYzTTBsMlRZQTVzRnZwUlpFNm1qLzdjdEJqWnlKcDQyaWhpRkNoNkciLCJtYWMiOiI1MmUwYjIzMzI4OThiYjEzNGRiN2RjNDgzZTVkNTE4YzVjZGFiZDYwNDM5YWMyZWZjMDU5YmIzZThjNDg5N2Y2IiwidGFnIjoiIn0%3D"}
]

# Zapisz ciasteczka do pliku cookies.pkl
with open('cookies.pkl', 'wb') as f:
    pickle.dump(cookies, f)

print("Ciasteczka zapisane do pliku cookies.pkl")
