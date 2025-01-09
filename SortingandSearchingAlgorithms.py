## Sorting and Searching Algorithms


##Purpose: Sort an array using the Selection sort algorithm.
##Best Case: O(n^2)
def selectionSort(userlist):

    iterationCount = 0

    print(f"The original list: {userlist}")

    n = len(userlist)

    for bottom in range(n-1):

        mp = bottom

        for i in range(bottom+1, n):

            if userlist[i] < userlist[mp]:

                mp = i

                iterationCount += 1

        userlist[bottom], userlist[mp] = userlist[mp], userlist[bottom]

    print(f"The list at {iterationCount} iterations using Selection Sort: {userlist}")

    return userlist

##Purpose: Sort an array using the Bubble sort algorithm.
##Best Case: O(n^2)
def bubbleSort(userlist):

    n = len(userlist)

    iterationCount = 0

    print(f"The original list: {userlist}")

    for i in range(n - 1):

        swapped = False

        for j in range(n - i - 1):

            if userlist[j] > userlist[j + 1]:  ##Compare adjacent elements

                userlist[j], userlist[j + 1] = userlist[j + 1], userlist[j] 

                swapped = True

                iterationCount += 1

        if not swapped:  ##Exit early if no swaps in the current pass

            break

    print(f"The list at {iterationCount} iterations using Bubble Sort: {userlist}")

    return userlist  ##Return the sorted list

##Purpose: Sort an array using the insertion sort algorithm.
##Best Case: O(n^2)
def insertionSort(userlist):

    n = len(userlist)

    iterationCount = 0

    print(f"The original list: {userlist}")    

    for i in range(1, n):

        currentElement = userlist[i]  # Correct current element for insertion

        j = i - 1


        # Shift elements to the right if greater than currentElement
        while j >= 0 and userlist[j] > currentElement:

            userlist[j + 1] = userlist[j]

            j -= 1

            iterationCount += 1  

        userlist[j + 1] = currentElement  # Insert current element at correct position
        
    print(f"The list at {iterationCount} iterations using Insertion Sort: {userlist}")  # Optional: Show progress

    return userlist

