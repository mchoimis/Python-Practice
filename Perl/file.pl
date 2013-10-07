#perl file.pl 
  
open(FILE, "C:/Users/nicole/yelp-draught-horse-philadelphia.htm"); 
#You declared FILE as "C:/Users/nicole/yelp-draught-horse-philadelphia.htm"
# so you can just put <FILE> down here in the while statement
while ($line = <FILE>) { 
    if ($line =~ /\((\d{3})\)[ -]?(\d{3})[ -]?(\d{4})/) { 
        print "$1-$2-$3 is a phone number!\n"; 
    } 
} 
  
# we used "regular expression." BTW, what is a regular expression or regex?

close(FILE); 