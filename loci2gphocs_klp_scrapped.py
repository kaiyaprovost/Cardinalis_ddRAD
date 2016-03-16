# pyrad .loci to gphocs format conversion
#
# This is a very simple conversion because the formats are very similar.
#
# Usage: python loci2gphocs -f <my_input.loci> [-o <my_output>] [-v True]
#
# Isaac Overcast
# March 21, 2015

## import libraries
import sys, os
import argparse

#parser = argparse.ArgumentParser(prog='PROG')
#parser.add_argument("-f", dest="locifile", required=True, help="name of the loci input file being converted")
#parser.add_argument("-o", dest="outfile", default='output.gphocs', help="gphocs output file name")
#parser.add_argument("-v", dest="verbose", help="Set verbosity. Dump tons of info to the screen", default=False)
#options = parser.parse_args()

#infilename = options.locifile
#outfilename = '%s' %(options.outfile)

#infile = open( infilename )
#outfile = open( outfilename, 'w' )

infile = open(r"C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard.loci")
outfile = open("C:/Users/Kaiya/Documents/Columbia/Thesis/THESIS DATA/cardcard_klp.gphocs","w")

## parse the loci
## Each set of reads at a locus is appended with a |,
## so after this call 'loci' will contain an array
## of sets of each read per locus.
loci = infile.read().strip().split("//")

## only examine loci w/ at least 1 outgroup sample
## and at least two inds from each focal populations
#if(options.verbose): print "Got nloci:", len(loci)

# Print the header, the number of loci in this file
print >>outfile, len(loci)-1

# iterate through each locus, print out the header for each locus:
# <locus_name> <n_samples> <locus_length>
# Then print the data for each sample in this format:
# <individual_name> <sequence>
for i, loc in enumerate(loci):
    # The enumerate is going to return is a [] as the last element
    # so if this is the last locus then we're done.
    if i == len(loci)-1:
        break

    # Get the length of the sequence read at this locus so we can print the
    # header. Basically you get the first line, then you take the 2nd element
    first_sequence = loc.strip().split("\n")[0]
    print("first",first_sequence)
    sequence_length = len(first_sequence.strip().split()[1])
    print("length",sequence_length)
    #if(options.verbose): print "Length of locus", i, "=", sequence_length

    # Separate out each sequence within the loc block. 'sequences'
    # will now be a list strings containing name/sequence pairs.
    # This is confusing, the [:-1] thing at the end means "all but the last 
    # line, since this is not a read, but is the line that contains info 
    # about positions of snps.
    sequences = loc.strip().split("\n")[:-1]

    # Print out the header for this locus
    print >>outfile, 'locus'+ str(i), len(sequences), str( sequence_length )

    # Iterate through each sequence read at this locus and write it to the file.
    for sequence in sequences:
        # Clean up the sequence data to make gphocs happy. Only accepts UPPER
        # case chars for bases, and only accepts 'N' for missing data. Also,
        # the .loci format prepends a '>' on to the individual names, so we have
        # to clean this up which is what the [1:] is doing.
        sequence = sequence[1:].upper().replace( '-', 'N' )

        print >>outfile, sequence

