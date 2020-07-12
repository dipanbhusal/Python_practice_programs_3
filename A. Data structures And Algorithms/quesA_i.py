#i. Tower of hanoi
def tower_of_hanoi(n, start_node, target_node, aux_node):
    if n == 1:
        print(f'Move disk 1 from {start_node} to {target_node}')
        return 
    tower_of_hanoi(n-1, start_node, aux_node, target_node)
    print(f'Move disk {n} from {start_node} to {target_node}')
    tower_of_hanoi(n-1,aux_node, target_node, start_node)


n  = 4
tower_of_hanoi(n, 'A', 'E', 'C')
