import qrcode

# inserir  em "texto" o valor a ser convertido em QRcode
texto = ''

meu_qrcode = qrcode.make(texto)

meu_qrcode.save('meu_qrcode.png', quantily=100)

