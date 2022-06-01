###################################################
# OLD WAY
###################################################
fileku = open('pesan.txt', 'w')
fileku.write('Ayo Belajar Pythoic\n')
fileku.close()
###################################################
# PYTHONIC WAY
###################################################
with open('pesan.txt', 'w') as fileku:
    fileku.write('Ayo Belajar Pythoic\n')
    