#cd C:\Perl64\bin
#perl YOUR_PATH_HERE/get_ba_review_demo_no_wget.pl 21st-amendment-bitter-american
#perl C:/Users/nmfong/Dropbox/Research/ptf/scraping/get_ba_review_demo_no_wget.pl 21st-amendment-bitter-american

# 21st-amendment-bitter-american  21st Amendment Brewery  87      89      3.86	11.92   9.2     852     312     540     American Pale Ale (APA) 4.40

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
open(FILE, "C:/Users/nicole/test.html");
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