##Purpose: Sort an array using the Merge Sort algorithm.
##Best Case: O(n log n)
def mergeSort(userlist):
    if len(userlist) > 1:
        mid = len(userlist) // 2  # Find the middle of the array
        left_half = userlist[:mid]  # Split into left half
        right_half = userlist[mid:]  # Split into right half

        mergeSort(left_half)  # Recursively sort the left half
        mergeSort(right_half)  # Recursively sort the right half

        i = j = k = 0
        # Merge the sorted halves
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                userlist[k] = left_half[i]
                i += 1
            else:
                userlist[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            userlist[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            userlist[k] = right_half[j]
            j += 1
            k += 1
    return userlist

##Purpose: Sort an array using the Quick Sort algorithm.
##Best Case: O(n log n)
def quickSort(userlist):
    if len(userlist) <= 1:

        return userlist  # Base case: arrays with 1 or 0 elements are sorted

    else:

        pivot = userlist[len(userlist) // 2]  # Choose the middle element as the pivot

        less_than_pivot = [x for x in userlist if x < pivot]

        equal_to_pivot = [x for x in userlist if x == pivot]

        greater_than_pivot = [x for x in userlist if x > pivot]

        # Recursively sort the partitions

        return quickSort(less_than_pivot) + equal_to_pivot + quickSort(greater_than_pivot)


## Purpose: Search the user's list for an integer.
## Best Case: O(1), Worst Case: O(n)    
def linearSearch(userlist):

    userElement = int(input("Enter an integer you would like to find in the list: "))

    print()

    n = len(userlist)
    
    for i in range(n):

        if userlist[i] == userElement:

            print(f"{userElement} was found at position: {i}")

            return i  # Return the index as soon as the element is found
    
    # This will only be executed if the loop completes without finding the element

    print(f"{userElement} was not found in the list.")

    return -1  # Return -1 to indicate the element was not found




## Purpose: Search the user's list for an integer.
## Best Case: O(1), Worst Case: O(log n)
def binarySearch(userlist):

    userElement = int(input("Enter an integer you would like to find in the list: "))

    print()
    
    iElement = 0  # Start index

    jElement = len(userlist) - 1  # End index
    
    while iElement <= jElement:

        mElement = (iElement + jElement) // 2
        
        if userlist[mElement] == userElement:

            print(f"{userElement} was found at position: {mElement}")

            return mElement  # Return the index of the found element

        elif userlist[mElement] < userElement:

            iElement = mElement + 1  # Search in the right half

        else:

            jElement = mElement - 1  # Search in the left half
    
    # This will only be executed if the while loop exits without finding the element
    print(f"{userElement} was not found in the list.")

    return -1  # Return -1 to indicate the element was not found





## Purpose: Determines both the min and max values of a list
def minMaxAlgorithm(userlist):

    ##Assigns currentmin and currentmax with the first element of the user list
    currentmin = currentmax = userlist[0]
    
    ##Assigned 'n' for the len of the user list
    n = len(userlist)
    
    for i in range(1, n):

        ## Compares the userlist[i] with currentmin
        if userlist[i] < currentmin:

            currentmin = userlist[i]

        ## Compares the userlist[i] with currentmax
        if userlist[i] > currentmax:

            currentmax = userlist[i]            

    return currentmin, currentmax





## Main function
def main():
    while True:
        try:
            # Input list
            userinput = input("Enter a list of integers separated by spaces:\n")
            userlist = [int(x) for x in userinput.split()]

            # Sorting
            sortingMethod = int(input("Which sorting method would you like to use? \n"
                                       "1: Selection Sort\n"
                                       "2: Bubble Sort\n"
                                       "3: Insertion Sort\n"
                                       "4: Merge Sort\n"
                                       "5: Quick Sort\n"))

            if sortingMethod == 1:
                userlist = selectionSort(userlist)
            elif sortingMethod == 2:
                userlist = bubbleSort(userlist)
            elif sortingMethod == 3:
                userlist = insertionSort(userlist)
            elif sortingMethod == 4:
                userlist = mergeSort(userlist)
                print(f"The list after Merge Sort: {userlist}")
            elif sortingMethod == 5:
                userlist = quickSort(userlist)
                print(f"The list after Quick Sort: {userlist}")
            else:
                print("Invalid input. Please enter a number between 1 and 5.")
                continue

            break  # Exit loop after valid sorting

        except ValueError:
            print("Invalid input. Please enter numbers for the list and a valid option for sorting.")

    # Searching
    while True:
        searchingAlgorithm = input("Would you like to search for an integer?\nYes or No\n").strip().lower()
        if searchingAlgorithm == 'yes':
            while True:
                try:
                    selectAlgorithm = int(input("Which algorithm would you like to use:\n1: Linear Search\n2: Binary Search.\n"))
                    if selectAlgorithm == 1:
                        print(linearSearch(userlist))
                        break
                    elif selectAlgorithm == 2:
                        print(binarySearch(userlist))
                        break
                    else:
                        print("Invalid input. Please enter '1' or '2'.")
                except ValueError:
                    print("Invalid input. Please enter '1' or '2'.")
            break  # Exit search loop
        elif searchingAlgorithm == 'no':
            print("No value needed to find.")
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    # Min/Max Calculation
    while True:
        minmax = input("Would you like to calculate the min and max value?\nYes or No:\n").strip().lower()
        if minmax == 'yes':
            print("Minimum value and Maximum value:", minMaxAlgorithm(userlist))
            break
        elif minmax == 'no':
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

# Program Loop
    while True:
        tryAgain = input("Would you like to use the program again? (Yes or No)\n").strip().lower()
        if tryAgain == 'yes':
            main()
        else:
            print("Thank you for using my program!")
            break
           
main()
