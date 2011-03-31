
import time
import os

rd = {}
# lumikki.env
rd['MYPREFIX'] = '/home/sauna/usr/'
# conf/lighttpd.conf
rd['var.log_root'] = '"/tmp"'
rd['var.server_root'] = '"/home/sauna/lumikki_devel/webroot"'
rd['var.state_dir'] = '"/tmp"'
rd['var.home_dir'] = '"/tmp"'
rd['var.conf_dir'] = '"/home/sauna/lumikki_devel/conf"'
rd['server.port'] = '8000'

# conf/conf.d/cgi.conf
rd['setenv.add-environment'] = '("PYTHONPATH" => "/usr/lib/python2.6/site-packages")'
rd['cgi.assign'] = '( ".cgi" => "/usr/bin/python2.6" )'

def makeBackup(filename):

	inFile = open(filename,'r')
	outFile = open('/tmp/%s.%lf' % (os.path.basename(filename), 
					time.time()), 'w')

	inFile_list = []
	for line in inFile:
		outFile.write('%s' % (line))
		inFile_list.append(line)

	inFile.close()

	return inFile_list

def replaceLines(outFn, lines):

	outFile = open(outFn,'w')
	for line in lines:
		key = line.split('=')[0].strip()
		if rd.has_key(key):
			print "modified to: %s=%s" % (key,rd[key])
			outFile.write('%s=%s\n'  % (key,rd[key]))
			continue
		outFile.write('%s' % (line))

lines = makeBackup('../lumikki.env')
replaceLines('../lumikki.env', lines)

lines = makeBackup('../conf/lighttpd.conf')
replaceLines('../conf/lighttpd.conf', lines)

lines = makeBackup('../conf/conf.d/cgi.conf')
replaceLines('../conf/conf.d/cgi.conf', lines)
