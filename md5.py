import hashlib

salt='localsalt'
needed="7fa68589ef35bced981aeca08c4f126b"
i=0

print "Looking for a match with %s..." % needed
while (i < 1000000):
	m = hashlib.md5()
	password = salt+str(i)
	m.update(password)
	hash = m.hexdigest()
	if hash == needed:
		print "    MATCH FOUND!"
		print "    The passcode is: %s" % str(i)
		break
	i += 1
