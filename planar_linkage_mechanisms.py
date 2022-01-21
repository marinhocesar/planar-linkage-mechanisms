from topology_generation import generate_topologies

while True:
    print("\nLinkage Mechanism Topology Generation")
    print("Type 'q' to quit.")
    max = input("Maximum size of kinematic chain: ")

    if max == 'q':
        break
    
    try:
        max = int(max)
        if (max % 2 != 0) or (max < 6):
            print("Your input should be an even number greater or equal to 6.")
        else:
            generate_topologies(max)
    except ValueError:
        print("Please, enter a valid integer.")

    