def scan_scheduling(current, requests, direction, max_track):
    # Create a copy of the requests list
    queue = list(requests)
    # Sort the queue in ascending order
    queue.sort()
    # Initialize the total seek time
    total_seek_time = 0
    # Initialize the current head position
    current_head = current

    if direction == 'left':
        # Move towards the leftmost track
        while current_head >= 0:
            if current_head in queue:
                # Calculate the seek time for the current request
                seek_time = abs(current_head - current)
                # Update the total seek time
                total_seek_time += seek_time
                # Remove the processed request from the queue
                queue.remove(current_head)
            current_head -= 1

        # Move towards the rightmost track
        current_head = 0
        while current_head <= max_track:
            if current_head in queue:
                # Calculate the seek time for the current request
                seek_time = abs(current_head - current)
                # Update the total seek time
                total_seek_time += seek_time
                # Remove the processed request from the queue
                queue.remove(current_head)
            current_head += 1

    elif direction == 'right':
        # Move towards the rightmost track
        while current_head <= max_track:
            if current_head in queue:
                # Calculate the seek time for the current request
                seek_time = abs(current_head - current)
                # Update the total seek time
                total_seek_time += seek_time
                # Remove the processed request from the queue
                queue.remove(current_head)
            current_head += 1

        # Move towards the leftmost track
        current_head = max_track
        while current_head >= 0:
            if current_head in queue:
                # Calculate the seek time for the current request
                seek_time = abs(current_head - current)
                # Update the total seek time
                total_seek_time += seek_time
                # Remove the processed request from the queue
                queue.remove(current_head)
            current_head -= 1

    return total_seek_time


# Example usage
current_position = 50
request_queue = [82, 170, 43, 140, 24, 16, 190]
direction = 'left'
max_track = 199
seek_time = scan_scheduling(current_position, request_queue, direction, max_track)
print("Total seek time:", seek_time)
