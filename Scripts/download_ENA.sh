#! /bin/bash

# Check if input and output files are provided
if [[ $# -lt 2 ]]; then
	echo "Usage: bash download_ENA.sh <input_file> <threads> <output_file>"
	exit 1
fi

# Store input file variable
input_file=$1 #"ena-file-download-PRJEB62687.txt"

# Store user defined thread count (max of 12)
threads=$2

# Store output file variable
#output_file=$2 #""

URL_LIST=$(awk -F' ' '{print $3}' $input_file)

echo $URL_LIST | xargs -n 1 -P $threads wget -q -nc
