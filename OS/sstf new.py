def shortest_seek_time(current, requests):
    # Create a copy of the requests list
    queue = list(requests)
    # Initialize the total seek time
    total_seek_time = 0
    # Initialize the current head position
    current_head = current

    while queue:
        # Find the request with the shortest seek time
        shortest_seek = min(queue, key=lambda x: abs(x - current_head))
        # Calculate the seek time for the current request
        seek_time = abs(shortest_seek - current_head)
        # Update the total seek time
        total_seek_time += seek_time
        # Update the current head position
        current_head = shortest_seek
        # Remove the processed request from the queue
        queue.remove(shortest_seek)

    return total_seek_time


# Example usage
current_position = 50
request_queue = [45,21,67,90,4,50,89,52,61,52,87,25]
seek_time = shortest_seek_time(current_position, request_queue)
print("Total seek time:", seek_time)
