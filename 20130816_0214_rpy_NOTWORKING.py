from rpy import *

# START OF METHOD 1
hclust = r("""
    a <- read.table("cpOfSimMatrix.txt")
    mydist <- dist(1-a)
    hclust(mydist)
""")
r("rm(a)") # Ends with an error if you leave anything in memory
# END OF METHOD 1

# START OF METHOD 2
set_default_mode(NO_CONVERSION)
a = r.read_table("cpOfSimMatrix.txt")
mydist = r.dist(r["-"](1,a)) # Note the trick for '1-a' here
set_default_mode(BASIC_CONVERSION)
hclust = r.hclust(mydist) # Converts R object to Python dict
# END OF METHOD 2

# START OF METHOD 3 (here's one I created earlier)
r.load(".RData")
hclust = r('myHclust')
# END OF METHOD 3
