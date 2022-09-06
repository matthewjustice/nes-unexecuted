"""
nes_unexecuted for Python 3
Finds code that isn't executed in a NES game,
or more specifically any ROM byte that isn't accessed.
"""
import sys

# constants
MAX_CPU_ADDR = 0xFFFF
CDL_VALUE_NOT_ACCESSED = 0


def main():
    """Program entry point"""
    # Check for command line args
    if len(sys.argv) < 3:
        print_help()
        return

    # Read command line arguments
    labels_file_name = sys.argv[1]
    cdl_file_name = sys.argv[2]

    show_addr = False
    if len(sys.argv) >= 4:
        # If any value was passed for argv[3]
        show_addr = True

    # Generate the labels dictionary from the labels file
    print(f'Processing label file {labels_file_name}')
    labels_dict = process_labels_file(labels_file_name)
    # print_labels(labels_dict)

    # Process the CDL file
    print(f'Processing CDL file {cdl_file_name}')
    unexecuted_dict = process_cdl_file(cdl_file_name, CDL_VALUE_NOT_ACCESSED, labels_dict)

    # Print the results
    print("Labels found where at least one byte wasn't executed...")
    print_unexecuted(unexecuted_dict, show_addr)

    return


def print_unexecuted(unexecuted_dict, show_addr):
    """Print the unexecuted labels and addresses"""
    for label in unexecuted_dict.keys():
        print(label)
        if show_addr:
            for addr in unexecuted_dict[label]:
                print(f'    {addr:04X}')


def find_closest_label(address, labels_dict):
    """
    Given an address, find the closest entry in the labels dictionary.
    The closest label is the label address less than or equal to the 
    specified address.
    """
    # start with an invalid last_address
    last_address = 0xFFFFFFFF

    # Loop through all the keys in labels_dict, storing each as
    # last_address as we go. The keys are in numberical order (ascending),
    # so once we find the label address that is greater than the specified
    # address, we've reached the NEXT label, so we return the label for
    # last address.
    for label_address in labels_dict.keys():
        if(label_address > address):
            break
        last_address = label_address

    return labels_dict[last_address]


def process_cdl_file(file_name, cdl_value, labels_dict):
    """
    Read a CDL file and return labels and addresses that
    match the specified cdl_value. The result is a dictionary
    where key="closest label" and value = "list of addresses"
    """
    result_dict = {}
    address = 0

    # Read all the bytes of the CDL file
    with open(file_name, 'rb') as cdl_file:
        cdl_bytes = cdl_file.read()

    # Read through all the bytes from the CDL file.
    # For each byte, if it matches the specified cdl_value,
    # find the label that its address is closest to, and 
    # store in in a dictionary that will be returned to the caller.
    for b in cdl_bytes:
        if b == cdl_value:
            # Found a match, Convert the byte address in CDL file
            # to a NES CPU address
            cpu_addr = address + 0x8000

            # Exit early if we go beyond the max address
            if cpu_addr > MAX_CPU_ADDR:
                break

            # Find the nearest (less than or equal) label for this address
            closest_label = find_closest_label(cpu_addr, labels_dict)

            # If we don't have this label as a key in the dictionary
            # already, add it as a key. Its value will initially be an
            # emtpy list (to hold all the matching addresses)
            if closest_label not in result_dict:
                result_dict[closest_label] = []

            # Add the address to the list of addresses for this label
            result_dict[closest_label].append(cpu_addr)

        # increment our loop counter that track the address of the CDL byte
        address = address + 1

    return result_dict


def process_labels_file(file_name):
    """Read a labels file and return a sorted dictionary of key=addr,val=label"""
    result_dict = {}
    with open(file_name, 'r') as labels_file:
        for line in labels_file:
            line_parts = line.split()
            addr = int(line_parts[1], 16)
            label_name = line_parts[2]
            result_dict[addr] = label_name

    return dict(sorted(result_dict.items()))


def print_labels(dict):
    """Print a labels dictionary"""
    for key, value in dict.items():
        print(f'{key:04X}={value}')


def print_help():
    """Tell the user how to use this tool"""
    print('Usage: nes_unexecuted.py labels.txt file.cdl [show-addr]')
    return


# Only execute main when running as the primary module
if __name__ == '__main__':
    main()
