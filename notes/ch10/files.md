# FIle handling in pseudocode
To open a file before reading from or writing to it:
```
OPEN <file_identifier> FOR <file_mode>
```
`<file_mode>` can be one of three: `READ`, `WRITE`, `APPEND`.
Sample write file handler pseudocode script:
```
DECLARE filePath :          STRING
DECLARE userInput, out :    STRING
OUTPUT "File path: "
INPUT filePath
OPEN filePath FOR WRITE
REPEAT
    OUTPUT "> "
    INPUT userInput
    IF userInput <> ""
        THEN
            WRITEFILE, userInput
        ELSE
            CLOSEFILE(filePath)
    ENDIF
UNTIL userInput = ""
OUTPUT "Now reading..."

REPEAT
    READFILE, out
    OUTPUT out
UNTIL EOF(filePath)
CLOSEFILE(filePath)
```

