import json

input_file = "yelp_academic_dataset_review.json"
output_file_prefix = "split_file_"
num_files = 20

with open(input_file, "r", encoding = "UTF8") as f:
    number_of_lines = sum(1 for _ in f)


lines_to_split = number_of_lines // num_files

with open(input_file, "r" , encoding="utf8") as f:
    for i in range(num_files):
        output_filename = f"{output_file_prefix}{i+1}.json"

        with open(output_filename, "w", encoding="utf8" ) as out_file:
            for j in range(lines_per_file):
                line = f.readline()
                if not line:
                    break  # Stop if file ends early
                out_file.write(line)

print("✅ JSON file successfully split into smaller parts!")

