MAX_HEIGHT = 25
MAX_WIDTH = 30
repeat
        print("Input a valid height: ")
        height = tonumber(io.read())
until height > 0 and height < MAX_HEIGHT
repeat
        print("Input a valid width: ")
        width = tonumber(io.read())
until width > 0 and width < MAX_WIDTH
print("Options for operation:\
h for calculating the hypotenuse\
a for calculating the area\
p for calculating the perimeter")
operation = io.read()
if operation == 'h' then
        print("Hypotenuse is ", tostring((height ^ 2 + width ^ 2) ^ 0.5))
elseif operation == 'a' then
        print("Area is ", tostring(height * width / 2))
elseif operation == 'p' then
        print("Perimeter is ", tostring(height + width + (height ^ 2 + width ^ 2) ^ 0.5))
else
        print("Invalid command verb! ")
end
