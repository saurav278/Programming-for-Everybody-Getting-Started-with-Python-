hrs = raw_input("Enter Hours:")
h = float(hrs)
rph = float(raw_input("Enter rate per hour"))

if hrs > 40:
    print 40*rph + (h-40)*rph*1.5
else:
    print h*rph
