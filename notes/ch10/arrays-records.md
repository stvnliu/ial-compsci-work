# Records and arrays
Common datatypes contain (For pseudocode):
REAL, CHAR, INTEGER, STRING, ARRAY[T], BOOLEAN
## Composite data types with Records
Records are composite data types formed by the inclusion of several related items that may be of different data types. (Aggregate data?)
In pseudocode, a record data type definition takes the following form:
```
TYPE
<TypeName>
    DECLARE <ident> : <type>
    DECLARE <ident> : <type>
    DELCARE <ident> : <type>
    ::
    ::
ENDTYPE
```
Example:
```
TYPE
Book
    DECLARE Name : STRING
    DECLARE PriceCents : INTEGER
    DECLARE PublishedDate : DATE
    DECLARE AuthorName : STRING
ENDTYPE
```
To reference a value inside a Record:
```
DECLARE Obj : TObjType
Obj.prop1 <- "Value1"
```
**Implementation in Java**
```java
public class Job {                                                                              // Defining template for inner class object
    private int payCents;
    public Job(int payCents) {
        this.payCents = payCents;
        return;
    }
    public int getPayCents() {
        return this.payCents;
    }
}
public class Person {                                                                           // Defining template for class object
    private String name;
    private Job job;
    private LocalDate dateBirth;
    public Person(String name, Job job, LocalDate dateBirth) {
        this.name = name;
        this.job = job;
        this.dateBirth = dateBirth;
        return;
    }
    public String getName() {
        return this.name;
    }
    public Job getJob() {
        return this.job;
    }
    public LocalDate getDateBirth() {
        return this.dateBirth;
    }
}

public class MainApp {
    public static void main(String[] args) {
        Person person = new Person("Jack", new Job(450000), new LocalDate("2007-01-01"));       // Object initialization
        System.out.println(person.name);
    }
}
```
### Explanation
Object definitions `RECORD`s can also include other object type definitions for the construction of multi-property multi-layer complex data types that encapsulate relevant data well, and can be used in enterprise-grade applications.
## 10.2 Arrays as collections of data


An **array** is a data structure containing serveral elements of the same data type: these elements can be accessed using the **same identifier name**. The position of each element in an array is defined using the array's **index**.
An array is defined in pseudocode as  
`DECLARE ArrayVariable : ARRAY[<start>:<end>] OF <type>`
A value can be the referenced from `ArrayVariable` in this format:  
`OUTPUT ArrayVariable[<index>] // where <start> < <index> < <end>`  

### Populating an array

```
FOR Counter <- <start> to <end>
    OUTPUT "Input value at pos ", Counter
    INPUT tmpVar
    ArrayVariable[Counter] <- tmpVar
NEXT Counter
```
**A similar implementation in Python:**
```python
array: list = []
target_length: int = 10
for i in range(0, target_length+1):
    val = int(input(f"Input value at pos {i}"))
    array.append(val)
print(".".join(array))
# or
for i in range(len(array)):
    print(array[i])
```


## 10.2.2 2-dimentional arrays


Essentially, 2-dimentional arrays are tables, aka. **arrays within arrays**.  
In pseudocode, it can be defined by: 
```
DECLARE <ident> : ARRAY[<lbound_row>:<hbound_row>, <lbound_col>:<hbound_col>] OF <datatype> 
// Example
DECLARE table : ARRAY[0:10, 0:5] OF INTEGER 
```

### Populate each element of a table

```
DECLARE table : ARRAY[0:10, 0:5] OF INTEGER     // First index = rows, second index = cols
DECLARE InputVal: INTEGER
FOR I <- 0 TO 10                                // Row loop
    FOR J <- 0 TO 5                             // Column loop
        OUTPUT "Input integer value of table at position ", I, ", ", J, ": "
        INPUT InputVal
        ARRAY[I, J] = InputVal
    NEXT J
NEXT I
```

**Implementation in Python**

```python
table: list = []
rows: int = int(input("Rows: "))
cols: int = int(input("Columns: "))
for i in range(rows):               # Loop over each row
    row = []
    for j in range(cols):           # Loop over each column
        row.append(int(input(f"integer value for table element at pos ({i}, {j}): ")))
    table.append(row)
# Output formatting section
output = ""
for row in table:
    output += f"{' '.join(row)}\n"
print(output)
```


## Implementing Linear search on an Array


```
DECLARE arr : ARRAY[0:<endIndex>] OF INTEGER
DECLARE item, ptr : INTEGER
DECLARE found : BOOLEAN
found <- FALSE
ptr <- 0
OUTPUT "Value of item to match: "
INPUT item
WHILE ptr < LENGTH(arr) OR found <> TRUE DO
    IF arr[ptr] = item
        THEN
            found <- TRUE
            OUTPUT "Match for ", item, " found at position ", index
    ENDIF
    ptr <- ptr + 1
```
**Implementation in Python**
```
import random
def generate_test_data(int length):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 100))
    return arr
test_data = generate_test_data(length)
found = False
match_data = int(input("Which one would you like to match for?"))
for data, index in test_data:
    if data == match_data:
        print(f"Found match for {data} at position {index}")
        break
    else:
        pass
```

## Implementing Bubble sort on an Array


```
DECLARE arr : ARRAY[0:<endIndex>] OF INTEGER
DECLARE ptr, swp, check, i: INTEGER
check <- 0
WHILE check < LENGTH(arr) - 1 DO            // gatekeeper loop; ensures that array after loop is properly sorted - array with LENGTH {x} can have at most {x-1} sorted element pairs  
    FOR ptr <- 0 TO LENGTH(arr) - 1
        IF arr[ptr] > arr[ptr + 1]          // Ascending sort: > ; Descending sort: <
            THEN
                swp <- arr[ptr]             // "cache" the arr[ptr] element to be referenced
                arr[ptr] <- arr[ptr + 1]    // alter value of arr[ptr] element (hence why we need swp (swap variable) to temporarily store value of arr[ptr])
                arr[ptr + 1] <- swp         // alter value of arr[ptr+1] (next-in-line) element with cached arr[ptr] value - swapping
            ELSE
                check <- check + 1          // incr. checks if this element pair passed check
        ENDIF
    NEXT ptr                                // incr. ptr to loop to the next element
ENDWHILE

// output result of sorted arr
FOR i <- 0 TO LENGTH(arr)
    OUTPUT "Element at pos ", i, ": ", arr[i]
NEXT i
```

### Explanation

The algorithm implemented above utilizes, most significantly, the check and ptr variable.
The check variable is used to verify that the array has been completely sorted before moving on with the program.
**This also means there will be always one iteration at the end where all elements are sorted, 
and the algorithm checks for all of the elements pass.**
The variable `swp` (shorthand for `swap`) is a temporary variable in place to cache the value of the element to prevent it from being modified by other processes.

**Implementation in Python**
```python
import random

def generate_test_data(length: int):
    arr = []
    for i in range(length):
        arr.append(random.randint(0, 100)
    return arr
testarr = generate_test_data(10)
index = 0
while checks < len(testarr): 
    checks = 0
    while index < len(testarr):
        if testarr[index] > testarr[index+1]:
            swp = testarr[index]
            testarr[index] = testarr[index+1]
            testarr[index+1] = swp
        else:
            checks += 1
        index += 1
print(testarr)
```
