

for line in open('../conf/uiDefaults.conf'):
	if len(line.strip()) == 0: continue
	if line.strip()[0] == '#': continue
	
	var = line.split('=')[0].strip().replace("'","")
	value = line.split('=')[-1].strip().replace("'","")
	
	print "\t<var>\n",
	print "\t\t<name>%s</name>\n" % (var),
	print "\t\t<title>%s</title>\n" % (var),
	print "\t\t<value>%s</value>\n" % (value),
	print "\t</var>\n",
	