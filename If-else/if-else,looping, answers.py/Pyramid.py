#Your task is to write a program which reads the number of blocks the builders have, and outputs the height of the pyramid that can be built using these blocks.

#Note: the height is measured by the number of fully completed layers – if the builders don't have a sufficient number of blocks and cannot complete the next layer, they finish their work immediately.


blocks = int(input("Enter the number of blocks: "))

pyramid_height = 0
blocks_required = 1

while blocks:
    if blocks >= blocks_required:
        pyramid_height += 1
        blocks = blocks - blocks_required
        blocks_required += 1
    else:
        print("Not enough blocks for the next layer")
        break
print("The height of the pyramid:", pyramid_height)

