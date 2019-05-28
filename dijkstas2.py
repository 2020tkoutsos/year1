#djikstras algorithm is intended to find the shortest path regardless of how many nodes
#it stops the algorithm once the shortest path to the destination node has been determined

matrix = [[1,2,2], [1,2,2], [1,1,1]]
# matrix is created
def path_finder(matrix):
    # def path finder to locate shortest path way
    begin = (0,0)
    finish = (len(matrix)-1, len(matrix)-1)
    # hash was created to hold explored
    explored = {begin:0}
    # array was created to store unidentified values
    unidentified = [begin]
    # hash was created to hold lowest costs
    lowest_cost = {begin:0}
    # continue while routes are left unidentified
# variables are defined and ready to find the shortest path

    while unidentified:
        # take position from unidentified
        x,y = unidentified.pop(0)
        # check is value is at the finish
        if (x,y) == finish:
            # return lowest_cost and add begin value
            return lowest_cost[(x,y)] + matrix[0][0]
            # return lowest_cost[(x,y)] + matrix[0][0] + matrix[x][y]
        # hold parent node
        px,py = x,y
        # check all directions
        for x,y in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
            # check if directions are in bounds using the for loop iterating through the matrix
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]):
                # identify weight
                w = lowest_cost[(px,py)]+ matrix[x][y]

            if (x,y) not in explored or w < lowest_cost[(x,y)]:
                    # add to unidentified
                    unidentified.append((x,y))
                    # update explored
                    explored[(x,y)] = (px,py)
                    # update lowest_cost
                    lowest_cost[(x,y)] = w

                    print(w)

print(path_finder(matrix))

#sources
# Anish helped me so much he led me through how to do it, the logic, and walked me through how to write the code
#https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm
#https://www.youtube.com/watch?v=FSm1zybd0Tk
#https://stackoverflow.com/questions/23459390/subscriptable-error-when-trying-to-make-a-dictionary-in-to-a-list
