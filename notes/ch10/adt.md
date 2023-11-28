# Abstract data types
> Abstract data types are specialized array types that are modified by pointers in particular ways.
> ADTs are fundamental to modern data structures, data management, and the implementation of relevant algorithms
## Definitions
Abstract data types (ADTs) have **3 types**:
- **Stack**
    - Follows Last-in-first-out **(LIFO)** principle. First item to be added to the stack is the last to be removed.
    - `basePointer` at `stack[0]`; `topPointer` at `stack[LENGTH(stack) - 1]`.
    - Upon `push` operation, `topPointer++`; upon `pop` operation, `topPointer--`.
    - *Used by embedded system internal operations to traverse through a tree of function scope and callbacks.*
- **Queue**
    - Follows First-in-last-out **(FILO)** principle.
    - Uses `enqueue` and `dequeue` operations.
    - `frontPointer` at `queue[0]`; `endPointer` at `queue[LENGTH(queue) - 1]`.
    - When `enqueue`, `endPointer++`; when `dequeue`, `frontPointer--`.
    - Queue consists of only one item when `frontPointer == endPointer`.
- **LinkedList**
    - Each element contains a "data" value and a "goto (aka. node)" value.
    - For an array implementing Linked List operations `linklist OF INTEGER`, data value is at `linklist[x][0]`; node value a `linklist[x][1]`. Where `x` is the index of pair in linked list. 
## Implementation
### Stack operations
```
DECLARE stackArray : ARRAY[0:<endIndex>] OF <type>
DECLARE basePointer, topPointer, index, stackfull: INTEGER
DECLARE item : <type>
basePointer <- 0
topPointer <- 0
stackfull <- <endIndex>

// Populating stackArray with push operations
FOR index <- basePointer TO stackfull:
    OUTPUT "Array value at pos ", index, ": "
    INPUT stackArray[index]
    topPointer <- topPointer + 1
NEXT index
OUTPUT "Perform how many pop operations? > "
INPUT opNum
// Performing 2 pop operations
FOR i <- 1 TO opNum
    IF topPointer < basePointer
        THEN
            OUTPUT "Can't pop, stack empty"
        ELSE
            OUTPUT "Popped item ", stackArray[topPointer]
            topPointer <- topPointer - 1
    ENDIF
NEXT i
```
### Queue operations
```
DECLARE queueArray : ARRAY[0:<endIndex>] OF <type>
DECLARE frontPointer, endPointer, index : INTEGER
DECLARE item : <type>
frontPointer <- 0
endPointer <- 0
// Given that queueArray has already been populated (ENQUEUE function)
endPointer <- LENGTH(queueArray) - 1
// DEQUEUE
FOR 
```
