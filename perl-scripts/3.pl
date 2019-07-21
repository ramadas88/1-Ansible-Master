use strict;
use warnings;


sub main {
    my $file = "/tmp/logo.png";
    
    if(-f $file) {
       print "Found File : $file\n";
    }
    else {
     print "File not found $file\n"; 
   }

}

main ();



