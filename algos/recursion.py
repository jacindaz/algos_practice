CHAR_FOR_INT = '0123456789abcdef'

def to_string(num, base):
    if num < base:
        return CHAR_FOR_INT[num]

    return to_string(num // base, base) + CHAR_FOR_INT[num % base]


# Rules
#   => 3 towers
#   => transfer all disks from 1 tower to another
#   => can only move 1 disk as a time
#   => larger disk can never be placed on a smaller disk

# base case: when have 1 disk left, move to final destination
# what state to change?
# recursive call


# Here is a high-level outline of how to move a tower from the starting pole, to the goal pole, using an intermediate pole:

# Move a tower of height-1 to an intermediate pole, using the final pole.
# Move the remaining disk to the final pole.
# Move the tower of height-1 from the intermediate pole to the final pole using the original pole.


def move_disk(disk, from_pole, to_pole):
    print('moving disk {} from {} to {}'.format(disk, from_pole, to_pole))

def move_tower(height, from_pole, to_pole, with_pole):
    if height >= 1:
        move_tower(height-1, from_pole, with_pole, to_pole)
        move_disk(height, from_pole, to_pole)
        move_tower(height-1, with_pole, to_pole, from_pole)


print(move_tower(3, 'A', 'B', 'C'))
