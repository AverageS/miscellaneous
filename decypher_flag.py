import os

data = b'Password>:TnZGFjo+k4/vaiYaQcTD8sr8vPSh\x00THAWEzhslIntbnBOIpaq\x00FNG8Hf4vzfxRlsrB/Ek/wpWX0xDdECEiKrAKqER/LTAJ3sJ7aco=:<Encrypted_flag'

password = "TnZGFjo+k4/vaiYaQcTD8sr8vPSh"
flag = "FNG8Hf4vzfxRlsrB/Ek/wpWX0xDdECEiKrAKqER/LTAJ3sJ7aco="
os.system(" echo %s | openssl enc -md md5 -d -base64 -aes-128-ctr -nopad -nosalt -k %s" % (flag,password ))
