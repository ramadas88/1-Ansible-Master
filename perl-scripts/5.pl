use strict;
use warnings;


sub main {


 my @files  = ('/tmp/file1.txt', 
               '/tmp/file2/.txt', 
               '/tmp/nofile.txt',
               
  );
  

foreach my $file(@files) {
       if ( -f $file ) {
            print "Found files : $file\n"
            }
       else {
              print " File not found : $file\n"
             }
         

  } 

   


}

main();
