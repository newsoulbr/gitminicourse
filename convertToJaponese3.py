#! /usr/bin/env python
import sys

#Insert your first name and last name here
name="Integritas";
lastName="Rock";

if len(sys.argv) > 1:
    name=sys.argv[1].lower();
else:
    name=name.lower();
    
if len(sys.argv) > 2:
    lastName=sys.argv[2].lower();
else:
    lastName=lastName.lower();

japaneseLetter = {
    "a":"ka",
	"b":"tu",
	"c":"mi",
	"d":"te",
	"e":"ku",
	"f":"lu",
	"g":"ji",
	"h":"ri",
	"i":"ki",
	"j":"zu",
	"k":"me",
	"l":"ta",
	"m":"rin",
	"n":"to",
	"o":"mo",
	"p":"no",
	"q":"ke",
	"r":"shi",
	"s":"ari",
	"t":"shi",
	"u":"do",
	"v":"ru",
	"x":"na",
	"w":"mei",
	"y":"fu",
	"z":"ra",
}

japoneseName="";
japoneseLastName="";

for namechar in name:
	japoneseName+=japaneseLetter.get(namechar);

for namechar in lastName:
	japoneseLastName+=japaneseLetter.get(namechar);

#That is the final way to print the converted name	
if len(japoneseLastName) > 0 :
	print japoneseName.capitalize()+" "+japoneseLastName.capitalize();
else:
	print japoneseName.capitalize();
