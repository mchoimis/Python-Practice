#perl regex.pl Nathan nathan nate jonathan nathaniel 555-1212 
  
foreach $arg (@ARGV) { 
    if ($arg =~ /nathan/) { 
        print "The word $arg has nathan in it!\n"; 
    } 
} 
  
print "\nNow let's make it case-insensitive:\n"; 
foreach $arg (@ARGV) { 
    if ($arg =~ /nathan/i) { 
        print "The word $arg has nathan in it!\n"; 
    } 
} 
  
# if you put i, it means you take both lower and upper case letters equally

print "\nNow let's look for phone numbers:\n"; 
foreach $arg (@ARGV) { 
    if ($arg =~ /\d{3}-\d{4}/) { 
        print "$arg is a phone number!\n"; 
    } 
} 