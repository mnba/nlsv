#!/usr/bin/env python3
"""
convert_nlsv_to_tsv.py - converts NLSV* test to TSV* text file format.

Usage: 
  python3 ./convert_nlsv_to_tsv.py <input.nlsv> <output.tsv>
 
* NLSV New Line Separated Values file format
In NLSV the text file holds each value on a separate line, with empty line
indicating the end of each record, as a separator between adjacent records.
* [TSV, tab separated values format](https://en.wikipedia.org/wiki/Tab-separated_values)
 See README.md for details.

For testing run: 
  python3 ./convert_nlsv_to_tsv.py ./test_input.nlsv ./output.tsv
"""
import sys 

def convert_nlsv_to_tsv(input_filename, output_filename):
  """
  Converts a file in NLSV format to TSV format.
  Args:
    input_filename: The name of the input file in NLSV format.
    output_filename: The name of the output file in TSV format.
  """
  try:
    with open(input_filename, 'r') as input_file, open(output_filename, 'w') as output_file:
      records = convert_nlsv_to_data(input_file)
      write_tsv(records, output_file)
      print(f"Done, written {len(records)} records.")
  except FileNotFoundError:
    print(f"Error: Input file '{input_filename}' not found.")
  except PermissionError:
    print(f"Error: Permission denied to access file '{input_filename}'.")
  '''except IOError as e:
    print(f"IO Error: {e}")
  except Exception as e:
    print(f"An unexpected error occurred: {e}")'''


def convert_nlsv_to_data(input_file):
  """
  Converts the contents of an NLSV file to a 2D array of records.
  Args:
    input_file: A file object opened for reading in text mode.
  Returns:
    A 2D array where each element of the outer array represents a record,
    and the elements of the inner array are the values in that record.
  """
  records = []
  current_record = []
  record_length = None

  for lno,line in enumerate(input_file):
    line = line.strip()
    if line: # ordinary value encountered
      # Add the current NLSvalue into the current record
      current_record.append(line)

    else: # End of record reached, indicated by empty line.
      #==if not line: 
      # Processing the end of record: 
      if not current_record:
        continue # skip 
      if record_length is None: # the case when we read the very first record 
        record_length = len(current_record)
      elif len(current_record) != record_length: 
        print(f"Warning: Inconsistent record length at line {lno}, record: {current_record}. Continuing conversion.")
      # Add the new record 
      records.append(current_record)
      # prepare for next record
      current_record = []

  # Append the last record if file does not end with a blank line
  if current_record: # we got some values in record
    if record_length is None: # at EOF but still the very first record
      record_length = len(current_record)
    if len(current_record) != record_length:
      print(f"Warning: Inconsistent record length at the end of file, record: {current_record}. Finishing conversion.")
    records.append(current_record)

  return records


def write_tsv(records, output_file):
  """
  Writes the list of records into a file in TSV format.
  Args:
    records: A 2D array where each element of the outer array represents a record,
             and the elements of the inner array are the values of each record.
    output_file: A file object opened for writing in text mode.
  """
  for record in records:
    output_file.write("\t".join(record) + "\n")
  # done 


# Test the functionality
def test():
  input_filename = "test_input.nlsv"
  output_filename = "output.tsv"
  convert_nlsv_to_tsv(input_filename, output_filename)

sUsage = "Usage: convert_nlsv_to_tsv.py <input.nlsv> <output.tsv>"
def main():
  args = sys.argv
  if len(args)<=2 or args[1]=="--help":
    print(sUsage)
    return 0
  input_filename  = args[1]
  output_filename = args[2]
  convert_nlsv_to_tsv(input_filename, output_filename)

if __name__ == "__main__":
  #test() #tested:works OK 
  main()  
