#perl subexp.pl "555-1234 blah (215) 555-1212 blah (215)-555-4321" 
  

foreach $arg (@ARGV) { 
    if ($arg =~ /\d{3}-\d{4}/) { 
        print "$arg is a phone number!\n"; 
    } 
} 
  
print "\nNow let's pull out the phone numbers:\n"; 
foreach $arg (@ARGV) { 
    if ($arg =~ /(\d{3}-\d{4})/) { 
        print "$1 is the first phone number!\n"; 
    } 
} 
  
print "\nNow let's pull out ALL the phone numbers:\n"; 
foreach $arg (@ARGV) { 
    while ($arg =~ /(\d{3}-\d{4})/g) { 
        print "$1 is a phone number!\n"; 
    } 
} 
  
print "\nLet's require the area code:\n"; 
foreach $arg (@ARGV) { 
    if ($arg =~ /\((\d{3})\) (\d{3})-(\d{4})/) { 
        print "$1 is the first part\n"; 
        print "$2 is the second part\n"; 
        print "$3 is the third part\n"; 
    } 
} 
  
print "\nLet's make dashes optional:\n"; 
foreach $arg (@ARGV) { 
    while ($arg =~ /\((\d{3})\)[ -]?(\d{3})[ -]?(\d{4})/g) { 
        print "$1-$2-$3 is a full phone number\n"; 
    } 
} 
## g is for global, makes it keep going, [] square brackers make things optional, ? means you can have either one of the things