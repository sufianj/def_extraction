#!/bin/bash

# Change to the directory where the CSV file is located
#dd /path/to/csv/file

# Read the CSV file using 'awk' to skip the header line
awk 'NR > 1' 28477_id+dir.csv > temp.csv
current_dir='0704'
# Loop through each line in the CSV file
while IFS=',' read -r id_without_addr_or_v dir; do
    # Check if current_dir is not equal to the value in the 'dir' column
    if [ "$current_dir" != "$dir" ]; then
        mkdir -p "$current_dir"
        mv -f "${current_dir}".* "${current_dir}"/
        currentma_dir="$dir"
    fi

    # Run the 'get_paper.sh' script with the value in the 'id_without_addr_or_v' column as an argument
    ./get_paper.sh "$id_without_addr_or_v"

done < temp.csv
mv -f "${current_dir}.*" "${current_dir}/"
cd ..
# Remove temporary file
rm temp.csv
