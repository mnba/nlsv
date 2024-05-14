# NLSV file format: New Line Separated Values 

Here proposed a file format called **NLSV**, *New Line Separated Values*. 
It is equivalent to CSV, and TSV file formats.
In NLSV the text file holds each value on a separate line, with empty line
indicating the end of each record, as a separator between adjacent records.

* [CSV, comma separated values format](https://en.wikipedia.org/wiki/Comma-separated_values)
* [TSV, tab separated values format](https://en.wikipedia.org/wiki/Tab-separated_values)

This is an example NLSV data, here first record represents the _header record_
equivalent of CSV/TSV. Such header record can be displayed in Spreadsheet application
(MS Excel, LibreCalc) as a highlighted header or a sticky header. 

```nlsv
Name 
Date
Count 
Action 

Alex F
Nov 23, 2020
0 subscribers
SUBSCRIBE

Eugene Skorn
May 22, 2019
0 subscribers
SUBSCRIBE
```

This Python script converts NLSV test to TSV text file format. 
The script (main function) accepts input and output filenames, converts NLSV data
into TSV, and writes resulted converted data into the output text file. 
The script also processes the possible IO errors.

Converter function at first step identifies the length of record for data which is
given at input as a database table, i.e. how many values keeps one individual record.
After that it reads the input, and fills in every record with corresponding value.
Converter checks consistensy of counts of values in all records, signaling about
error if that count is wrong for some record, while trying to continue the convertion.

