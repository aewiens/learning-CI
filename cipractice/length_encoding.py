# Copy of length-encoding script from the Hypothesis documentation's
# quick-start guide, just a dummy example for learning TravisCI
# https://hypothesis.readthedocs.io/en/latest/quickstart.html

# "Runs" of data: sequences in which the same data value occurs in many
# consecutive data elements

# Run-length encoding (RLE): a simple form of lossless data compression in
# which runs of data are stored as a single data value and count, rather than
# as the original run

# This is most useful on data sets that contain many such runs.


def encode(input_string):
	count = 1
	prev = ''
	lst = []

	for character in input_string:
		if character != prev:
			if prev:
				entry = (prev, count)
				lst.append(entry)

			count =1
			prev = character

		else:
			count += 1

	if not input_string:
		return []

	else:
		entry = (character, count)
		lst.append(entry)

	return lst


def decode(lst):
	q = ''
	for character, count in lst:
		q += character * count

	return q
