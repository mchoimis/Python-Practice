#cd C:\Perl64\bin
#perl YOUR_PATH_HERE/get_ba_review_demo.pl 21st-amendment-bitter-american
#perl C:/Users/nmfong/Documents/get_ba_review_demo.pl 21st-amendment-bitter-american

# 21st-amendment-bitter-american  21st Amendment Brewery  87      89      3.86	11.92   9.2     852     312     540     American Pale Ale (APA) 4.40

# the call to wget specifies two files (insert your own location on your computer): one is a logfile to track your requests, and the other (temp.html) is the file where the request is saved
# if you do not set the system path to wget, you can locate the program and put the full path to wget here as I have done in the uncommented version of this first call to wget:

system("\"C:/Program Files (x86)/GnuWin32/bin/wget\" -U \"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22\" --no-check-certificate -a C:/Users/nicole/wgetlog.txt -O C:/Users/nicole/temp.html http://www.google.com/search?q=$ARGV[0]+site:beeradvocate.com");

#system("wget -U \"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22\" --no-check-certificate -a C:/Users/nmfong/Downloads/PTF/wgetlog.txt -O C:/Users/nmfong/Downloads/PTF/temp.html http://www.google.com/search?q=$ARGV[0]+site:beeradvocate.com");

$starturls = 0;
$baurl = null;

# here you need to specify the location from the file where you saved the Google search
open(LIST, "C:/Users/nicole/temp.html"); # opening three files that are already saved
while ($next = <LIST>) {

if ($next =~ /href="http:\/\/beeradvocate.com\/beer\/profile\/(.*?)"/) {
	$baurl = $1;
#	print "$baurl\n";
# this call will open the results of the Google search, and download the ratings web page
	system("wget -U \"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.22 (KHTML, like Gecko) Chrome/25.0.1364.152 Safari/537.22\" -a C:/Users/nicole/wgetlog.txt -O C:/Users/nicole/temp2.html http://beeradvocate.com/beer/profile/$baurl");
}
}
close(LIST);

$score = "null";
$bros = "null";
$avg = "null";
$pdev = "null";
$psdev = "null";
$nrating = "null";
$nreview = "null";
$nhad = "null";
$brewerid = "null";
$brewer = "null";
$styleid = "null";
$style = "null";
$abv = "null";

$on = 0;

# one more location to specify: reopen the ratings web page
open(FILE, "C:/Users/nicole/temp2.html");
while ($line = <FILE>) {

if ($on eq 0 and $line =~ /BA SCORE/) { $on = 1; }
if ($on eq 1 and $line =~ /THE BROS/) { $on = 2; }
if ($on eq 2 and $line =~ /<b>Brewed by:<\/b>/) { $on = 3; }
if ($on eq 3 and $line =~ /<b>Style | ABV<\/b>/) { $on = 4; }

if ($on eq 1) {
	if ($line =~ /<br><span class="BAscore_big">(.*)<\/span>/) {$score = $1; }
	if ($line =~ /<br>-<br>(.*) Ratings<\/td>/) {$nrating = $1; }
	}
if ($on eq 2) {
	if ($line =~ /<br><span class="BAscore_big">(.*)<\/span>/) {$bros = $1; }
	if ($line =~ /rAvg: (.*)<!--<br>psDev: (.*)%-->/) {$avg = $1; $psdev = $2; }
	if ($line =~ /<br>pDev: (.*)%/) {$pdev = $1; }
	if ($line =~ /<br>Reviews: (.*)<br>Hads: (.*)<br>/) {$nreview = $1; $nhad = $2; }
	}
if ($on eq 3) {
	if ($line =~ /<a href="\/beer\/profile\/(.*?)"><b>(.*)<\/b>/) {$brewerid = $1; $brewer = $2; }
#	if ($line =~ /<b>(.*)<\/b>/) {$brewer = $1; }
	}
if ($on eq 4) {
#	if ($line =~ /<a href="\/beer\/style\/(.*?)"><b>(.*)<\/b><\/a> | &nbsp;(.*)% <a href="\/articles/) {$styleid = $1; $style = $2; $abv = $3; }
	if ($line =~ /<a href="\/beer\/style\/(.*?)"><b>(.*)<\/b><\/a>(.*);(.*)% <a href="\/articles/) {$styleid = $1; $style = $2; $abv = $4; }
	if ($line =~ /<br><br>/) {$on = 0; }
	}
}
close(FILE);
print "$ARGV[0]\t$brewer\t$score\t$bros\t$avg\t$pdev\t$psdev\t$nrating\t$nreview\t$nhad\t$style\t$abv\n";
