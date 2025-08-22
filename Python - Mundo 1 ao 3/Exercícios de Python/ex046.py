from time import sleep
from emoji import emojize
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emojize(':party_popper:\033[1;97mFELIZ ANO NOVO!!\033[m:partying_face:'))
