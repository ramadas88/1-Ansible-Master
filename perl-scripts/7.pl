use strict;
use warnings;


  $|=1;

sub main{
   my $file = "/tmp/file-1.txt";
   open(INPUT , $file) or die(" INput file $file not found. \n");
  
   while(my $line = <INPUT>) {
   
    if($line =~ /egg/) {
     print " $line"; 
    }
  }
 
    close(INPUT);



}

main();
