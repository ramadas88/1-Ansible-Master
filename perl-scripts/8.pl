use strict;
use warnings;


  $|=1;

sub main{
   my $input = "/tmp/file-1.txt";
   open(INPUT , $input) or die(" INput file $input not found. \n");
   
   my $output = 'output.txt';
   open(OUTPUT, '>'.$output) or die "Cant Create $output File\n";

    
   while(my $line = <INPUT>) {
   
       if($line =~ /\begg\b/) {
          $line =~ s/egg/diangrous/ig;
          print OUTPUT  $line; 
    }
  }
 
    close(INPUT);
    close(OUTPUT);
    close(OUTPUT);


}

main();
