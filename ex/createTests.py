users = ['gabi', 'joao', 'marcos']

f = open('testsSaulo.py')
t = f.read()
f.close()

for user in users:
	r = t.replace('saulo', user)
	r = r.replace('Saulo', user.title())

	fo = open('tests' + user.title() + '.py', 'wb')
	fo.write(r)
	fo.close()