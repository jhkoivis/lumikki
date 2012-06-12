
fn = 'lena.png'

f = open(fn, "rb")
data = f.read()

out = open('index.html', 'w')

out.write('<html><body>')
out.write('<img alt="Embedded Image" src="data:image/png;base64,')
out.write(data.encode("base64"))
out.write('">')
out.write('</html></body>')