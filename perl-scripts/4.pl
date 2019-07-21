use strict;
use warnings;


sub main {


 my @files  = ('/tmp/file1.txt', 
               '/tmp/file2/.txt', 
               '/tmp/nofile.txt',
               
  );
  

foreach my $file(@files) {
        print "$file\n";

  } 

   


}

main();
