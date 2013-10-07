use strict;
use warnings;

use LWP::Simple;
use LWP::UserAgent;
use HTTP::Request;
use HTTP::Response;


##open file to store links
open my $file1,">>", ("extracted_links.txt");
select($file1); 

##starting URL
my @urls = 'http://stackoverflow.com/';

my $browser = LWP::UserAgent->new('IE 6');
$browser->timeout(10);
my %visited;
my $url_count = 0;


while (@urls) 
{
     my $url = shift @urls;
     if (exists $visited{$url}) ##check if URL already exists
     {
         next;
     }
     else
     {
         $url_count++;
     }         

     my $request = HTTP::Request->new(GET => $url);
     my $response = $browser->request($request);

     if ($response->is_error()) 
     {
         printf "%s\n", $response->status_line;
     }
     else
     {
         my $contents = $response->content();
         $visited{$url} = 1;
         @lines = split(/\n/,$contents);
         foreach $line(@lines)
         {
             $line =~ m@(((http\:\/\/)|(www\.))([a-z]|[A-Z]|[0-9]|[/.]|[~]|[-_]|[()])*[^'">])@g;
             print "$1\n";  
             push @urls, $$line[2];
         }

         sleep 60;

         if ($visited{$url} == 100)
         {
            last;
         }
    }
}

close $file1;