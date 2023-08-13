import os

def calculate_average(file_path, value_column_index):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    values = [ float(line.strip().split('\t')[value_column_index]) for line in lines[1:]]
    average = sum(values) / len(values)

    print(values)
    return average

def main():
    input_directory = "../snakemake-workflow/benchmarks"  # Update this to the directory containing your benchmark files
    output_file = "averages.tsv"  # Update this to the desired output file name
    value_column_index = 3  # Update this to the index of the column containing the values

    averages = {}

    for filename in os.listdir(input_directory):
        if filename.endswith(".tsv"):
            file_path = os.path.join(input_directory, filename)
            file_name_without_extension = os.path.splitext(filename)[0]
            average = calculate_average(file_path, value_column_index)
            averages[file_name_without_extension] = average

    with open(output_file, 'w') as f:
        for file_name, average in sorted(averages.items()):
            f.write(f"{file_name}\t{average}\n")

if __name__ == "__main__":
    main()
