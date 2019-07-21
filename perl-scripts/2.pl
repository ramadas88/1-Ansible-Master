use strict;
use warnings;

use LWP::Simple;

sub main{
   print "Downloading.............\n";
   print get("https://caveofprogramming.com/");
   print "Finished \n";
}


main();

