import socket,time,sys
print("-"*30)
print("""
      PORT SCANNER v.1
Geliştirilme aşamasîndadır.
instagram: dridex_trojan_lockbit
""")
print("-"*30)
try:
    domain = input('domain giriniz: '.strip())
    port = int(input("port giriniz: ".strip()))
    print(time.asctime())
    serverip = socket.gethostbyname(domain)
except socket.gaierror:
    print("Geçerli bir adres giriniz")
except ValueError:
    print(f"Lütfen {port} bir sayı olarak giriniz")


print("-"*30)
q = 0 
while q < 1:
   q += 1
   try:
       s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
       socket.setdefaulttimeout(1)
       sonuc =   s.connect_ex((domain,port))
       if sonuc == 0:
           print('açîk girdiyiniz port: ', port)           
       if sonuc == 1:
           print('kapalı port: ', port)   
   except:
       print('bilinmeyen hata:2 oldu parametreleri doğru giriniz.')
   finally:
       print("işlem bitmiştir", sys.exit())
  
