# An irregular/uneven matrix, or ragged matrix, is a matrix that has a different number of elements in each row. Ragged matrices are not used in linear algebra, since standard matrix transformations cannot be performed on them, but they are useful as arrays in computing.
#Write a Python program to find the indices of all occurrences of target in the uneven matrix
def find_index(sample):
    output_list = []
    for r,row in enumerate(sample):
        for c,column in enumerate(row):
            if column == NumIndex:
                output_list.append([r,c])
    return output_list


NumIndex = 3
sample = [[1, 3, 2, 32, 19], 
          [19, 2, 48, 19], 
          [], [9, 35, 4], 
          [3, 19]]

#[[0, 4], [1, 0], [1, 3], [4, 1]]

print(find_index(sample))
